from MiniCVisitor import MiniCVisitor
from MiniCParser  import MiniCParser


class MiniCThreeAddressCodeVisitor(MiniCVisitor):

    def __init__(self):
        self._temp_count  = 0
        self._label_count = 0
        self._code        = []
        # rótulos de break/continue do while atual; None fora de while
        self._break_label    = None
        self._continue_label = None

    # -------------------------------------------------------------------------
    # Helpers
    # -------------------------------------------------------------------------

    def _new_temp(self):
        # gera próximo temporário: t1, t2, ...
        self._temp_count += 1
        return f't{self._temp_count}'

    def _new_label(self):
        # gera próximo rótulo: L1, L2, ...
        self._label_count += 1
        return f'L{self._label_count}'

    def _emit(self, instr):
        self._code.append(instr)

    def get_code(self):
        return '\n'.join(self._code)

    # -------------------------------------------------------------------------
    # Programa e definições
    # -------------------------------------------------------------------------

    def visitProgram(self, ctx: MiniCParser.ProgramContext):
        return self.visitChildren(ctx)

    def visitDefinition(self, ctx: MiniCParser.DefinitionContext):
        return self.visitChildren(ctx)

    def visitData_definition(self, ctx: MiniCParser.Data_definitionContext):
        # declarações não geram instrução intermediária
        return None

    # -------------------------------------------------------------------------
    # Função
    # -------------------------------------------------------------------------

    def visitFunction_definition(self, ctx: MiniCParser.Function_definitionContext):
        header = ctx.function_header()
        nome   = header.declarator().IDENTIFIER().getText()

        self._emit(f'func {nome}:')

        # emite cada parâmetro formal
        param_decl = header.parameter_list().parameter_declaration()
        if param_decl:
            for d in param_decl.declarator():
                self._emit(f'    param {d.IDENTIFIER().getText()}')

        self.visit(ctx.function_body())
        self._emit(f'endfunc {nome}')
        self._emit('')
        return None

    def visitFunction_body(self, ctx: MiniCParser.Function_bodyContext):
        # declarações locais não geram código; visita só os statements
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    def visitBlock(self, ctx: MiniCParser.BlockContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return None

    # -------------------------------------------------------------------------
    # Statements
    # -------------------------------------------------------------------------

    def visitStatement(self, ctx: MiniCParser.StatementContext):

        # expression ;
        if ctx.expression() and not ctx.IF() and not ctx.WHILE() and not ctx.RETURN():
            self.visit(ctx.expression())
            return None

        # if ( expr ) stat [ else stat ]
        if ctx.IF():
            cond     = self.visit(ctx.expression())
            then_lbl = self._new_label()
            end_lbl  = self._new_label()
            stmts    = ctx.statement()

            if len(stmts) == 2:
                # if-else
                else_lbl = self._new_label()
                self._emit(f'    if {cond} goto {then_lbl}')
                self._emit(f'    goto {else_lbl}')
                self._emit(f'{then_lbl}:')
                self.visit(stmts[0])
                self._emit(f'    goto {end_lbl}')
                self._emit(f'{else_lbl}:')
                self.visit(stmts[1])
            else:
                self._emit(f'    if {cond} goto {then_lbl}')
                self._emit(f'    goto {end_lbl}')
                self._emit(f'{then_lbl}:')
                self.visit(stmts[0])

            self._emit(f'{end_lbl}:')
            return None

        # while ( expr ) stat
        if ctx.WHILE():
            start_lbl = self._new_label()
            body_lbl  = self._new_label()
            end_lbl   = self._new_label()

            # salva rótulos do while exterior para suportar aninhamento
            prev_break    = self._break_label
            prev_continue = self._continue_label
            self._break_label    = end_lbl
            self._continue_label = start_lbl

            self._emit(f'{start_lbl}:')
            cond = self.visit(ctx.expression())
            self._emit(f'    if {cond} goto {body_lbl}')
            self._emit(f'    goto {end_lbl}')
            self._emit(f'{body_lbl}:')
            self.visit(ctx.statement(0))
            self._emit(f'    goto {start_lbl}')
            self._emit(f'{end_lbl}:')

            # restaura rótulos do while exterior
            self._break_label    = prev_break
            self._continue_label = prev_continue
            return None

        # break ;
        if ctx.BREAK():
            self._emit(f'    goto {self._break_label}')
            return None

        # continue ;
        if ctx.CONTINUE():
            self._emit(f'    goto {self._continue_label}')
            return None

        # return [ expr ] ;
        if ctx.RETURN():
            if ctx.expression():
                val = self.visit(ctx.expression())
                self._emit(f'    return {val}')
            else:
                self._emit('    return')
            return None

        # block ou ; (statement vazio)
        return self.visitChildren(ctx)

    # -------------------------------------------------------------------------
    # Expression — atribuições ficam aqui após separação da gramática
    # -------------------------------------------------------------------------

    def visitBinaryExpr(self, ctx: MiniCParser.BinaryExprContext):
        # expression que é só um binary: delega
        return self.visit(ctx.binary())

    def _visitar_atribuicao(self, ctx, op):
        nome = ctx.IDENTIFIER().getText()
        # lado direito agora é expression() após separação na gramática
        val  = self.visit(ctx.expression())

        if op == '=':
            # x = val
            self._emit(f'    {nome} = {val}')
        else:
            # x op= val  →  t = x arith val ; x = t
            arith = op[0]   # '+', '-', '*', '/', '%'
            t = self._new_temp()
            self._emit(f'    {t} = {nome} {arith} {val}')
            self._emit(f'    {nome} = {t}')

        return nome

    def visitAssignExpr(self,    ctx): return self._visitar_atribuicao(ctx, '=')
    def visitAssignAddExpr(self, ctx): return self._visitar_atribuicao(ctx, '+=')
    def visitAssignSubExpr(self, ctx): return self._visitar_atribuicao(ctx, '-=')
    def visitAssignMulExpr(self, ctx): return self._visitar_atribuicao(ctx, '*=')
    def visitAssignDivExpr(self, ctx): return self._visitar_atribuicao(ctx, '/=')
    def visitAssignModExpr(self, ctx): return self._visitar_atribuicao(ctx, '%=')

    # -------------------------------------------------------------------------
    # Operadores binários (relacionais e aritméticos)
    # -------------------------------------------------------------------------

    def _visitar_bin_op(self, ctx, op):
        # t = left op right
        left  = self.visit(ctx.binary(0))
        right = self.visit(ctx.binary(1))
        t     = self._new_temp()
        self._emit(f'    {t} = {left} {op} {right}')
        return t

    def visitEqExpr(self,  ctx): return self._visitar_bin_op(ctx, '==')
    def visitNeqExpr(self, ctx): return self._visitar_bin_op(ctx, '!=')
    def visitLtExpr(self,  ctx): return self._visitar_bin_op(ctx, '<')
    def visitLeExpr(self,  ctx): return self._visitar_bin_op(ctx, '<=')
    def visitGtExpr(self,  ctx): return self._visitar_bin_op(ctx, '>')
    def visitGeExpr(self,  ctx): return self._visitar_bin_op(ctx, '>=')
    def visitAddExpr(self, ctx): return self._visitar_bin_op(ctx, '+')
    def visitSubExpr(self, ctx): return self._visitar_bin_op(ctx, '-')
    def visitMulExpr(self, ctx): return self._visitar_bin_op(ctx, '*')
    def visitDivExpr(self, ctx): return self._visitar_bin_op(ctx, '/')
    def visitModExpr(self, ctx): return self._visitar_bin_op(ctx, '%')

    # -------------------------------------------------------------------------
    # Unary
    # -------------------------------------------------------------------------

    def visitUnaryExpr(self, ctx: MiniCParser.UnaryExprContext):
        return self.visit(ctx.unary())

    def visitPreInc(self, ctx: MiniCParser.PreIncContext):
        # ++x  →  t = x + 1 ; x = t
        nome = ctx.IDENTIFIER().getText()
        t    = self._new_temp()
        self._emit(f'    {t} = {nome} + 1')
        self._emit(f'    {nome} = {t}')
        return nome

    def visitPreDec(self, ctx: MiniCParser.PreDecContext):
        # --x  →  t = x - 1 ; x = t
        nome = ctx.IDENTIFIER().getText()
        t    = self._new_temp()
        self._emit(f'    {t} = {nome} - 1')
        self._emit(f'    {nome} = {t}')
        return nome

    def visitPrimaryExpr(self, ctx: MiniCParser.PrimaryExprContext):
        return self.visit(ctx.primary())

    # -------------------------------------------------------------------------
    # Primary
    # -------------------------------------------------------------------------

    def visitIdentPrimary(self, ctx: MiniCParser.IdentPrimaryContext):
        return ctx.IDENTIFIER().getText()

    def visitIntPrimary(self, ctx: MiniCParser.IntPrimaryContext):
        return ctx.CONSTANT_INT().getText()

    def visitCharPrimary(self, ctx: MiniCParser.CharPrimaryContext):
        return ctx.CONSTANT_CHAR().getText()

    def visitParenPrimary(self, ctx: MiniCParser.ParenPrimaryContext):
        return self.visit(ctx.expression())

    def visitCallPrimary(self, ctx: MiniCParser.CallPrimaryContext):
        # avalia argumentos, emite param para cada um, emite call
        nome     = ctx.IDENTIFIER().getText()
        arg_list = ctx.argument_list()
        # argumentos agora são expression() após separação na gramática
        args     = arg_list.expression() if arg_list else []

        vals = [self.visit(a) for a in args]
        for v in vals:
            self._emit(f'    param {v}')

        t = self._new_temp()
        self._emit(f'    {t} = call {nome}, {len(args)}')
        return t