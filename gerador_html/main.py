import sys

from antlr4 import CommonTokenStream, FileStream, StdinStream

from HtmlLexer import HtmlLexer
from HtmlParser import HtmlParser
from Visitor import Visitor


def main():
    # Lê entrada de arquivo (argumento) ou stdin
    if len(sys.argv) > 1:
        entrada = FileStream(sys.argv[1], encoding='utf-8')
    else:
        entrada = StdinStream()

    # Análise léxica
    lexer  = HtmlLexer(entrada)
    tokens = CommonTokenStream(lexer)

    # Análise sintática
    parser = HtmlParser(tokens)
    arvore = parser.root()

    # Interrompe se houver erros sintáticos
    if parser.getNumberOfSyntaxErrors() > 0:
        sys.exit(1)

    # Geração do HTML via visitor
    visitor = Visitor()
    visitor.visit(arvore)


if __name__ == '__main__':
    main()