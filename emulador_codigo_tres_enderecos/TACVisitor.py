# Generated from TAC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .TACParser import TACParser
else:
    from TACParser import TACParser

# This class defines a complete generic visitor for a parse tree produced by TACParser.

class TACVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TACParser#prog.
    def visitProg(self, ctx:TACParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#item.
    def visitItem(self, ctx:TACParser.ItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#funcDef.
    def visitFuncDef(self, ctx:TACParser.FuncDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#instr.
    def visitInstr(self, ctx:TACParser.InstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#label.
    def visitLabel(self, ctx:TACParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#stmt.
    def visitStmt(self, ctx:TACParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#assign.
    def visitAssign(self, ctx:TACParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#callRhs.
    def visitCallRhs(self, ctx:TACParser.CallRhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#binaryRhs.
    def visitBinaryRhs(self, ctx:TACParser.BinaryRhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#negRhs.
    def visitNegRhs(self, ctx:TACParser.NegRhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#notRhs.
    def visitNotRhs(self, ctx:TACParser.NotRhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#copyRhs.
    def visitCopyRhs(self, ctx:TACParser.CopyRhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#op.
    def visitOp(self, ctx:TACParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#operand.
    def visitOperand(self, ctx:TACParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#ifGoto.
    def visitIfGoto(self, ctx:TACParser.IfGotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#goto.
    def visitGoto(self, ctx:TACParser.GotoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#printStat.
    def visitPrintStat(self, ctx:TACParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#printArg.
    def visitPrintArg(self, ctx:TACParser.PrintArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#paramStat.
    def visitParamStat(self, ctx:TACParser.ParamStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TACParser#returnStat.
    def visitReturnStat(self, ctx:TACParser.ReturnStatContext):
        return self.visitChildren(ctx)



del TACParser