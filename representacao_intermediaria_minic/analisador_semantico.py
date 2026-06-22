"""
analisador_semantico.py
Visitor semântico para a linguagem MiniC.
Cobre todos os itens do trabalho:
  a) variáveis não declaradas
  b) variáveis declaradas mais de uma vez
  c) número de argumentos em chamadas de função
  d) tipos dos argumentos em chamadas de função
  e) compatibilidade de tipos na atribuição (=, +=, -=, *=, /=, %=)
  f) operandos de +, -, *, /, % devem ser int
  g) break e continue só dentro de while
Todos os erros são acumulados numa lista e impressos no final.
"""

from MiniCVisitor import MiniCVisitor
from MiniCParser  import MiniCParser


# =============================================================================
# PARTE 1 — Tabela de símbolos e estrutura base do Visitor
# =============================================================================

class AnalisadorSemantico(MiniCVisitor):

    def __init__(self):
        # Lista que acumula todos os erros encontrados
        self.erros = []

        # Tabela global: nome -> {'tipo': 'int'|'char'|'func', ...}
        # Funções guardam também 'param_types' (lista de tipos dos parâmetros)
        self.tabela_global = {}

        # Escopo local da função atual; None quando fora de qualquer função
        self.escopo_local = None

        # Profundidade de whiles aninhados; 0 = fora de while
        self.profundidade_while = 0

        # Tipo resolvido de cada nó de expressão: ctx -> 'int' | 'char' | None
        self.tipos = {}

    # -------------------------------------------------------------------------
    # Helpers de escopo
    # -------------------------------------------------------------------------

    def _declarar(self, nome, info, linha, col):
        # Declara 'nome' no escopo atual; erro se já existir (item b)
        escopo = self.escopo_local if self.escopo_local is not None else self.tabela_global
        if nome in escopo:
            self._erro(linha, col, f"'{nome}' já foi declarado neste escopo")
        else:
            escopo[nome] = info

    def _buscar(self, nome):
        # Procura 'nome' no escopo local e depois no global
        if self.escopo_local is not None and nome in self.escopo_local:
            return self.escopo_local[nome]
        return self.tabela_global.get(nome)

    # -------------------------------------------------------------------------
    # Helper de tipo
    # -------------------------------------------------------------------------

    def _tipo(self, ctx):
        # Retorna o tipo já resolvido para o nó ctx, ou None se não determinado
        return self.tipos.get(ctx)

    # -------------------------------------------------------------------------
    # Helper de erro
    # -------------------------------------------------------------------------

    def _erro(self, linha, col, mensagem):
        # Formata e acumula erro com linha e coluna
        self.erros.append(f"Linha {linha}, col {col}: ERRO — {mensagem}")


# =============================================================================
# PARTE 2 — Declarações, funções, parâmetros e chamadas (itens a, b, c, d)
# =============================================================================

    def visitData_definition(self, ctx: MiniCParser.Data_definitionContext):
        # Declara cada variável no escopo atual; detecta redeclaração (item b)
        tipo = ctx.getChild(0).getText()  # 'int' ou 'char'
        for decl in ctx.declarator():
            nome  = decl.IDENTIFIER().getText()
            linha = decl.IDENTIFIER().getSymbol().line
            col   = decl.IDENTIFIER().getSymbol().column
            self._declarar(nome, {'tipo': tipo}, linha, col)
        return self.visitChildren(ctx)

    def visitFunction_definition(self, ctx: MiniCParser.Function_definitionContext):
        # Registra a função na tabela global, abre escopo, visita corpo, fecha escopo
        tipo_retorno = 'int' if ctx.INT() is not None else 'void'
        header       = ctx.function_header()
        nome_func    = header.declarator().IDENTIFIER().getText()
        linha        = header.declarator().IDENTIFIER().getSymbol().line
        col          = header.declarator().IDENTIFIER().getSymbol().column
        param_types  = self._coletar_param_types(header.parameter_list())

        self._declarar(nome_func, {
            'tipo': 'func',
            'retorno': tipo_retorno,
            'param_types': param_types
        }, linha, col)

        self.escopo_local = {}
        self._declarar_params(header.parameter_list())
        self.visit(ctx.function_body())
        self.escopo_local = None
        return None

    def _coletar_param_types(self, param_list_ctx):
        # Retorna lista de tipos dos parâmetros; [] se não houver
        param_types = []
        decl = param_list_ctx.parameter_declaration()
        if decl is None:
            return param_types
        tipo = decl.getChild(0).getText()  # 'int' ou 'char'
        for _ in decl.declarator():
            param_types.append(tipo)
        return param_types

    def _declarar_params(self, param_list_ctx):
        # Declara cada parâmetro no escopo local; detecta redeclaração (item b)
        decl = param_list_ctx.parameter_declaration()
        if decl is None:
            return
        tipo = decl.getChild(0).getText()  # 'int' ou 'char'
        for d in decl.declarator():
            nome  = d.IDENTIFIER().getText()
            linha = d.IDENTIFIER().getSymbol().line
            col   = d.IDENTIFIER().getSymbol().column
            self._declarar(nome, {'tipo': tipo}, linha, col)

    def visitIdentPrimary(self, ctx: MiniCParser.IdentPrimaryContext):
        # Verifica se variável foi declarada (item a) e propaga seu tipo
        nome  = ctx.IDENTIFIER().getText()
        linha = ctx.IDENTIFIER().getSymbol().line
        col   = ctx.IDENTIFIER().getSymbol().column
        info  = self._buscar(nome)
        if info is None:
            self._erro(linha, col, f"variável '{nome}' não declarada")
            self.tipos[ctx] = None
        else:
            self.tipos[ctx] = info['tipo']
        return self.visitChildren(ctx)

    def visitIntPrimary(self, ctx: MiniCParser.IntPrimaryContext):
        # Literal inteiro: tipo fixo 'int'
        self.tipos[ctx] = 'int'
        return self.visitChildren(ctx)

    def visitCharPrimary(self, ctx: MiniCParser.CharPrimaryContext):
        # Literal char ('a'): tipo fixo 'char'
        self.tipos[ctx] = 'char'
        return self.visitChildren(ctx)

    def visitParenPrimary(self, ctx: MiniCParser.ParenPrimaryContext):
        # Expressão entre parênteses: herda o tipo do filho
        self.visitChildren(ctx)
        self.tipos[ctx] = self._tipo(ctx.expression())
        return None

    def visitCallPrimary(self, ctx: MiniCParser.CallPrimaryContext):
        # Verifica número de argumentos (item c) e tipos (item d)
        nome  = ctx.IDENTIFIER().getText()
        linha = ctx.IDENTIFIER().getSymbol().line
        col   = ctx.IDENTIFIER().getSymbol().column

        self.visitChildren(ctx)

        info = self._buscar(nome)
        if info is None:
            self._erro(linha, col, f"função '{nome}' não declarada")
            self.tipos[ctx] = None
            return None
        if info['tipo'] != 'func':
            self._erro(linha, col, f"'{nome}' não é uma função")
            self.tipos[ctx] = None
            return None

        param_types = info['param_types']
        arg_list    = ctx.argument_list()
        args        = arg_list.expression() if arg_list else []

        # item c: quantidade de argumentos
        if len(args) != len(param_types):
            self._erro(linha, col,
                f"'{nome}' espera {len(param_types)} argumento(s), "
                f"mas recebeu {len(args)}")
        else:
            # item d: tipos dos argumentos
            for i, (arg, tipo_esp) in enumerate(zip(args, param_types)):
                tipo_arg = self._tipo(arg)
                if tipo_arg is not None and tipo_arg != tipo_esp:
                    self._erro(arg.start.line, arg.start.column,
                        f"argumento {i+1} de '{nome}': "
                        f"esperado '{tipo_esp}', recebido '{tipo_arg}'")

        self.tipos[ctx] = info['retorno'] if info['retorno'] != 'void' else None
        return None


# =============================================================================
# PARTE 3 — Tipos em expressões, atribuições, aritmética e break/continue
#           (itens e, f, g)
# =============================================================================

    # -------------------------------------------------------------------------
    # Propagação de tipo em unary
    # -------------------------------------------------------------------------

    def visitPreInc(self, ctx: MiniCParser.PreIncContext):
        # Pré-incremento (++x): verifica declaração e propaga tipo
        nome  = ctx.IDENTIFIER().getText()
        linha = ctx.IDENTIFIER().getSymbol().line
        col   = ctx.IDENTIFIER().getSymbol().column
        info  = self._buscar(nome)
        if info is None:
            self._erro(linha, col, f"variável '{nome}' não declarada")
            self.tipos[ctx] = None
        else:
            self.tipos[ctx] = info['tipo']
        return self.visitChildren(ctx)

    def visitPreDec(self, ctx: MiniCParser.PreDecContext):
        # Pré-decremento (--x): mesmo comportamento do preInc
        nome  = ctx.IDENTIFIER().getText()
        linha = ctx.IDENTIFIER().getSymbol().line
        col   = ctx.IDENTIFIER().getSymbol().column
        info  = self._buscar(nome)
        if info is None:
            self._erro(linha, col, f"variável '{nome}' não declarada")
            self.tipos[ctx] = None
        else:
            self.tipos[ctx] = info['tipo']
        return self.visitChildren(ctx)

    def visitPrimaryExpr(self, ctx: MiniCParser.PrimaryExprContext):
        # Unary que é só uma primary: herda o tipo do filho
        self.visitChildren(ctx)
        self.tipos[ctx] = self._tipo(ctx.primary())
        return None

    def visitUnaryExpr(self, ctx: MiniCParser.UnaryExprContext):
        # Binary que é só um unary: herda o tipo do filho
        self.visitChildren(ctx)
        self.tipos[ctx] = self._tipo(ctx.unary())
        return None

    # -------------------------------------------------------------------------
    # Operadores relacionais — resultado sempre int (0 ou 1)
    # -------------------------------------------------------------------------

    def _visitar_relacional(self, ctx):
        # Comparações (==, !=, <, <=, >, >=): resultado sempre int
        self.visitChildren(ctx)
        self.tipos[ctx] = 'int'
        return None

    def visitEqExpr(self, ctx):  return self._visitar_relacional(ctx)
    def visitNeqExpr(self, ctx): return self._visitar_relacional(ctx)
    def visitLtExpr(self, ctx):  return self._visitar_relacional(ctx)
    def visitLeExpr(self, ctx):  return self._visitar_relacional(ctx)
    def visitGtExpr(self, ctx):  return self._visitar_relacional(ctx)
    def visitGeExpr(self, ctx):  return self._visitar_relacional(ctx)

    # -------------------------------------------------------------------------
    # Operadores aritméticos — item f: operandos devem ser int
    # -------------------------------------------------------------------------

    def _visitar_aritmetico(self, ctx, op):
        # item f: ambos os operandos devem ser int; resultado é int se ok, None se erro
        self.visitChildren(ctx)

        esq      = ctx.binary(0)
        dir      = ctx.binary(1)
        tipo_esq = self._tipo(esq)
        tipo_dir = self._tipo(dir)
        erro     = False

        if tipo_esq is not None and tipo_esq != 'int':
            self._erro(esq.start.line, esq.start.column,
                f"operando esquerdo de '{op}' deve ser int, mas é '{tipo_esq}'")
            erro = True

        if tipo_dir is not None and tipo_dir != 'int':
            self._erro(dir.start.line, dir.start.column,
                f"operando direito de '{op}' deve ser int, mas é '{tipo_dir}'")
            erro = True

        # Se houve erro propaga None para evitar erros duplos acima
        self.tipos[ctx] = None if erro else 'int'
        return None

    def visitAddExpr(self, ctx): return self._visitar_aritmetico(ctx, '+')
    def visitSubExpr(self, ctx): return self._visitar_aritmetico(ctx, '-')
    def visitMulExpr(self, ctx): return self._visitar_aritmetico(ctx, '*')
    def visitDivExpr(self, ctx): return self._visitar_aritmetico(ctx, '/')
    def visitModExpr(self, ctx): return self._visitar_aritmetico(ctx, '%')

    # -------------------------------------------------------------------------
    # Atribuições simples e compostas — item e
    # -------------------------------------------------------------------------

    def _visitar_atribuicao(self, ctx, op):
        # item e: tipo da expressão direita deve bater com o tipo da variável
        # item f: operadores compostos aritméticos exigem variável int
        nome  = ctx.IDENTIFIER().getText()
        linha = ctx.IDENTIFIER().getSymbol().line
        col   = ctx.IDENTIFIER().getSymbol().column

        self.visitChildren(ctx)

        info = self._buscar(nome)
        if info is None:
            self._erro(linha, col, f"variável '{nome}' não declarada")
            self.tipos[ctx] = None
            return None

        tipo_var = info['tipo']
        # lado direito agora é expression() pois atribuição está em expression
        tipo_dir = self._tipo(ctx.expression())

        # item f: operadores compostos exigem variável int
        if op != '=' and tipo_var != 'int':
            self._erro(linha, col,
                f"operador '{op}' requer variável do tipo int, "
                f"mas '{nome}' é '{tipo_var}'")
            self.tipos[ctx] = tipo_var
            return None

        # item e: tipos devem ser compatíveis; só verifica se tipo_dir é conhecido
        if tipo_dir is not None and tipo_dir != tipo_var:
            self._erro(linha, col,
                f"atribuição incompatível: '{nome}' é '{tipo_var}', "
                f"mas a expressão é '{tipo_dir}'")

        self.tipos[ctx] = tipo_var
        return None

    def visitAssignExpr(self,    ctx): return self._visitar_atribuicao(ctx, '=')
    def visitAssignAddExpr(self, ctx): return self._visitar_atribuicao(ctx, '+=')
    def visitAssignSubExpr(self, ctx): return self._visitar_atribuicao(ctx, '-=')
    def visitAssignMulExpr(self, ctx): return self._visitar_atribuicao(ctx, '*=')
    def visitAssignDivExpr(self, ctx): return self._visitar_atribuicao(ctx, '/=')
    def visitAssignModExpr(self, ctx): return self._visitar_atribuicao(ctx, '%=')

    # -------------------------------------------------------------------------
    # Propagação de tipo em expression
    # -------------------------------------------------------------------------

    def visitBinaryExpr(self, ctx: MiniCParser.BinaryExprContext):
        # expression que é só um binary: herda seu tipo
        self.visitChildren(ctx)
        self.tipos[ctx] = self._tipo(ctx.binary())
        return None

    # -------------------------------------------------------------------------
    # Laço while e break/continue — item g
    # -------------------------------------------------------------------------

    def visitStatement(self, ctx: MiniCParser.StatementContext):
        # item g: controla profundidade de while; detecta break/continue fora de laço
        if ctx.WHILE():
            self.profundidade_while += 1
            self.visitChildren(ctx)
            self.profundidade_while -= 1
            return None

        if ctx.BREAK():
            if self.profundidade_while == 0:
                tok = ctx.BREAK().getSymbol()
                self._erro(tok.line, tok.column,
                    "'break' utilizado fora de laço while")
            return None

        if ctx.CONTINUE():
            if self.profundidade_while == 0:
                tok = ctx.CONTINUE().getSymbol()
                self._erro(tok.line, tok.column,
                    "'continue' utilizado fora de laço while")
            return None

        return self.visitChildren(ctx)


# =============================================================================
# Função auxiliar para rodar o analisador e imprimir os erros
# =============================================================================

def analisar(tree, parser):
    # Roda o visitor semântico e imprime todos os erros encontrados no final
    analisador = AnalisadorSemantico()
    analisador.visit(tree)

    if analisador.erros:
        print(f"\n{'='*50}")
        print(f"Análise semântica: {len(analisador.erros)} erro(s) encontrado(s):")
        print(f"{'='*50}")
        for erro in analisador.erros:
            print(f"  {erro}")
        print(f"{'='*50}\n")
    else:
        print("\nAnálise semântica: nenhum erro encontrado.\n")

    return analisador.erros