# Generated from TAC.g4 by ANTLR 4.13.2
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
        4,1,30,138,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,1,0,4,0,34,8,0,11,0,12,0,35,1,0,1,0,1,1,1,1,
        3,1,42,8,1,1,2,1,2,1,2,1,2,1,2,1,2,5,2,50,8,2,10,2,12,2,53,9,2,1,
        2,1,2,1,3,3,3,58,8,3,1,3,1,3,3,3,62,8,3,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,1,5,1,5,3,5,73,8,5,1,6,1,6,1,6,1,6,3,6,79,8,6,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,94,8,7,1,8,1,8,1,9,1,9,
        1,10,1,10,1,10,1,10,1,10,3,10,105,8,10,1,11,1,11,1,11,3,11,110,8,
        11,1,12,1,12,1,12,1,12,5,12,116,8,12,10,12,12,12,119,9,12,1,12,3,
        12,122,8,12,1,13,1,13,3,13,126,8,13,1,14,1,14,1,14,3,14,131,8,14,
        1,15,1,15,1,15,3,15,136,8,15,1,15,0,0,16,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,30,0,2,2,0,8,8,10,20,1,0,26,27,143,0,33,1,0,0,0,2,
        41,1,0,0,0,4,43,1,0,0,0,6,61,1,0,0,0,8,63,1,0,0,0,10,72,1,0,0,0,
        12,74,1,0,0,0,14,93,1,0,0,0,16,95,1,0,0,0,18,97,1,0,0,0,20,99,1,
        0,0,0,22,106,1,0,0,0,24,111,1,0,0,0,26,125,1,0,0,0,28,127,1,0,0,
        0,30,132,1,0,0,0,32,34,3,2,1,0,33,32,1,0,0,0,34,35,1,0,0,0,35,33,
        1,0,0,0,35,36,1,0,0,0,36,37,1,0,0,0,37,38,5,0,0,1,38,1,1,0,0,0,39,
        42,3,4,2,0,40,42,3,6,3,0,41,39,1,0,0,0,41,40,1,0,0,0,42,3,1,0,0,
        0,43,44,5,1,0,0,44,45,5,26,0,0,45,46,5,2,0,0,46,47,5,27,0,0,47,51,
        5,3,0,0,48,50,3,6,3,0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,
        51,52,1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,4,0,0,55,5,1,0,
        0,0,56,58,3,8,4,0,57,56,1,0,0,0,57,58,1,0,0,0,58,59,1,0,0,0,59,62,
        3,10,5,0,60,62,3,8,4,0,61,57,1,0,0,0,61,60,1,0,0,0,62,7,1,0,0,0,
        63,64,5,26,0,0,64,65,5,3,0,0,65,9,1,0,0,0,66,73,3,12,6,0,67,73,3,
        20,10,0,68,73,3,22,11,0,69,73,3,24,12,0,70,73,3,28,14,0,71,73,3,
        30,15,0,72,66,1,0,0,0,72,67,1,0,0,0,72,68,1,0,0,0,72,69,1,0,0,0,
        72,70,1,0,0,0,72,71,1,0,0,0,73,11,1,0,0,0,74,75,5,26,0,0,75,76,5,
        5,0,0,76,78,3,14,7,0,77,79,5,6,0,0,78,77,1,0,0,0,78,79,1,0,0,0,79,
        13,1,0,0,0,80,81,5,7,0,0,81,82,5,26,0,0,82,83,5,2,0,0,83,94,5,27,
        0,0,84,85,3,18,9,0,85,86,3,16,8,0,86,87,3,18,9,0,87,94,1,0,0,0,88,
        89,5,8,0,0,89,94,3,18,9,0,90,91,5,9,0,0,91,94,3,18,9,0,92,94,3,18,
        9,0,93,80,1,0,0,0,93,84,1,0,0,0,93,88,1,0,0,0,93,90,1,0,0,0,93,92,
        1,0,0,0,94,15,1,0,0,0,95,96,7,0,0,0,96,17,1,0,0,0,97,98,7,1,0,0,
        98,19,1,0,0,0,99,100,5,21,0,0,100,101,3,18,9,0,101,102,5,22,0,0,
        102,104,5,26,0,0,103,105,5,6,0,0,104,103,1,0,0,0,104,105,1,0,0,0,
        105,21,1,0,0,0,106,107,5,22,0,0,107,109,5,26,0,0,108,110,5,6,0,0,
        109,108,1,0,0,0,109,110,1,0,0,0,110,23,1,0,0,0,111,112,5,23,0,0,
        112,117,3,26,13,0,113,114,5,2,0,0,114,116,3,26,13,0,115,113,1,0,
        0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,0,0,118,121,1,0,
        0,0,119,117,1,0,0,0,120,122,5,6,0,0,121,120,1,0,0,0,121,122,1,0,
        0,0,122,25,1,0,0,0,123,126,3,18,9,0,124,126,5,28,0,0,125,123,1,0,
        0,0,125,124,1,0,0,0,126,27,1,0,0,0,127,128,5,24,0,0,128,130,3,18,
        9,0,129,131,5,6,0,0,130,129,1,0,0,0,130,131,1,0,0,0,131,29,1,0,0,
        0,132,133,5,25,0,0,133,135,3,18,9,0,134,136,5,6,0,0,135,134,1,0,
        0,0,135,136,1,0,0,0,136,31,1,0,0,0,15,35,41,51,57,61,72,78,93,104,
        109,117,121,125,130,135
    ]

class TACParser ( Parser ):

    grammarFileName = "TAC.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'func'", "','", "':'", "'endfunc'", "'='", 
                     "';'", "'call'", "'-'", "'!'", "'+'", "'*'", "'/'", 
                     "'>'", "'>='", "'<'", "'<='", "'=='", "'!='", "'&&'", 
                     "'||'", "'if'", "'goto'", "'print'", "'param'", "'return'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "STRING", "WS", 
                      "COMMENT" ]

    RULE_prog = 0
    RULE_item = 1
    RULE_funcDef = 2
    RULE_instr = 3
    RULE_label = 4
    RULE_stmt = 5
    RULE_assign = 6
    RULE_rhs = 7
    RULE_op = 8
    RULE_operand = 9
    RULE_ifGoto = 10
    RULE_goto = 11
    RULE_printStat = 12
    RULE_printArg = 13
    RULE_paramStat = 14
    RULE_returnStat = 15

    ruleNames =  [ "prog", "item", "funcDef", "instr", "label", "stmt", 
                   "assign", "rhs", "op", "operand", "ifGoto", "goto", "printStat", 
                   "printArg", "paramStat", "returnStat" ]

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
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    ID=26
    INT=27
    STRING=28
    WS=29
    COMMENT=30

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

        def EOF(self):
            return self.getToken(TACParser.EOF, 0)

        def item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TACParser.ItemContext)
            else:
                return self.getTypedRuleContext(TACParser.ItemContext,i)


        def getRuleIndex(self):
            return TACParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = TACParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.item()
                self.state = 35 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 132120578) != 0)):
                    break

            self.state = 37
            self.match(TACParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcDef(self):
            return self.getTypedRuleContext(TACParser.FuncDefContext,0)


        def instr(self):
            return self.getTypedRuleContext(TACParser.InstrContext,0)


        def getRuleIndex(self):
            return TACParser.RULE_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem" ):
                listener.enterItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem" ):
                listener.exitItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = TACParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_item)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.funcDef()
                pass
            elif token in [21, 22, 23, 24, 25, 26]:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.instr()
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


    class FuncDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TACParser.ID, 0)

        def INT(self):
            return self.getToken(TACParser.INT, 0)

        def instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TACParser.InstrContext)
            else:
                return self.getTypedRuleContext(TACParser.InstrContext,i)


        def getRuleIndex(self):
            return TACParser.RULE_funcDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDef" ):
                listener.enterFuncDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDef" ):
                listener.exitFuncDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDef" ):
                return visitor.visitFuncDef(self)
            else:
                return visitor.visitChildren(self)




    def funcDef(self):

        localctx = TACParser.FuncDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(TACParser.T__0)
            self.state = 44
            self.match(TACParser.ID)
            self.state = 45
            self.match(TACParser.T__1)
            self.state = 46
            self.match(TACParser.INT)
            self.state = 47
            self.match(TACParser.T__2)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 132120576) != 0):
                self.state = 48
                self.instr()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(TACParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(TACParser.StmtContext,0)


        def label(self):
            return self.getTypedRuleContext(TACParser.LabelContext,0)


        def getRuleIndex(self):
            return TACParser.RULE_instr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstr" ):
                listener.enterInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstr" ):
                listener.exitInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstr" ):
                return visitor.visitInstr(self)
            else:
                return visitor.visitChildren(self)




    def instr(self):

        localctx = TACParser.InstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instr)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 56
                    self.label()


                self.state = 59
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.label()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TACParser.ID, 0)

        def getRuleIndex(self):
            return TACParser.RULE_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabel" ):
                listener.enterLabel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabel" ):
                listener.exitLabel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = TACParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(TACParser.ID)
            self.state = 64
            self.match(TACParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self):
            return self.getTypedRuleContext(TACParser.AssignContext,0)


        def ifGoto(self):
            return self.getTypedRuleContext(TACParser.IfGotoContext,0)


        def goto(self):
            return self.getTypedRuleContext(TACParser.GotoContext,0)


        def printStat(self):
            return self.getTypedRuleContext(TACParser.PrintStatContext,0)


        def paramStat(self):
            return self.getTypedRuleContext(TACParser.ParamStatContext,0)


        def returnStat(self):
            return self.getTypedRuleContext(TACParser.ReturnStatContext,0)


        def getRuleIndex(self):
            return TACParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = TACParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_stmt)
        try:
            self.state = 72
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.assign()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.ifGoto()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.goto()
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 4)
                self.state = 69
                self.printStat()
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 5)
                self.state = 70
                self.paramStat()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 6)
                self.state = 71
                self.returnStat()
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


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TACParser.ID, 0)

        def rhs(self):
            return self.getTypedRuleContext(TACParser.RhsContext,0)


        def getRuleIndex(self):
            return TACParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = TACParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(TACParser.ID)
            self.state = 75
            self.match(TACParser.T__4)
            self.state = 76
            self.rhs()
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 77
                self.match(TACParser.T__5)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TACParser.RULE_rhs

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NegRhsContext(RhsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.RhsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operand(self):
            return self.getTypedRuleContext(TACParser.OperandContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegRhs" ):
                listener.enterNegRhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegRhs" ):
                listener.exitNegRhs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegRhs" ):
                return visitor.visitNegRhs(self)
            else:
                return visitor.visitChildren(self)


    class CallRhsContext(RhsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.RhsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(TACParser.ID, 0)
        def INT(self):
            return self.getToken(TACParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallRhs" ):
                listener.enterCallRhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallRhs" ):
                listener.exitCallRhs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallRhs" ):
                return visitor.visitCallRhs(self)
            else:
                return visitor.visitChildren(self)


    class BinaryRhsContext(RhsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.RhsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TACParser.OperandContext)
            else:
                return self.getTypedRuleContext(TACParser.OperandContext,i)

        def op(self):
            return self.getTypedRuleContext(TACParser.OpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryRhs" ):
                listener.enterBinaryRhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryRhs" ):
                listener.exitBinaryRhs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryRhs" ):
                return visitor.visitBinaryRhs(self)
            else:
                return visitor.visitChildren(self)


    class NotRhsContext(RhsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.RhsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operand(self):
            return self.getTypedRuleContext(TACParser.OperandContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotRhs" ):
                listener.enterNotRhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotRhs" ):
                listener.exitNotRhs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotRhs" ):
                return visitor.visitNotRhs(self)
            else:
                return visitor.visitChildren(self)


    class CopyRhsContext(RhsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a TACParser.RhsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operand(self):
            return self.getTypedRuleContext(TACParser.OperandContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCopyRhs" ):
                listener.enterCopyRhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCopyRhs" ):
                listener.exitCopyRhs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCopyRhs" ):
                return visitor.visitCopyRhs(self)
            else:
                return visitor.visitChildren(self)



    def rhs(self):

        localctx = TACParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_rhs)
        try:
            self.state = 93
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = TACParser.CallRhsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.match(TACParser.T__6)
                self.state = 81
                self.match(TACParser.ID)
                self.state = 82
                self.match(TACParser.T__1)
                self.state = 83
                self.match(TACParser.INT)
                pass

            elif la_ == 2:
                localctx = TACParser.BinaryRhsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 84
                self.operand()
                self.state = 85
                self.op()
                self.state = 86
                self.operand()
                pass

            elif la_ == 3:
                localctx = TACParser.NegRhsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.match(TACParser.T__7)
                self.state = 89
                self.operand()
                pass

            elif la_ == 4:
                localctx = TACParser.NotRhsContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.match(TACParser.T__8)
                self.state = 91
                self.operand()
                pass

            elif la_ == 5:
                localctx = TACParser.CopyRhsContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 92
                self.operand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return TACParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)




    def op(self):

        localctx = TACParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2096384) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TACParser.ID, 0)

        def INT(self):
            return self.getToken(TACParser.INT, 0)

        def getRuleIndex(self):
            return TACParser.RULE_operand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperand" ):
                listener.enterOperand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperand" ):
                listener.exitOperand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = TACParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operand)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfGotoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(TACParser.OperandContext,0)


        def ID(self):
            return self.getToken(TACParser.ID, 0)

        def getRuleIndex(self):
            return TACParser.RULE_ifGoto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfGoto" ):
                listener.enterIfGoto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfGoto" ):
                listener.exitIfGoto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfGoto" ):
                return visitor.visitIfGoto(self)
            else:
                return visitor.visitChildren(self)




    def ifGoto(self):

        localctx = TACParser.IfGotoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ifGoto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(TACParser.T__20)
            self.state = 100
            self.operand()
            self.state = 101
            self.match(TACParser.T__21)
            self.state = 102
            self.match(TACParser.ID)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 103
                self.match(TACParser.T__5)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GotoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TACParser.ID, 0)

        def getRuleIndex(self):
            return TACParser.RULE_goto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoto" ):
                listener.enterGoto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoto" ):
                listener.exitGoto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoto" ):
                return visitor.visitGoto(self)
            else:
                return visitor.visitChildren(self)




    def goto(self):

        localctx = TACParser.GotoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_goto)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(TACParser.T__21)
            self.state = 107
            self.match(TACParser.ID)
            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 108
                self.match(TACParser.T__5)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def printArg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TACParser.PrintArgContext)
            else:
                return self.getTypedRuleContext(TACParser.PrintArgContext,i)


        def getRuleIndex(self):
            return TACParser.RULE_printStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStat" ):
                listener.enterPrintStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStat" ):
                listener.exitPrintStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStat" ):
                return visitor.visitPrintStat(self)
            else:
                return visitor.visitChildren(self)




    def printStat(self):

        localctx = TACParser.PrintStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_printStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(TACParser.T__22)
            self.state = 112
            self.printArg()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 113
                self.match(TACParser.T__1)
                self.state = 114
                self.printArg()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 120
                self.match(TACParser.T__5)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(TACParser.OperandContext,0)


        def STRING(self):
            return self.getToken(TACParser.STRING, 0)

        def getRuleIndex(self):
            return TACParser.RULE_printArg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintArg" ):
                listener.enterPrintArg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintArg" ):
                listener.exitPrintArg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintArg" ):
                return visitor.visitPrintArg(self)
            else:
                return visitor.visitChildren(self)




    def printArg(self):

        localctx = TACParser.PrintArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_printArg)
        try:
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.operand()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.match(TACParser.STRING)
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


    class ParamStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(TACParser.OperandContext,0)


        def getRuleIndex(self):
            return TACParser.RULE_paramStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamStat" ):
                listener.enterParamStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamStat" ):
                listener.exitParamStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamStat" ):
                return visitor.visitParamStat(self)
            else:
                return visitor.visitChildren(self)




    def paramStat(self):

        localctx = TACParser.ParamStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paramStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(TACParser.T__23)
            self.state = 128
            self.operand()
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 129
                self.match(TACParser.T__5)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(TACParser.OperandContext,0)


        def getRuleIndex(self):
            return TACParser.RULE_returnStat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStat" ):
                listener.enterReturnStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStat" ):
                listener.exitReturnStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStat" ):
                return visitor.visitReturnStat(self)
            else:
                return visitor.visitChildren(self)




    def returnStat(self):

        localctx = TACParser.ReturnStatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_returnStat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(TACParser.T__24)
            self.state = 133
            self.operand()
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 134
                self.match(TACParser.T__5)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





