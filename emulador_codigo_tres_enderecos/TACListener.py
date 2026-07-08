# Generated from TAC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TACParser import TACParser
else:
    from TACParser import TACParser

# This class defines a complete listener for a parse tree produced by TACParser.
class TACListener(ParseTreeListener):

    # Enter a parse tree produced by TACParser#prog.
    def enterProg(self, ctx:TACParser.ProgContext):
        pass

    # Exit a parse tree produced by TACParser#prog.
    def exitProg(self, ctx:TACParser.ProgContext):
        pass


    # Enter a parse tree produced by TACParser#item.
    def enterItem(self, ctx:TACParser.ItemContext):
        pass

    # Exit a parse tree produced by TACParser#item.
    def exitItem(self, ctx:TACParser.ItemContext):
        pass


    # Enter a parse tree produced by TACParser#funcDef.
    def enterFuncDef(self, ctx:TACParser.FuncDefContext):
        pass

    # Exit a parse tree produced by TACParser#funcDef.
    def exitFuncDef(self, ctx:TACParser.FuncDefContext):
        pass


    # Enter a parse tree produced by TACParser#instr.
    def enterInstr(self, ctx:TACParser.InstrContext):
        pass

    # Exit a parse tree produced by TACParser#instr.
    def exitInstr(self, ctx:TACParser.InstrContext):
        pass


    # Enter a parse tree produced by TACParser#label.
    def enterLabel(self, ctx:TACParser.LabelContext):
        pass

    # Exit a parse tree produced by TACParser#label.
    def exitLabel(self, ctx:TACParser.LabelContext):
        pass


    # Enter a parse tree produced by TACParser#stmt.
    def enterStmt(self, ctx:TACParser.StmtContext):
        pass

    # Exit a parse tree produced by TACParser#stmt.
    def exitStmt(self, ctx:TACParser.StmtContext):
        pass


    # Enter a parse tree produced by TACParser#assign.
    def enterAssign(self, ctx:TACParser.AssignContext):
        pass

    # Exit a parse tree produced by TACParser#assign.
    def exitAssign(self, ctx:TACParser.AssignContext):
        pass


    # Enter a parse tree produced by TACParser#callRhs.
    def enterCallRhs(self, ctx:TACParser.CallRhsContext):
        pass

    # Exit a parse tree produced by TACParser#callRhs.
    def exitCallRhs(self, ctx:TACParser.CallRhsContext):
        pass


    # Enter a parse tree produced by TACParser#binaryRhs.
    def enterBinaryRhs(self, ctx:TACParser.BinaryRhsContext):
        pass

    # Exit a parse tree produced by TACParser#binaryRhs.
    def exitBinaryRhs(self, ctx:TACParser.BinaryRhsContext):
        pass


    # Enter a parse tree produced by TACParser#negRhs.
    def enterNegRhs(self, ctx:TACParser.NegRhsContext):
        pass

    # Exit a parse tree produced by TACParser#negRhs.
    def exitNegRhs(self, ctx:TACParser.NegRhsContext):
        pass


    # Enter a parse tree produced by TACParser#notRhs.
    def enterNotRhs(self, ctx:TACParser.NotRhsContext):
        pass

    # Exit a parse tree produced by TACParser#notRhs.
    def exitNotRhs(self, ctx:TACParser.NotRhsContext):
        pass


    # Enter a parse tree produced by TACParser#copyRhs.
    def enterCopyRhs(self, ctx:TACParser.CopyRhsContext):
        pass

    # Exit a parse tree produced by TACParser#copyRhs.
    def exitCopyRhs(self, ctx:TACParser.CopyRhsContext):
        pass


    # Enter a parse tree produced by TACParser#op.
    def enterOp(self, ctx:TACParser.OpContext):
        pass

    # Exit a parse tree produced by TACParser#op.
    def exitOp(self, ctx:TACParser.OpContext):
        pass


    # Enter a parse tree produced by TACParser#operand.
    def enterOperand(self, ctx:TACParser.OperandContext):
        pass

    # Exit a parse tree produced by TACParser#operand.
    def exitOperand(self, ctx:TACParser.OperandContext):
        pass


    # Enter a parse tree produced by TACParser#ifGoto.
    def enterIfGoto(self, ctx:TACParser.IfGotoContext):
        pass

    # Exit a parse tree produced by TACParser#ifGoto.
    def exitIfGoto(self, ctx:TACParser.IfGotoContext):
        pass


    # Enter a parse tree produced by TACParser#goto.
    def enterGoto(self, ctx:TACParser.GotoContext):
        pass

    # Exit a parse tree produced by TACParser#goto.
    def exitGoto(self, ctx:TACParser.GotoContext):
        pass


    # Enter a parse tree produced by TACParser#printStat.
    def enterPrintStat(self, ctx:TACParser.PrintStatContext):
        pass

    # Exit a parse tree produced by TACParser#printStat.
    def exitPrintStat(self, ctx:TACParser.PrintStatContext):
        pass


    # Enter a parse tree produced by TACParser#printArg.
    def enterPrintArg(self, ctx:TACParser.PrintArgContext):
        pass

    # Exit a parse tree produced by TACParser#printArg.
    def exitPrintArg(self, ctx:TACParser.PrintArgContext):
        pass


    # Enter a parse tree produced by TACParser#paramStat.
    def enterParamStat(self, ctx:TACParser.ParamStatContext):
        pass

    # Exit a parse tree produced by TACParser#paramStat.
    def exitParamStat(self, ctx:TACParser.ParamStatContext):
        pass


    # Enter a parse tree produced by TACParser#returnStat.
    def enterReturnStat(self, ctx:TACParser.ReturnStatContext):
        pass

    # Exit a parse tree produced by TACParser#returnStat.
    def exitReturnStat(self, ctx:TACParser.ReturnStatContext):
        pass



del TACParser