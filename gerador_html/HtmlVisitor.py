# Generated from Html.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HtmlParser import HtmlParser
else:
    from HtmlParser import HtmlParser

# This class defines a complete generic visitor for a parse tree produced by HtmlParser.

class HtmlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HtmlParser#root.
    def visitRoot(self, ctx:HtmlParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HtmlParser#questao.
    def visitQuestao(self, ctx:HtmlParser.QuestaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HtmlParser#qTexto.
    def visitQTexto(self, ctx:HtmlParser.QTextoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HtmlParser#qRadioBox.
    def visitQRadioBox(self, ctx:HtmlParser.QRadioBoxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HtmlParser#qCheckBox.
    def visitQCheckBox(self, ctx:HtmlParser.QCheckBoxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HtmlParser#qMenu.
    def visitQMenu(self, ctx:HtmlParser.QMenuContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HtmlParser#qBotao.
    def visitQBotao(self, ctx:HtmlParser.QBotaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HtmlParser#qTabela.
    def visitQTabela(self, ctx:HtmlParser.QTabelaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HtmlParser#opcoes.
    def visitOpcoes(self, ctx:HtmlParser.OpcoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HtmlParser#menuOpcoes.
    def visitMenuOpcoes(self, ctx:HtmlParser.MenuOpcoesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HtmlParser#menuOpcao.
    def visitMenuOpcao(self, ctx:HtmlParser.MenuOpcaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HtmlParser#linhaCabecalho.
    def visitLinhaCabecalho(self, ctx:HtmlParser.LinhaCabecalhoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HtmlParser#linhaDados.
    def visitLinhaDados(self, ctx:HtmlParser.LinhaDadosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HtmlParser#linha.
    def visitLinha(self, ctx:HtmlParser.LinhaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HtmlParser#str_.
    def visitStr_(self, ctx:HtmlParser.Str_Context):
        return self.visitChildren(ctx)



del HtmlParser