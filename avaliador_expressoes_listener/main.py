"""
main.py
Programa principal: instancia léxico, sintático e o avaliador (LISTENER).

Uso:
    python main.py                  # modo interativo
    python main.py "3 + fact 4"    # expressão via argumento
"""

import sys
from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker

from ExpressaoLexer  import ExpressaoLexer
from ExpressaoParser import ExpressaoParser
from avaliador       import AvaliadorExpressoes


def avaliar(expressao: str) -> float:
    # 1. Léxico
    entrada = InputStream(expressao)
    lexer   = ExpressaoLexer(entrada)
    tokens  = CommonTokenStream(lexer)

    # 2. Sintático
    parser = ExpressaoParser(tokens)
    arvore = parser.prog()

    if parser.getNumberOfSyntaxErrors() > 0:
        raise SyntaxError("Expressão com erro sintático.")

    # 3. Avaliador - padrão LISTENER
    avaliador = AvaliadorExpressoes()
    walker    = ParseTreeWalker()
    walker.walk(avaliador, arvore)

    return avaliador.resultado(arvore)


def fmt(v: float) -> str:
    return str(int(v)) if v == int(v) else str(v)


def interativo():
    print("Avaliador de Expressões (LISTENER) – ANTLR4")
    print("Ops: + - * / ^ fact absoluto  |  parênteses")
    print("Digite 'sair' para encerrar.\n")
    while True:
        try:
            linha = input("expr> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if linha.lower() in ("sair", "exit", ""):
            break
        try:
            print(f"  = {fmt(avaliar(linha))}")
        except Exception as e:
            print(f"  [ERRO] {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        expr = " ".join(sys.argv[1:])
        try:
            print(f"{expr} = {fmt(avaliar(expr))}")
        except Exception as e:
            print(f"ERRO: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        interativo()