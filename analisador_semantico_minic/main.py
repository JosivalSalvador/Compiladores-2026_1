"""
main.py
Programa principal do analisador semântico MiniC.
Instancia léxico, parser e chama o analisador semântico.

Uso:
    python main.py arquivo.c
"""

import sys
from antlr4 import CommonTokenStream, FileStream

from MiniCLexer              import MiniCLexer
from MiniCParser             import MiniCParser
from analisador_semantico    import analisar


def main():
    # Verifica se o arquivo fonte foi passado como argumento
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo.c>")
        sys.exit(1)

    caminho = sys.argv[1]

    # -------------------------------------------------------------------------
    # 1) Análise léxica
    # Lê o arquivo fonte e transforma em fluxo de tokens
    # -------------------------------------------------------------------------
    try:
        entrada = FileStream(caminho, encoding='utf-8')
    except FileNotFoundError:
        print(f"Erro: arquivo '{caminho}' não encontrado.")
        sys.exit(1)

    lexer  = MiniCLexer(entrada)
    tokens = CommonTokenStream(lexer)

    # -------------------------------------------------------------------------
    # 2) Análise sintática
    # Constrói a árvore sintática a partir dos tokens
    # -------------------------------------------------------------------------
    parser = MiniCParser(tokens)
    tree   = parser.program()

    # Se houver erros sintáticos, não faz sentido continuar com a semântica
    if parser.getNumberOfSyntaxErrors() > 0:
        print(f"\nAnálise sintática: {parser.getNumberOfSyntaxErrors()} erro(s) encontrado(s).")
        print("Corrija os erros sintáticos antes de prosseguir.")
        sys.exit(1)

    print(f"Arquivo: {caminho}")
    print("Análise sintática: OK")

    # -------------------------------------------------------------------------
    # 3) Análise semântica
    # Roda o visitor semântico e imprime todos os erros encontrados no final
    # -------------------------------------------------------------------------
    erros = analisar(tree, parser)

    # Sai com código de erro se houver problemas semânticos
    sys.exit(1 if erros else 0)


if __name__ == '__main__':
    main()