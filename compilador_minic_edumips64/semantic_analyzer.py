# Autor: Josival Salvador Monteiro Júnior
# Trabalho 09 - Geração de Código Assembly do EduMIPS64
#
# Analisador semântico do MiniC.
#
# Percorre a árvore de sintaxe gerada pelo parser (via MiniC.g4) em duas
# passadas:
#   1) coleta variáveis globais e assinaturas de função (nome, tipo de
#      retorno, parâmetros), sem entrar nos corpos — assim funções podem se
#      chamar em qualquer ordem, inclusive recursivamente (observação 3);
#   2) analisa o corpo de cada função: declarações locais, tipos, uso de
#      identificadores/funções não declarados, break/continue fora de while,
#      retorno compatível com a assinatura, e a chamada printf("%d\n", arg).
#
# Ao final, expõe:
#   .errors          -> lista de strings com os erros encontrados (vazia = ok)
#   .global_vars     -> {nome: 'int'|'char'}
#   .functions       -> {nome: {'return_type': 'int'|None, 'params': [(tipo,nome), ...]}}
#   .function_locals -> {nome_func: {nome_var: 'int'|'char'}}  (inclui parâmetros)
#
# Essas três últimas estruturas são a tabela de símbolos que o tac_generator.py
# (próximo arquivo) reaproveita, em vez de percorrer a AST de novo do zero.

from MiniCParser import MiniCParser
from MiniCVisitor import MiniCVisitor


class SemanticAnalyzer(MiniCVisitor):

    def __init__(self):
        self.global_vars = {}       # nome -> 'int' | 'char'
        self.functions = {}         # nome -> {'return_type': 'int'|None, 'params': [(tipo,nome), ...]}
        self.function_locals = {}   # nome_func -> {nome_var: 'int'|'char'}  (params + locais)
        self.errors = []

        self.current_function = None      # nome da função sendo analisada (fase 2)
        self.current_return_type = None   # tipo de retorno esperado na função atual
        self.loop_depth = 0                # profundidade de laços 'while' (p/ break/continue)

    # ---------- utilidades ----------

    def error(self, ctx, msg):
        line = ctx.start.line if ctx is not None else '?'
        self.errors.append(f"[linha {line}] Erro semantico: {msg}")

    def is_declared(self, name):
        locals_ = self.function_locals.get(self.current_function, {})
        return name in locals_ or name in self.global_vars

    def lookup_type(self, name):
        locals_ = self.function_locals.get(self.current_function, {})
        if name in locals_:
            return locals_[name]
        return self.global_vars.get(name)

    def check_variable(self, name, ctx, contexto=""):
        """Verifica se 'name' e uma variavel valida (local ou global) e registra erro caso contrario."""
        if self.is_declared(name):
            return True
        sufixo = f" ({contexto})" if contexto else ""
        if name in self.functions:
            self.error(ctx, f"'{name}' e uma funcao, nao uma variavel{sufixo}")
        else:
            self.error(ctx, f"variavel '{name}' nao declarada{sufixo}")
        return False

    def check_function(self, name, ctx):
        """Verifica se 'name' e uma funcao valida e registra erro caso contrario."""
        if name in self.functions:
            return True
        if self.is_declared(name):
            self.error(ctx, f"'{name}' e uma variavel, nao pode ser chamada como funcao")
        else:
            self.error(ctx, f"funcao '{name}' nao foi definida")
        return False

    def is_constant_literal(self, expr_ctx):
        """Verifica se 'expr_ctx' e uma constante literal pura (int ou char),
        sem operador, variavel ou chamada -- e o unico formato aceito para o
        inicializador de uma variavel GLOBAL (nao ha avaliador de expressoes
        constantes; a regra e deliberadamente simples: soh literal direto,
        como em 'int global_counter = 0;')."""
        if not isinstance(expr_ctx, MiniCParser.BinaryExprContext):
            return False
        binary_ctx = expr_ctx.binary()
        if not isinstance(binary_ctx, MiniCParser.UnaryExprContext):
            return False
        unary_ctx = binary_ctx.unary()
        if not isinstance(unary_ctx, MiniCParser.PrimaryExprContext):
            return False
        primary_ctx = unary_ctx.primary()
        return isinstance(primary_ctx, (MiniCParser.IntPrimaryContext, MiniCParser.CharPrimaryContext))

    # ---------- ponto de entrada ----------

    def analyze(self, tree: MiniCParser.ProgramContext):
        definitions = tree.definition()

        # PASSO 1: coleta globais e assinaturas de funcao (sem entrar nos corpos)
        for definition in definitions:
            if definition.data_definition():
                self.collect_global_var(definition.data_definition())
            elif definition.function_definition():
                self.collect_function_signature(definition.function_definition())

        # a funcao 'main' e o ponto de entrada exigido (usado como 'func main, 0:' no TAC
        # e como label 'main:' no assembly final)
        if 'main' not in self.functions:
            self.error(None, "funcao 'main' nao foi definida (e o ponto de entrada exigido do programa)")
        elif len(self.functions['main']['params']) != 0:
            self.error(None, "funcao 'main' nao deve receber parametros")

        # PASSO 2: analisa o corpo de cada funcao
        for definition in definitions:
            if definition.function_definition():
                self.analyze_function(definition.function_definition())

        return self.errors

    # ---------- PASSO 1: coleta de variaveis globais e assinaturas ----------

    def collect_global_var(self, ctx: MiniCParser.Data_definitionContext):
        var_type = 'int' if ctx.INT() else 'char'
        for decl in ctx.init_declarator():
            name = decl.IDENTIFIER().getText()
            if name in self.global_vars:
                self.error(ctx, f"variavel global '{name}' redeclarada")
            elif name in self.functions:
                self.error(ctx, f"'{name}' ja foi declarado como funcao")
            else:
                self.global_vars[name] = var_type

            # inicializador de global: so aceita constante literal pura,
            # nao ha avaliador de expressao constante (ex: 'int x = 0;' ok,
            # 'int x = 1 + 1;' ou 'int x = outra_var;' nao)
            init = decl.expression()
            if init is not None and not self.is_constant_literal(init):
                self.error(ctx, f"inicializador de '{name}' deve ser uma constante literal (int ou char), ex: 'int {name} = 0;'")

    def collect_function_signature(self, ctx: MiniCParser.Function_definitionContext):
        # ALTERAÇÃO: tipo de retorno agora pode ser INT, VOID (sinônimo de
        # "sem retorno") ou omitido -- nos dois últimos casos, ctx.INT() é
        # None e o resultado já cai corretamente em "sem retorno" (None).
        return_type = 'int' if ctx.INT() else None
        name = ctx.function_header().declarator().IDENTIFIER().getText()

        params = []
        param_decl = ctx.function_header().parameter_list().parameter_declaration()
        # ALTERAÇÃO: quando a lista de parâmetros é escrita como '(void)', a
        # alternativa que casa em 'parameter_list' é VOID, não
        # 'parameter_declaration' -- então 'param_decl' já vem None nesse
        # caso automaticamente, caindo no mesmo caminho de '()' vazio abaixo,
        # sem necessidade de checar VOID explicitamente aqui.
        if param_decl is not None:
            # ALTERAÇÃO: cada declarador pode ter seu próprio tipo (INT/CHAR)
            # logo antes dele, ou herdar o tipo do declarador anterior quando
            # omitido -- por isso não dá mais para ler 'param_decl.INT()' uma
            # única vez (pode haver vários tokens INT/CHAR na mesma lista).
            # Percorre os filhos na ordem em que aparecem no texto, guardando
            # o tipo mais recente visto e aplicando-o a cada declarator.
            current_type = None
            for child in param_decl.children:
                if isinstance(child, MiniCParser.DeclaratorContext):
                    params.append((current_type, child.IDENTIFIER().getText()))
                elif hasattr(child, 'getSymbol'):
                    tok_type = child.getSymbol().type
                    if tok_type == MiniCParser.INT:
                        current_type = 'int'
                    elif tok_type == MiniCParser.CHAR:
                        current_type = 'char'

        if name in self.functions:
            self.error(ctx, f"funcao '{name}' redeclarada")
        elif name in self.global_vars:
            self.error(ctx, f"'{name}' ja foi declarado como variavel global")
        else:
            self.functions[name] = {'return_type': return_type, 'params': params}

        # parametros ja entram como "locais" da funcao (referenciados pelo nome no corpo)
        locals_ = {}
        for p_type, p_name in params:
            if p_name in locals_:
                self.error(ctx, f"parametro '{p_name}' duplicado na funcao '{name}'")
            else:
                locals_[p_name] = p_type
        self.function_locals[name] = locals_

    # ---------- PASSO 2: analise do corpo de uma funcao ----------

    def analyze_function(self, ctx: MiniCParser.Function_definitionContext):
        name = ctx.function_header().declarator().IDENTIFIER().getText()
        self.current_function = name
        self.current_return_type = self.functions.get(name, {}).get('return_type')
        self.loop_depth = 0

        self.visit(ctx.function_body())

        self.current_function = None
        self.current_return_type = None

    def visitFunction_body(self, ctx: MiniCParser.Function_bodyContext):
        for dd in ctx.data_definition():
            self.collect_local_var(dd)
        for st in ctx.statement():
            self.visit(st)
        return None

    def collect_local_var(self, ctx: MiniCParser.Data_definitionContext):
        var_type = 'int' if ctx.INT() else 'char'
        locals_ = self.function_locals[self.current_function]
        for decl in ctx.init_declarator():
            name = decl.IDENTIFIER().getText()
            if name in locals_:
                self.error(ctx, f"variavel '{name}' redeclarada na funcao '{self.current_function}'")
            else:
                locals_[name] = var_type

            # inicializador de local: aceita qualquer expressao valida (pode
            # referenciar parametro ou outra local ja declarada antes dela --
            # 'is_declared' ja cobre isso porque 'name' so entra em 'locals_'
            # DEPOIS desta linha, entao 'int a = b;' antes de 'int b;' cai
            # corretamente como 'b' nao declarada)
            init = decl.expression()
            if init is not None:
                rhs_type = self.visit(init)
                if rhs_type == 'void':
                    self.error(ctx, f"nao e possivel inicializar '{name}' com o resultado de uma funcao sem retorno")

    def visitBlock(self, ctx: MiniCParser.BlockContext):
        for st in ctx.statement():
            self.visit(st)
        return None

    def visitStatement(self, ctx: MiniCParser.StatementContext):
        if ctx.IF():
            self.visit(ctx.expression())
            self.visit(ctx.statement(0))
            if ctx.ELSE():
                self.visit(ctx.statement(1))
        elif ctx.WHILE():
            self.visit(ctx.expression())
            self.loop_depth += 1
            self.visit(ctx.statement(0))
            self.loop_depth -= 1
        elif ctx.BREAK():
            if self.loop_depth == 0:
                self.error(ctx, "'break' usado fora de um laco 'while'")
        elif ctx.CONTINUE():
            if self.loop_depth == 0:
                self.error(ctx, "'continue' usado fora de um laco 'while'")
        elif ctx.RETURN():
            expr = ctx.expression()
            if expr is not None:
                if self.current_return_type is None:
                    self.error(ctx, f"funcao '{self.current_function}' nao retorna valor (void), mas 'return' possui expressao")
                self.visit(expr)
            else:
                if self.current_return_type is not None:
                    self.error(ctx, f"funcao '{self.current_function}' deve retornar um valor do tipo '{self.current_return_type}'")
        elif ctx.printf_statement():
            self.visit(ctx.printf_statement())
        elif ctx.block():
            self.visit(ctx.block())
        elif ctx.expression():
            self.visit(ctx.expression())
        # senao: statement vazio ';' -> nada a fazer
        return None

    def visitPrintf_statement(self, ctx: MiniCParser.Printf_statementContext):
        fmt_text = ctx.STRING().getText()
        if fmt_text != '"%d\\n"':
            self.error(ctx, f'printf so e aceito no formato exato printf("%d\\n", arg); (recebido {fmt_text})')
        self.visit(ctx.printf_argument())
        return None

    def visitPrintfArgIdent(self, ctx: MiniCParser.PrintfArgIdentContext):
        name = ctx.IDENTIFIER().getText()
        self.check_variable(name, ctx, 'printf')
        return None

    def visitPrintfArgInt(self, ctx: MiniCParser.PrintfArgIntContext):
        return None

    def visitPrintfArgChar(self, ctx: MiniCParser.PrintfArgCharContext):
        return None

    # ---------- expressoes (cada visit retorna o tipo resultante: 'int' | 'char' | 'void') ----------

    def visitAssignExpr(self, ctx: MiniCParser.AssignExprContext):
        name = ctx.IDENTIFIER().getText()
        self.check_variable(name, ctx, "atribuicao")
        rhs_type = self.visit(ctx.expression())
        if rhs_type == 'void':
            self.error(ctx, f"nao e possivel atribuir a '{name}' o resultado de uma funcao sem retorno")
        return self.lookup_type(name) or 'int'

    def visit_compound_assign(self, ctx, op_text):
        name = ctx.IDENTIFIER().getText()
        self.check_variable(name, ctx, op_text)
        rhs_type = self.visit(ctx.expression())
        if rhs_type == 'void':
            self.error(ctx, f"nao e possivel usar '{op_text}' com o resultado de uma funcao sem retorno")
        return self.lookup_type(name) or 'int'

    def visitAssignAddExpr(self, ctx: MiniCParser.AssignAddExprContext):
        return self.visit_compound_assign(ctx, '+=')

    def visitAssignSubExpr(self, ctx: MiniCParser.AssignSubExprContext):
        return self.visit_compound_assign(ctx, '-=')

    def visitAssignMulExpr(self, ctx: MiniCParser.AssignMulExprContext):
        return self.visit_compound_assign(ctx, '*=')

    def visitAssignDivExpr(self, ctx: MiniCParser.AssignDivExprContext):
        return self.visit_compound_assign(ctx, '/=')

    def visitAssignModExpr(self, ctx: MiniCParser.AssignModExprContext):
        return self.visit_compound_assign(ctx, '%=')

    def visitBinaryExpr(self, ctx: MiniCParser.BinaryExprContext):
        return self.visit(ctx.binary())

    def visit_binary_op(self, ctx):
        left = self.visit(ctx.binary(0))
        right = self.visit(ctx.binary(1))
        if left == 'void' or right == 'void':
            self.error(ctx, "uso de funcao sem retorno dentro de uma expressao")
        return 'int'

    def visitEqExpr(self, ctx: MiniCParser.EqExprContext):
        return self.visit_binary_op(ctx)

    def visitNeqExpr(self, ctx: MiniCParser.NeqExprContext):
        return self.visit_binary_op(ctx)

    def visitLtExpr(self, ctx: MiniCParser.LtExprContext):
        return self.visit_binary_op(ctx)

    def visitLeExpr(self, ctx: MiniCParser.LeExprContext):
        return self.visit_binary_op(ctx)

    def visitGtExpr(self, ctx: MiniCParser.GtExprContext):
        return self.visit_binary_op(ctx)

    def visitGeExpr(self, ctx: MiniCParser.GeExprContext):
        return self.visit_binary_op(ctx)

    def visitAddExpr(self, ctx: MiniCParser.AddExprContext):
        return self.visit_binary_op(ctx)

    def visitSubExpr(self, ctx: MiniCParser.SubExprContext):
        return self.visit_binary_op(ctx)

    def visitMulExpr(self, ctx: MiniCParser.MulExprContext):
        return self.visit_binary_op(ctx)

    def visitDivExpr(self, ctx: MiniCParser.DivExprContext):
        return self.visit_binary_op(ctx)

    def visitModExpr(self, ctx: MiniCParser.ModExprContext):
        return self.visit_binary_op(ctx)

    def visitUnaryExpr(self, ctx: MiniCParser.UnaryExprContext):
        return self.visit(ctx.unary())

    def visitPreInc(self, ctx: MiniCParser.PreIncContext):
        name = ctx.IDENTIFIER().getText()
        self.check_variable(name, ctx, '++')
        return self.lookup_type(name) or 'int'

    def visitPreDec(self, ctx: MiniCParser.PreDecContext):
        name = ctx.IDENTIFIER().getText()
        self.check_variable(name, ctx, '--')
        return self.lookup_type(name) or 'int'

    def visitPrimaryExpr(self, ctx: MiniCParser.PrimaryExprContext):
        return self.visit(ctx.primary())

    def visitCallPrimary(self, ctx: MiniCParser.CallPrimaryContext):
        name = ctx.IDENTIFIER().getText()
        args = ctx.argument_list().expression() if ctx.argument_list() else []
        for a in args:
            self.visit(a)  # valida sub-expressoes (variaveis, chamadas aninhadas, etc.)

        if not self.check_function(name, ctx):
            return 'int'

        expected = len(self.functions[name]['params'])
        if len(args) != expected:
            self.error(ctx, f"chamada a '{name}' espera {expected} argumento(s), recebeu {len(args)}")

        ret = self.functions[name]['return_type']
        return ret if ret is not None else 'void'

    def visitIdentPrimary(self, ctx: MiniCParser.IdentPrimaryContext):
        name = ctx.IDENTIFIER().getText()
        self.check_variable(name, ctx)
        return self.lookup_type(name) or 'int'

    def visitIntPrimary(self, ctx: MiniCParser.IntPrimaryContext):
        return 'int'

    def visitCharPrimary(self, ctx: MiniCParser.CharPrimaryContext):
        return 'char'

    def visitParenPrimary(self, ctx: MiniCParser.ParenPrimaryContext):
        return self.visit(ctx.expression())