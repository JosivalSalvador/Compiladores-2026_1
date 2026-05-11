"""
avaliador.py
Implementação do padrão VISITOR para avaliação de expressões aritméticas.
"""

import math
from ExpressaoVisitor import ExpressaoVisitor
from ExpressaoParser  import ExpressaoParser


class AvaliadorExpressoes(ExpressaoVisitor):
    """
    Visitor que percorre a árvore sintática e retorna o valor
    calculado de cada nó diretamente (sem dicionário auxiliar).
    """

    # -- prog --
    def visitProg(self, ctx: ExpressaoParser.ProgContext):
        return self.visit(ctx.expr())

    # -- expr --
    def visitSoma(self, ctx: ExpressaoParser.SomaContext):
        return self.visit(ctx.expr()) + self.visit(ctx.term())

    def visitSubtracao(self, ctx: ExpressaoParser.SubtracaoContext):
        return self.visit(ctx.expr()) - self.visit(ctx.term())

    def visitPassaTerm(self, ctx: ExpressaoParser.PassaTermContext):
        return self.visit(ctx.term())

    # -- term --
    def visitMultiplicacao(self, ctx: ExpressaoParser.MultiplicacaoContext):
        return self.visit(ctx.term()) * self.visit(ctx.power())

    def visitDivisao(self, ctx: ExpressaoParser.DivisaoContext):
        divisor = self.visit(ctx.power())
        if divisor == 0:
            raise ZeroDivisionError("Divisão por zero!")
        return self.visit(ctx.term()) / divisor

    def visitPassaPower(self, ctx: ExpressaoParser.PassaPowerContext):
        return self.visit(ctx.power())

    # -- power --
    def visitPotenciacao(self, ctx: ExpressaoParser.PotenciacaoContext):
        return self.visit(ctx.unary()) ** self.visit(ctx.power())

    def visitPassaUnary(self, ctx: ExpressaoParser.PassaUnaryContext):
        return self.visit(ctx.unary())

    # -- unary --
    def visitFatorial(self, ctx: ExpressaoParser.FatorialContext):
        v = self.visit(ctx.unary())
        n = int(v)
        if n < 0 or n != v:
            raise ValueError(f"Fatorial indefinido para {v}")
        return float(math.factorial(n))

    def visitValorAbsoluto(self, ctx: ExpressaoParser.ValorAbsolutoContext):
        return abs(self.visit(ctx.unary()))

    def visitPassaAtom(self, ctx: ExpressaoParser.PassaAtomContext):
        return self.visit(ctx.atom())

    # -- atom --
    def visitParentesis(self, ctx: ExpressaoParser.ParentesisContext):
        return self.visit(ctx.expr())

    def visitNumero(self, ctx: ExpressaoParser.NumeroContext):
        return float(ctx.NUMBER().getText())