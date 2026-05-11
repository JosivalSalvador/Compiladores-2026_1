# Generated from Expressao.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExpressaoParser import ExpressaoParser
else:
    from ExpressaoParser import ExpressaoParser

# This class defines a complete listener for a parse tree produced by ExpressaoParser.
class ExpressaoListener(ParseTreeListener):

    # Enter a parse tree produced by ExpressaoParser#prog.
    def enterProg(self, ctx:ExpressaoParser.ProgContext):
        pass

    # Exit a parse tree produced by ExpressaoParser#prog.
    def exitProg(self, ctx:ExpressaoParser.ProgContext):
        pass


    # Enter a parse tree produced by ExpressaoParser#PassaTerm.
    def enterPassaTerm(self, ctx:ExpressaoParser.PassaTermContext):
        pass

    # Exit a parse tree produced by ExpressaoParser#PassaTerm.
    def exitPassaTerm(self, ctx:ExpressaoParser.PassaTermContext):
        pass


    # Enter a parse tree produced by ExpressaoParser#Soma.
    def enterSoma(self, ctx:ExpressaoParser.SomaContext):
        pass

    # Exit a parse tree produced by ExpressaoParser#Soma.
    def exitSoma(self, ctx:ExpressaoParser.SomaContext):
        pass


    # Enter a parse tree produced by ExpressaoParser#Subtracao.
    def enterSubtracao(self, ctx:ExpressaoParser.SubtracaoContext):
        pass

    # Exit a parse tree produced by ExpressaoParser#Subtracao.
    def exitSubtracao(self, ctx:ExpressaoParser.SubtracaoContext):
        pass


    # Enter a parse tree produced by ExpressaoParser#Multiplicacao.
    def enterMultiplicacao(self, ctx:ExpressaoParser.MultiplicacaoContext):
        pass

    # Exit a parse tree produced by ExpressaoParser#Multiplicacao.
    def exitMultiplicacao(self, ctx:ExpressaoParser.MultiplicacaoContext):
        pass


    # Enter a parse tree produced by ExpressaoParser#PassaPower.
    def enterPassaPower(self, ctx:ExpressaoParser.PassaPowerContext):
        pass

    # Exit a parse tree produced by ExpressaoParser#PassaPower.
    def exitPassaPower(self, ctx:ExpressaoParser.PassaPowerContext):
        pass


    # Enter a parse tree produced by ExpressaoParser#Divisao.
    def enterDivisao(self, ctx:ExpressaoParser.DivisaoContext):
        pass

    # Exit a parse tree produced by ExpressaoParser#Divisao.
    def exitDivisao(self, ctx:ExpressaoParser.DivisaoContext):
        pass


    # Enter a parse tree produced by ExpressaoParser#Potenciacao.
    def enterPotenciacao(self, ctx:ExpressaoParser.PotenciacaoContext):
        pass

    # Exit a parse tree produced by ExpressaoParser#Potenciacao.
    def exitPotenciacao(self, ctx:ExpressaoParser.PotenciacaoContext):
        pass


    # Enter a parse tree produced by ExpressaoParser#PassaUnary.
    def enterPassaUnary(self, ctx:ExpressaoParser.PassaUnaryContext):
        pass

    # Exit a parse tree produced by ExpressaoParser#PassaUnary.
    def exitPassaUnary(self, ctx:ExpressaoParser.PassaUnaryContext):
        pass


    # Enter a parse tree produced by ExpressaoParser#Fatorial.
    def enterFatorial(self, ctx:ExpressaoParser.FatorialContext):
        pass

    # Exit a parse tree produced by ExpressaoParser#Fatorial.
    def exitFatorial(self, ctx:ExpressaoParser.FatorialContext):
        pass


    # Enter a parse tree produced by ExpressaoParser#ValorAbsoluto.
    def enterValorAbsoluto(self, ctx:ExpressaoParser.ValorAbsolutoContext):
        pass

    # Exit a parse tree produced by ExpressaoParser#ValorAbsoluto.
    def exitValorAbsoluto(self, ctx:ExpressaoParser.ValorAbsolutoContext):
        pass


    # Enter a parse tree produced by ExpressaoParser#PassaAtom.
    def enterPassaAtom(self, ctx:ExpressaoParser.PassaAtomContext):
        pass

    # Exit a parse tree produced by ExpressaoParser#PassaAtom.
    def exitPassaAtom(self, ctx:ExpressaoParser.PassaAtomContext):
        pass


    # Enter a parse tree produced by ExpressaoParser#Parentesis.
    def enterParentesis(self, ctx:ExpressaoParser.ParentesisContext):
        pass

    # Exit a parse tree produced by ExpressaoParser#Parentesis.
    def exitParentesis(self, ctx:ExpressaoParser.ParentesisContext):
        pass


    # Enter a parse tree produced by ExpressaoParser#Numero.
    def enterNumero(self, ctx:ExpressaoParser.NumeroContext):
        pass

    # Exit a parse tree produced by ExpressaoParser#Numero.
    def exitNumero(self, ctx:ExpressaoParser.NumeroContext):
        pass



del ExpressaoParser