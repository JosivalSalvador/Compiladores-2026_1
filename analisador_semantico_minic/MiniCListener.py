# Generated from MiniC.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .MiniCParser import MiniCParser
else:
    from MiniCParser import MiniCParser

# This class defines a complete listener for a parse tree produced by MiniCParser.
class MiniCListener(ParseTreeListener):

    # Enter a parse tree produced by MiniCParser#program.
    def enterProgram(self, ctx:MiniCParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniCParser#program.
    def exitProgram(self, ctx:MiniCParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniCParser#definition.
    def enterDefinition(self, ctx:MiniCParser.DefinitionContext):
        pass

    # Exit a parse tree produced by MiniCParser#definition.
    def exitDefinition(self, ctx:MiniCParser.DefinitionContext):
        pass


    # Enter a parse tree produced by MiniCParser#data_definition.
    def enterData_definition(self, ctx:MiniCParser.Data_definitionContext):
        pass

    # Exit a parse tree produced by MiniCParser#data_definition.
    def exitData_definition(self, ctx:MiniCParser.Data_definitionContext):
        pass


    # Enter a parse tree produced by MiniCParser#declarator.
    def enterDeclarator(self, ctx:MiniCParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by MiniCParser#declarator.
    def exitDeclarator(self, ctx:MiniCParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by MiniCParser#function_definition.
    def enterFunction_definition(self, ctx:MiniCParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by MiniCParser#function_definition.
    def exitFunction_definition(self, ctx:MiniCParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by MiniCParser#function_header.
    def enterFunction_header(self, ctx:MiniCParser.Function_headerContext):
        pass

    # Exit a parse tree produced by MiniCParser#function_header.
    def exitFunction_header(self, ctx:MiniCParser.Function_headerContext):
        pass


    # Enter a parse tree produced by MiniCParser#parameter_list.
    def enterParameter_list(self, ctx:MiniCParser.Parameter_listContext):
        pass

    # Exit a parse tree produced by MiniCParser#parameter_list.
    def exitParameter_list(self, ctx:MiniCParser.Parameter_listContext):
        pass


    # Enter a parse tree produced by MiniCParser#parameter_declaration.
    def enterParameter_declaration(self, ctx:MiniCParser.Parameter_declarationContext):
        pass

    # Exit a parse tree produced by MiniCParser#parameter_declaration.
    def exitParameter_declaration(self, ctx:MiniCParser.Parameter_declarationContext):
        pass


    # Enter a parse tree produced by MiniCParser#function_body.
    def enterFunction_body(self, ctx:MiniCParser.Function_bodyContext):
        pass

    # Exit a parse tree produced by MiniCParser#function_body.
    def exitFunction_body(self, ctx:MiniCParser.Function_bodyContext):
        pass


    # Enter a parse tree produced by MiniCParser#block.
    def enterBlock(self, ctx:MiniCParser.BlockContext):
        pass

    # Exit a parse tree produced by MiniCParser#block.
    def exitBlock(self, ctx:MiniCParser.BlockContext):
        pass


    # Enter a parse tree produced by MiniCParser#statement.
    def enterStatement(self, ctx:MiniCParser.StatementContext):
        pass

    # Exit a parse tree produced by MiniCParser#statement.
    def exitStatement(self, ctx:MiniCParser.StatementContext):
        pass


    # Enter a parse tree produced by MiniCParser#expression.
    def enterExpression(self, ctx:MiniCParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MiniCParser#expression.
    def exitExpression(self, ctx:MiniCParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MiniCParser#geExpr.
    def enterGeExpr(self, ctx:MiniCParser.GeExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#geExpr.
    def exitGeExpr(self, ctx:MiniCParser.GeExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#gtExpr.
    def enterGtExpr(self, ctx:MiniCParser.GtExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#gtExpr.
    def exitGtExpr(self, ctx:MiniCParser.GtExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#modExpr.
    def enterModExpr(self, ctx:MiniCParser.ModExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#modExpr.
    def exitModExpr(self, ctx:MiniCParser.ModExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#assignSubExpr.
    def enterAssignSubExpr(self, ctx:MiniCParser.AssignSubExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#assignSubExpr.
    def exitAssignSubExpr(self, ctx:MiniCParser.AssignSubExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#assignModExpr.
    def enterAssignModExpr(self, ctx:MiniCParser.AssignModExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#assignModExpr.
    def exitAssignModExpr(self, ctx:MiniCParser.AssignModExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#subExpr.
    def enterSubExpr(self, ctx:MiniCParser.SubExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#subExpr.
    def exitSubExpr(self, ctx:MiniCParser.SubExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#neqExpr.
    def enterNeqExpr(self, ctx:MiniCParser.NeqExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#neqExpr.
    def exitNeqExpr(self, ctx:MiniCParser.NeqExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#eqExpr.
    def enterEqExpr(self, ctx:MiniCParser.EqExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#eqExpr.
    def exitEqExpr(self, ctx:MiniCParser.EqExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#ltExpr.
    def enterLtExpr(self, ctx:MiniCParser.LtExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#ltExpr.
    def exitLtExpr(self, ctx:MiniCParser.LtExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#assignAddExpr.
    def enterAssignAddExpr(self, ctx:MiniCParser.AssignAddExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#assignAddExpr.
    def exitAssignAddExpr(self, ctx:MiniCParser.AssignAddExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#unaryExpr.
    def enterUnaryExpr(self, ctx:MiniCParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#unaryExpr.
    def exitUnaryExpr(self, ctx:MiniCParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#leExpr.
    def enterLeExpr(self, ctx:MiniCParser.LeExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#leExpr.
    def exitLeExpr(self, ctx:MiniCParser.LeExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#addExpr.
    def enterAddExpr(self, ctx:MiniCParser.AddExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#addExpr.
    def exitAddExpr(self, ctx:MiniCParser.AddExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#assignMulExpr.
    def enterAssignMulExpr(self, ctx:MiniCParser.AssignMulExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#assignMulExpr.
    def exitAssignMulExpr(self, ctx:MiniCParser.AssignMulExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#mulExpr.
    def enterMulExpr(self, ctx:MiniCParser.MulExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#mulExpr.
    def exitMulExpr(self, ctx:MiniCParser.MulExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#divExpr.
    def enterDivExpr(self, ctx:MiniCParser.DivExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#divExpr.
    def exitDivExpr(self, ctx:MiniCParser.DivExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#assignDivExpr.
    def enterAssignDivExpr(self, ctx:MiniCParser.AssignDivExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#assignDivExpr.
    def exitAssignDivExpr(self, ctx:MiniCParser.AssignDivExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#assignExpr.
    def enterAssignExpr(self, ctx:MiniCParser.AssignExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#assignExpr.
    def exitAssignExpr(self, ctx:MiniCParser.AssignExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#preInc.
    def enterPreInc(self, ctx:MiniCParser.PreIncContext):
        pass

    # Exit a parse tree produced by MiniCParser#preInc.
    def exitPreInc(self, ctx:MiniCParser.PreIncContext):
        pass


    # Enter a parse tree produced by MiniCParser#preDec.
    def enterPreDec(self, ctx:MiniCParser.PreDecContext):
        pass

    # Exit a parse tree produced by MiniCParser#preDec.
    def exitPreDec(self, ctx:MiniCParser.PreDecContext):
        pass


    # Enter a parse tree produced by MiniCParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:MiniCParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by MiniCParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:MiniCParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by MiniCParser#callPrimary.
    def enterCallPrimary(self, ctx:MiniCParser.CallPrimaryContext):
        pass

    # Exit a parse tree produced by MiniCParser#callPrimary.
    def exitCallPrimary(self, ctx:MiniCParser.CallPrimaryContext):
        pass


    # Enter a parse tree produced by MiniCParser#identPrimary.
    def enterIdentPrimary(self, ctx:MiniCParser.IdentPrimaryContext):
        pass

    # Exit a parse tree produced by MiniCParser#identPrimary.
    def exitIdentPrimary(self, ctx:MiniCParser.IdentPrimaryContext):
        pass


    # Enter a parse tree produced by MiniCParser#intPrimary.
    def enterIntPrimary(self, ctx:MiniCParser.IntPrimaryContext):
        pass

    # Exit a parse tree produced by MiniCParser#intPrimary.
    def exitIntPrimary(self, ctx:MiniCParser.IntPrimaryContext):
        pass


    # Enter a parse tree produced by MiniCParser#charPrimary.
    def enterCharPrimary(self, ctx:MiniCParser.CharPrimaryContext):
        pass

    # Exit a parse tree produced by MiniCParser#charPrimary.
    def exitCharPrimary(self, ctx:MiniCParser.CharPrimaryContext):
        pass


    # Enter a parse tree produced by MiniCParser#parenPrimary.
    def enterParenPrimary(self, ctx:MiniCParser.ParenPrimaryContext):
        pass

    # Exit a parse tree produced by MiniCParser#parenPrimary.
    def exitParenPrimary(self, ctx:MiniCParser.ParenPrimaryContext):
        pass


    # Enter a parse tree produced by MiniCParser#argument_list.
    def enterArgument_list(self, ctx:MiniCParser.Argument_listContext):
        pass

    # Exit a parse tree produced by MiniCParser#argument_list.
    def exitArgument_list(self, ctx:MiniCParser.Argument_listContext):
        pass



del MiniCParser