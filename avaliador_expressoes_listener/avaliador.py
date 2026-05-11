"""
avaliador.py
Implementação do padrão LISTENER para avaliação de expressões aritméticas.
"""

import math
from ExpressaoListener import ExpressaoListener
from ExpressaoParser   import ExpressaoParser


class AvaliadorExpressoes(ExpressaoListener):
    """
    Listener que calcula o valor de cada nó da árvore sintática.
    Os valores sobem da folha para a raiz via dicionário ctx -> float.
    """

    def __init__(self):
        self._val = {}          # contexto -> valor calculado

    def resultado(self, ctx):
        """Valor final (chamar com o contexto raiz 'prog')."""
        return self._val.get(ctx)

    # -- prog --
    def exitProg(self, ctx: ExpressaoParser.ProgContext):
        self._val[ctx] = self._val[ctx.expr()]

    # -- expr --
    def exitSoma(self, ctx: ExpressaoParser.SomaContext):
        self._val[ctx] = self._val[ctx.expr()] + self._val[ctx.term()]

    def exitSubtracao(self, ctx: ExpressaoParser.SubtracaoContext):
        self._val[ctx] = self._val[ctx.expr()] - self._val[ctx.term()]

    def exitPassaTerm(self, ctx: ExpressaoParser.PassaTermContext):
        self._val[ctx] = self._val[ctx.term()]

    # -- term --
    def exitMultiplicacao(self, ctx: ExpressaoParser.MultiplicacaoContext):
        self._val[ctx] = self._val[ctx.term()] * self._val[ctx.power()]

    def exitDivisao(self, ctx: ExpressaoParser.DivisaoContext):
        divisor = self._val[ctx.power()]
        if divisor == 0:
            raise ZeroDivisionError("Divisão por zero!")
        self._val[ctx] = self._val[ctx.term()] / divisor

    def exitPassaPower(self, ctx: ExpressaoParser.PassaPowerContext):
        self._val[ctx] = self._val[ctx.power()]

    # -- power --
    def exitPotenciacao(self, ctx: ExpressaoParser.PotenciacaoContext):
        self._val[ctx] = self._val[ctx.unary()] ** self._val[ctx.power()]

    def exitPassaUnary(self, ctx: ExpressaoParser.PassaUnaryContext):
        self._val[ctx] = self._val[ctx.unary()]

    # -- unary --
    def exitFatorial(self, ctx: ExpressaoParser.FatorialContext):
        v = self._val[ctx.unary()]
        n = int(v)
        if n < 0 or n != v:
            raise ValueError(f"Fatorial indefinido para {v}")
        self._val[ctx] = float(math.factorial(n))

    def exitValorAbsoluto(self, ctx: ExpressaoParser.ValorAbsolutoContext):
        self._val[ctx] = abs(self._val[ctx.unary()])

    def exitPassaAtom(self, ctx: ExpressaoParser.PassaAtomContext):
        self._val[ctx] = self._val[ctx.atom()]

    # -- atom --
    def exitParentesis(self, ctx: ExpressaoParser.ParentesisContext):
        self._val[ctx] = self._val[ctx.expr()]

    def exitNumero(self, ctx: ExpressaoParser.NumeroContext):
        self._val[ctx] = float(ctx.NUMBER().getText())