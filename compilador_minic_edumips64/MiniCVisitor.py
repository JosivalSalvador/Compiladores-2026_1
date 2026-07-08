# Generated from MiniC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniCParser import MiniCParser
else:
    from MiniCParser import MiniCParser

# This class defines a complete generic visitor for a parse tree produced by MiniCParser.

class MiniCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniCParser#program.
    def visitProgram(self, ctx:MiniCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#definition.
    def visitDefinition(self, ctx:MiniCParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#data_definition.
    def visitData_definition(self, ctx:MiniCParser.Data_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#declarator.
    def visitDeclarator(self, ctx:MiniCParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#init_declarator.
    def visitInit_declarator(self, ctx:MiniCParser.Init_declaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#function_definition.
    def visitFunction_definition(self, ctx:MiniCParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#function_header.
    def visitFunction_header(self, ctx:MiniCParser.Function_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#parameter_list.
    def visitParameter_list(self, ctx:MiniCParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#parameter_declaration.
    def visitParameter_declaration(self, ctx:MiniCParser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#function_body.
    def visitFunction_body(self, ctx:MiniCParser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#block.
    def visitBlock(self, ctx:MiniCParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#statement.
    def visitStatement(self, ctx:MiniCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#printf_statement.
    def visitPrintf_statement(self, ctx:MiniCParser.Printf_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#printfArgIdent.
    def visitPrintfArgIdent(self, ctx:MiniCParser.PrintfArgIdentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#printfArgInt.
    def visitPrintfArgInt(self, ctx:MiniCParser.PrintfArgIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#printfArgChar.
    def visitPrintfArgChar(self, ctx:MiniCParser.PrintfArgCharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#assignExpr.
    def visitAssignExpr(self, ctx:MiniCParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#assignAddExpr.
    def visitAssignAddExpr(self, ctx:MiniCParser.AssignAddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#assignSubExpr.
    def visitAssignSubExpr(self, ctx:MiniCParser.AssignSubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#assignMulExpr.
    def visitAssignMulExpr(self, ctx:MiniCParser.AssignMulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#assignDivExpr.
    def visitAssignDivExpr(self, ctx:MiniCParser.AssignDivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#assignModExpr.
    def visitAssignModExpr(self, ctx:MiniCParser.AssignModExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#binaryExpr.
    def visitBinaryExpr(self, ctx:MiniCParser.BinaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#geExpr.
    def visitGeExpr(self, ctx:MiniCParser.GeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#eqExpr.
    def visitEqExpr(self, ctx:MiniCParser.EqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#ltExpr.
    def visitLtExpr(self, ctx:MiniCParser.LtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#unaryExpr.
    def visitUnaryExpr(self, ctx:MiniCParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#gtExpr.
    def visitGtExpr(self, ctx:MiniCParser.GtExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#modExpr.
    def visitModExpr(self, ctx:MiniCParser.ModExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#leExpr.
    def visitLeExpr(self, ctx:MiniCParser.LeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#addExpr.
    def visitAddExpr(self, ctx:MiniCParser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#mulExpr.
    def visitMulExpr(self, ctx:MiniCParser.MulExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#divExpr.
    def visitDivExpr(self, ctx:MiniCParser.DivExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#subExpr.
    def visitSubExpr(self, ctx:MiniCParser.SubExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#neqExpr.
    def visitNeqExpr(self, ctx:MiniCParser.NeqExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#preInc.
    def visitPreInc(self, ctx:MiniCParser.PreIncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#preDec.
    def visitPreDec(self, ctx:MiniCParser.PreDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:MiniCParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#callPrimary.
    def visitCallPrimary(self, ctx:MiniCParser.CallPrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#identPrimary.
    def visitIdentPrimary(self, ctx:MiniCParser.IdentPrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#intPrimary.
    def visitIntPrimary(self, ctx:MiniCParser.IntPrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#charPrimary.
    def visitCharPrimary(self, ctx:MiniCParser.CharPrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#parenPrimary.
    def visitParenPrimary(self, ctx:MiniCParser.ParenPrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniCParser#argument_list.
    def visitArgument_list(self, ctx:MiniCParser.Argument_listContext):
        return self.visitChildren(ctx)



del MiniCParser