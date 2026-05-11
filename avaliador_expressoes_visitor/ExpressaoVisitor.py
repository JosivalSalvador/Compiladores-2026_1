# Generated from Expressao.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExpressaoParser import ExpressaoParser
else:
    from ExpressaoParser import ExpressaoParser

# This class defines a complete generic visitor for a parse tree produced by ExpressaoParser.

class ExpressaoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExpressaoParser#prog.
    def visitProg(self, ctx:ExpressaoParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressaoParser#PassaTerm.
    def visitPassaTerm(self, ctx:ExpressaoParser.PassaTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressaoParser#Soma.
    def visitSoma(self, ctx:ExpressaoParser.SomaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressaoParser#Subtracao.
    def visitSubtracao(self, ctx:ExpressaoParser.SubtracaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressaoParser#Multiplicacao.
    def visitMultiplicacao(self, ctx:ExpressaoParser.MultiplicacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressaoParser#PassaPower.
    def visitPassaPower(self, ctx:ExpressaoParser.PassaPowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressaoParser#Divisao.
    def visitDivisao(self, ctx:ExpressaoParser.DivisaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressaoParser#Potenciacao.
    def visitPotenciacao(self, ctx:ExpressaoParser.PotenciacaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressaoParser#PassaUnary.
    def visitPassaUnary(self, ctx:ExpressaoParser.PassaUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressaoParser#Fatorial.
    def visitFatorial(self, ctx:ExpressaoParser.FatorialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressaoParser#ValorAbsoluto.
    def visitValorAbsoluto(self, ctx:ExpressaoParser.ValorAbsolutoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressaoParser#PassaAtom.
    def visitPassaAtom(self, ctx:ExpressaoParser.PassaAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressaoParser#Parentesis.
    def visitParentesis(self, ctx:ExpressaoParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExpressaoParser#Numero.
    def visitNumero(self, ctx:ExpressaoParser.NumeroContext):
        return self.visitChildren(ctx)



del ExpressaoParser