# Generated from Expressao.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,65,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,25,8,1,10,1,12,1,28,
        9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,39,8,2,10,2,12,2,42,
        9,2,1,3,1,3,1,3,1,3,1,3,3,3,49,8,3,1,4,1,4,1,4,1,4,1,4,3,4,56,8,
        4,1,5,1,5,1,5,1,5,1,5,3,5,63,8,5,1,5,0,2,2,4,6,0,2,4,6,8,10,0,0,
        66,0,12,1,0,0,0,2,15,1,0,0,0,4,29,1,0,0,0,6,48,1,0,0,0,8,55,1,0,
        0,0,10,62,1,0,0,0,12,13,3,2,1,0,13,14,5,0,0,1,14,1,1,0,0,0,15,16,
        6,1,-1,0,16,17,3,4,2,0,17,26,1,0,0,0,18,19,10,3,0,0,19,20,5,1,0,
        0,20,25,3,4,2,0,21,22,10,2,0,0,22,23,5,2,0,0,23,25,3,4,2,0,24,18,
        1,0,0,0,24,21,1,0,0,0,25,28,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,
        27,3,1,0,0,0,28,26,1,0,0,0,29,30,6,2,-1,0,30,31,3,6,3,0,31,40,1,
        0,0,0,32,33,10,3,0,0,33,34,5,3,0,0,34,39,3,6,3,0,35,36,10,2,0,0,
        36,37,5,4,0,0,37,39,3,6,3,0,38,32,1,0,0,0,38,35,1,0,0,0,39,42,1,
        0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,5,1,0,0,0,42,40,1,0,0,0,43,
        44,3,8,4,0,44,45,5,5,0,0,45,46,3,6,3,0,46,49,1,0,0,0,47,49,3,8,4,
        0,48,43,1,0,0,0,48,47,1,0,0,0,49,7,1,0,0,0,50,51,5,6,0,0,51,56,3,
        8,4,0,52,53,5,7,0,0,53,56,3,8,4,0,54,56,3,10,5,0,55,50,1,0,0,0,55,
        52,1,0,0,0,55,54,1,0,0,0,56,9,1,0,0,0,57,58,5,8,0,0,58,59,3,2,1,
        0,59,60,5,9,0,0,60,63,1,0,0,0,61,63,5,10,0,0,62,57,1,0,0,0,62,61,
        1,0,0,0,63,11,1,0,0,0,7,24,26,38,40,48,55,62
    ]

class ExpressaoParser ( Parser ):

    grammarFileName = "Expressao.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'^'", "'fact'", 
                     "'absoluto'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_term = 2
    RULE_power = 3
    RULE_unary = 4
    RULE_atom = 5

    ruleNames =  [ "prog", "expr", "term", "power", "unary", "atom" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    NUMBER=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(ExpressaoParser.ExprContext,0)


        def EOF(self):
            return self.getToken(ExpressaoParser.EOF, 0)

        def getRuleIndex(self):
            return ExpressaoParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ExpressaoParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.expr(0)
            self.state = 13
            self.match(ExpressaoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExpressaoParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class PassaTermContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpressaoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(ExpressaoParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPassaTerm" ):
                listener.enterPassaTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPassaTerm" ):
                listener.exitPassaTerm(self)


    class SomaContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpressaoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExpressaoParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(ExpressaoParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSoma" ):
                listener.enterSoma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSoma" ):
                listener.exitSoma(self)


    class SubtracaoContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpressaoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExpressaoParser.ExprContext,0)

        def term(self):
            return self.getTypedRuleContext(ExpressaoParser.TermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubtracao" ):
                listener.enterSubtracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubtracao" ):
                listener.exitSubtracao(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExpressaoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ExpressaoParser.PassaTermContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 16
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 26
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 24
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        localctx = ExpressaoParser.SomaContext(self, ExpressaoParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 18
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 19
                        self.match(ExpressaoParser.T__0)
                        self.state = 20
                        self.term(0)
                        pass

                    elif la_ == 2:
                        localctx = ExpressaoParser.SubtracaoContext(self, ExpressaoParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 21
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 22
                        self.match(ExpressaoParser.T__1)
                        self.state = 23
                        self.term(0)
                        pass

             
                self.state = 28
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExpressaoParser.RULE_term

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MultiplicacaoContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpressaoParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(ExpressaoParser.TermContext,0)

        def power(self):
            return self.getTypedRuleContext(ExpressaoParser.PowerContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicacao" ):
                listener.enterMultiplicacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicacao" ):
                listener.exitMultiplicacao(self)


    class PassaPowerContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpressaoParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def power(self):
            return self.getTypedRuleContext(ExpressaoParser.PowerContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPassaPower" ):
                listener.enterPassaPower(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPassaPower" ):
                listener.exitPassaPower(self)


    class DivisaoContext(TermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpressaoParser.TermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def term(self):
            return self.getTypedRuleContext(ExpressaoParser.TermContext,0)

        def power(self):
            return self.getTypedRuleContext(ExpressaoParser.PowerContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivisao" ):
                listener.enterDivisao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivisao" ):
                listener.exitDivisao(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExpressaoParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_term, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ExpressaoParser.PassaPowerContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 30
            self.power()
            self._ctx.stop = self._input.LT(-1)
            self.state = 40
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 38
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = ExpressaoParser.MultiplicacaoContext(self, ExpressaoParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 32
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 33
                        self.match(ExpressaoParser.T__2)
                        self.state = 34
                        self.power()
                        pass

                    elif la_ == 2:
                        localctx = ExpressaoParser.DivisaoContext(self, ExpressaoParser.TermContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                        self.state = 35
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 36
                        self.match(ExpressaoParser.T__3)
                        self.state = 37
                        self.power()
                        pass

             
                self.state = 42
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PowerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExpressaoParser.RULE_power

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PassaUnaryContext(PowerContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpressaoParser.PowerContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unary(self):
            return self.getTypedRuleContext(ExpressaoParser.UnaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPassaUnary" ):
                listener.enterPassaUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPassaUnary" ):
                listener.exitPassaUnary(self)


    class PotenciacaoContext(PowerContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpressaoParser.PowerContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unary(self):
            return self.getTypedRuleContext(ExpressaoParser.UnaryContext,0)

        def power(self):
            return self.getTypedRuleContext(ExpressaoParser.PowerContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPotenciacao" ):
                listener.enterPotenciacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPotenciacao" ):
                listener.exitPotenciacao(self)



    def power(self):

        localctx = ExpressaoParser.PowerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_power)
        try:
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = ExpressaoParser.PotenciacaoContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.unary()
                self.state = 44
                self.match(ExpressaoParser.T__4)
                self.state = 45
                self.power()
                pass

            elif la_ == 2:
                localctx = ExpressaoParser.PassaUnaryContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.unary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExpressaoParser.RULE_unary

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PassaAtomContext(UnaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpressaoParser.UnaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(ExpressaoParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPassaAtom" ):
                listener.enterPassaAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPassaAtom" ):
                listener.exitPassaAtom(self)


    class ValorAbsolutoContext(UnaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpressaoParser.UnaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unary(self):
            return self.getTypedRuleContext(ExpressaoParser.UnaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValorAbsoluto" ):
                listener.enterValorAbsoluto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValorAbsoluto" ):
                listener.exitValorAbsoluto(self)


    class FatorialContext(UnaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpressaoParser.UnaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unary(self):
            return self.getTypedRuleContext(ExpressaoParser.UnaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFatorial" ):
                listener.enterFatorial(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFatorial" ):
                listener.exitFatorial(self)



    def unary(self):

        localctx = ExpressaoParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_unary)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = ExpressaoParser.FatorialContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(ExpressaoParser.T__5)
                self.state = 51
                self.unary()
                pass
            elif token in [7]:
                localctx = ExpressaoParser.ValorAbsolutoContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(ExpressaoParser.T__6)
                self.state = 53
                self.unary()
                pass
            elif token in [8, 10]:
                localctx = ExpressaoParser.PassaAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExpressaoParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NumeroContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpressaoParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(ExpressaoParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)


    class ParentesisContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExpressaoParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(ExpressaoParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentesis" ):
                listener.enterParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentesis" ):
                listener.exitParentesis(self)



    def atom(self):

        localctx = ExpressaoParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_atom)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                localctx = ExpressaoParser.ParentesisContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self.match(ExpressaoParser.T__7)
                self.state = 58
                self.expr(0)
                self.state = 59
                self.match(ExpressaoParser.T__8)
                pass
            elif token in [10]:
                localctx = ExpressaoParser.NumeroContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.match(ExpressaoParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        self._predicates[2] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




