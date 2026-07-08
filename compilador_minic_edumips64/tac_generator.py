# Autor: Josival Salvador Monteiro Júnior
# Trabalho 09 - Geração de Código Assembly do EduMIPS64
#
# Gerador de código de três endereços (TAC) a partir da AST do MiniC.


from MiniCParser import MiniCParser
from MiniCVisitor import MiniCVisitor


# Valores ASCII das sequências de escape aceitas por CONSTANT_CHAR/STRING no
# MiniC.g4 (mesmo conjunto do fragment EscapeSequence: \b \t \n \f \r \0 \\ \' \")
ESCAPE_ORDINALS = {
    'b': 8, 't': 9, 'n': 10, 'f': 12, 'r': 13,
    '0': 0, '\\': 92, "'": 39, '"': 34,
}


def char_text_to_ordinal(text):
    """Converte o texto bruto de um CONSTANT_CHAR (ex: "'a'" ou "'\\n'") no
    valor ASCII inteiro do caractere, como string -- 'operand' do TAC.g4 so
    aceita ID ou INT, nao existe operando do tipo char."""
    inner = text[1:-1]  # remove as aspas simples
    if inner.startswith('\\'):
        return str(ESCAPE_ORDINALS[inner[1]])
    return str(ord(inner))


class TACGenerator(MiniCVisitor):

    def __init__(self, global_vars, functions, function_locals):
        self.global_vars = global_vars
        self.functions = functions
        self.function_locals = function_locals

        self.temp_count = 0
        self.label_count = 0

        self.current_lines = None      # linhas da funcao sendo gerada agora
        self.current_param_map = {}    # nome do parametro -> 'p0', 'p1', ...
        self.break_labels = []         # pilha de rotulos de saida (break)
        self.continue_labels = []      # pilha de rotulos de topo (continue)

        self.func_blocks = []          # [(nome, n_params, [linhas]), ...]

    # ---------- utilidades ----------

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

    def emit(self, line):
        self.current_lines.append(line)

    def resolve_name(self, name):
        """Parametros da funcao atual sao referenciados no corpo pelo nome
        declarado (ex: 'a'), mas no TAC (e no interpretador do trabalho 8) so
        existem como p0, p1, ... na ordem declarada -- entao toda leitura ou
        escrita de identificador passa por aqui."""
        return self.current_param_map.get(name, name)

    # ---------- ponto de entrada ----------

    def generate(self, tree: MiniCParser.ProgramContext) -> str:
        global_init_lines = []   # "nome = valor" das globais com inicializador, na ordem do fonte

        for definition in tree.definition():
            if definition.data_definition():
                self.gen_global_init(definition.data_definition(), global_init_lines)
            elif definition.function_definition():
                self.gen_function(definition.function_definition())

        lines = []
        lines.extend(global_init_lines)   # solta, ANTES de qualquer func (ver exemplo do enunciado)

        for name, n_params, body in self.func_blocks:
            lines.append(f"func {name}, {n_params}:")
            for ln in body:
                if ln.endswith(':'):   # rotulo -> sem indentacao (estilo do enunciado)
                    lines.append(ln)
                else:
                    lines.append(f"    {ln}")
            lines.append("endfunc")
            lines.append("")

        # kickoff: o interpretador do trabalho 8 nao chama 'main' sozinho (ver nota 5)
        lines.append("_main_result = call main, 0")

        return "\n".join(lines)

    def gen_global_init(self, ctx: MiniCParser.Data_definitionContext, out: list):
        """Globais SEM inicializador nao geram nenhuma linha (a memoria
        reservada ja nasce zerada -- ver mips_generator.py). As que tem
        '= valor' viram uma atribuicao solta, fora de qualquer func --
        exatamente a posicao do 'global_counter = 0' no exemplo do
        enunciado."""
        for decl in ctx.init_declarator():
            init = decl.expression()
            if init is not None:
                name = decl.IDENTIFIER().getText()
                out.append(f"{name} = {self.global_init_operand(init)}")

    def global_init_operand(self, init_ctx) -> str:
        """Extrai o valor literal de um inicializador de global. O
        semantic_analyzer.py ja garante (is_constant_literal) que so chega
        aqui uma constante pura (int ou char), entao basta descer direto ate
        o primary -- sem precisar do eval_expr/visit genericos."""
        primary = init_ctx.binary().unary().primary()
        if isinstance(primary, MiniCParser.CharPrimaryContext):
            return char_text_to_ordinal(primary.CONSTANT_CHAR().getText())
        return primary.CONSTANT_INT().getText()

    # ---------- geracao de uma funcao ----------

    def gen_function(self, ctx: MiniCParser.Function_definitionContext):
        name = ctx.function_header().declarator().IDENTIFIER().getText()
        params = self.functions[name]['params']  # [(tipo, nome), ...]
        n_params = len(params)

        self.temp_count = 0
        self.label_count = 0
        self.current_lines = []
        self.current_param_map = {pname: f"p{i}" for i, (_, pname) in enumerate(params)}
        self.break_labels = []
        self.continue_labels = []

        for dd in ctx.function_body().data_definition():
            self.gen_local_init(dd)

        for st in ctx.function_body().statement():
            self.gen_statement(st)

        if not self.current_lines or not self.current_lines[-1].startswith("return "):
            self.emit("return 0")   # toda funcao termina com return explicito (ver nota 2)

        self.func_blocks.append((name, n_params, self.current_lines))
        self.current_lines = None
        self.current_param_map = {}

    def gen_local_init(self, ctx: MiniCParser.Data_definitionContext):
        """Locais SEM inicializador nao precisam de nenhuma linha aqui (o
        slot so passa a existir no assembly na primeira vez que a variavel e
        lida ou escrita -- ver collect_vars() do mips_generator.py). As que
        tem '= expressao' viram uma atribuicao comum, emitida como os
        primeiros statements da funcao -- na mesma ordem em que aparecem no
        fonte, o que tambem garante 'declare antes de usar' entre
        inicializadores (ex: 'int a = 1, b = a;' funciona; 'int a = b, b = 1;'
        nao, porque b ainda nao existe quando o inicializador de a e
        avaliado)."""
        for decl in ctx.init_declarator():
            init = decl.expression()
            if init is not None:
                target = self.resolve_name(decl.IDENTIFIER().getText())
                operand = self.eval_expr(init)
                self.emit(f"{target} = {operand}")

    # ---------- statements ----------

    def gen_statement(self, ctx: MiniCParser.StatementContext):
        if ctx.IF():
            self.gen_if(ctx)
        elif ctx.WHILE():
            self.gen_while(ctx)
        elif ctx.BREAK():
            self.emit(f"goto {self.break_labels[-1]}")
        elif ctx.CONTINUE():
            self.emit(f"goto {self.continue_labels[-1]}")
        elif ctx.RETURN():
            expr = ctx.expression()
            if expr is not None:
                operand = self.eval_expr(expr)
                self.emit(f"return {operand}")
            else:
                self.emit("return 0")   # ver nota 2
        elif ctx.printf_statement():
            self.gen_printf(ctx.printf_statement())
        elif ctx.block():
            for st in ctx.block().statement():
                self.gen_statement(st)
        elif ctx.expression():
            self.eval_expr(ctx.expression())   # descarta o operando resultante

    def gen_if(self, ctx: MiniCParser.StatementContext):
        cond = self.eval_expr(ctx.expression())
        l_true = self.new_label()
        l_false = self.new_label()

        self.emit(f"if {cond} goto {l_true}")
        self.emit(f"goto {l_false}")
        self.emit(f"{l_true}:")
        self.gen_statement(ctx.statement(0))

        if ctx.ELSE():
            l_end = self.new_label()
            self.emit(f"goto {l_end}")
            self.emit(f"{l_false}:")
            self.gen_statement(ctx.statement(1))
            self.emit(f"{l_end}:")
        else:
            self.emit(f"{l_false}:")

    def gen_while(self, ctx: MiniCParser.StatementContext):
        l_start = self.new_label()
        l_body = self.new_label()
        l_end = self.new_label()

        self.emit(f"{l_start}:")
        cond = self.eval_expr(ctx.expression())
        self.emit(f"if {cond} goto {l_body}")
        self.emit(f"goto {l_end}")
        self.emit(f"{l_body}:")

        self.break_labels.append(l_end)
        self.continue_labels.append(l_start)
        self.gen_statement(ctx.statement(0))
        self.break_labels.pop()
        self.continue_labels.pop()

        self.emit(f"goto {l_start}")
        self.emit(f"{l_end}:")

    def gen_printf(self, ctx: MiniCParser.Printf_statementContext):
        arg = ctx.printf_argument()
        if isinstance(arg, MiniCParser.PrintfArgIdentContext):
            operand = self.resolve_name(arg.IDENTIFIER().getText())
        elif isinstance(arg, MiniCParser.PrintfArgIntContext):
            operand = arg.CONSTANT_INT().getText()
        else:  # PrintfArgCharContext
            operand = char_text_to_ordinal(arg.CONSTANT_CHAR().getText())
        self.emit(f"print {operand}")

    # ---------- expressoes (cada eval_expr retorna um operando: ID ou INT como texto) ----------

    def eval_expr(self, ctx):
        return self.visit(ctx)

    def visitAssignExpr(self, ctx: MiniCParser.AssignExprContext):
        target = self.resolve_name(ctx.IDENTIFIER().getText())
        operand = self.eval_expr(ctx.expression())
        self.emit(f"{target} = {operand}")
        return operand

    def gen_compound_assign(self, ctx, op_symbol):
        target = self.resolve_name(ctx.IDENTIFIER().getText())
        rhs = self.eval_expr(ctx.expression())
        temp = self.new_temp()
        self.emit(f"{temp} = {target} {op_symbol} {rhs}")
        self.emit(f"{target} = {temp}")
        return temp

    def visitAssignAddExpr(self, ctx: MiniCParser.AssignAddExprContext):
        return self.gen_compound_assign(ctx, '+')

    def visitAssignSubExpr(self, ctx: MiniCParser.AssignSubExprContext):
        return self.gen_compound_assign(ctx, '-')

    def visitAssignMulExpr(self, ctx: MiniCParser.AssignMulExprContext):
        return self.gen_compound_assign(ctx, '*')

    def visitAssignDivExpr(self, ctx: MiniCParser.AssignDivExprContext):
        return self.gen_compound_assign(ctx, '/')

    def visitAssignModExpr(self, ctx: MiniCParser.AssignModExprContext):
        return self.gen_compound_assign(ctx, '%')

    def visitBinaryExpr(self, ctx: MiniCParser.BinaryExprContext):
        return self.eval_expr(ctx.binary())

    def gen_binary_op(self, ctx, op_symbol):
        left = self.eval_expr(ctx.binary(0))
        right = self.eval_expr(ctx.binary(1))
        temp = self.new_temp()
        self.emit(f"{temp} = {left} {op_symbol} {right}")
        return temp

    def visitEqExpr(self, ctx: MiniCParser.EqExprContext):
        return self.gen_binary_op(ctx, '==')

    def visitNeqExpr(self, ctx: MiniCParser.NeqExprContext):
        return self.gen_binary_op(ctx, '!=')

    def visitLtExpr(self, ctx: MiniCParser.LtExprContext):
        return self.gen_binary_op(ctx, '<')

    def visitLeExpr(self, ctx: MiniCParser.LeExprContext):
        return self.gen_binary_op(ctx, '<=')

    def visitGtExpr(self, ctx: MiniCParser.GtExprContext):
        return self.gen_binary_op(ctx, '>')

    def visitGeExpr(self, ctx: MiniCParser.GeExprContext):
        return self.gen_binary_op(ctx, '>=')

    def visitAddExpr(self, ctx: MiniCParser.AddExprContext):
        return self.gen_binary_op(ctx, '+')

    def visitSubExpr(self, ctx: MiniCParser.SubExprContext):
        return self.gen_binary_op(ctx, '-')

    def visitMulExpr(self, ctx: MiniCParser.MulExprContext):
        return self.gen_binary_op(ctx, '*')

    def visitDivExpr(self, ctx: MiniCParser.DivExprContext):
        return self.gen_binary_op(ctx, '/')

    def visitModExpr(self, ctx: MiniCParser.ModExprContext):
        return self.gen_binary_op(ctx, '%')

    def visitUnaryExpr(self, ctx: MiniCParser.UnaryExprContext):
        return self.eval_expr(ctx.unary())

    def visitPreInc(self, ctx: MiniCParser.PreIncContext):
        target = self.resolve_name(ctx.IDENTIFIER().getText())
        temp = self.new_temp()
        self.emit(f"{temp} = {target} + 1")
        self.emit(f"{target} = {temp}")
        return temp

    def visitPreDec(self, ctx: MiniCParser.PreDecContext):
        target = self.resolve_name(ctx.IDENTIFIER().getText())
        temp = self.new_temp()
        self.emit(f"{temp} = {target} - 1")
        self.emit(f"{target} = {temp}")
        return temp

    def visitPrimaryExpr(self, ctx: MiniCParser.PrimaryExprContext):
        return self.eval_expr(ctx.primary())

    def visitCallPrimary(self, ctx: MiniCParser.CallPrimaryContext):
        name = ctx.IDENTIFIER().getText()
        args = ctx.argument_list().expression() if ctx.argument_list() else []

        for a in args:
            operand = self.eval_expr(a)
            self.emit(f"param {operand}")

        temp = self.new_temp()
        self.emit(f"{temp} = call {name}, {len(args)}")
        return temp

    def visitIdentPrimary(self, ctx: MiniCParser.IdentPrimaryContext):
        return self.resolve_name(ctx.IDENTIFIER().getText())

    def visitIntPrimary(self, ctx: MiniCParser.IntPrimaryContext):
        return ctx.CONSTANT_INT().getText()

    def visitCharPrimary(self, ctx: MiniCParser.CharPrimaryContext):
        return char_text_to_ordinal(ctx.CONSTANT_CHAR().getText())

    def visitParenPrimary(self, ctx: MiniCParser.ParenPrimaryContext):
        return self.eval_expr(ctx.expression())