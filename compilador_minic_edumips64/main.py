# Autor: Josival Salvador Monteiro Júnior
# Trabalho 09 - Geração de Código Assembly do EduMIPS64
#
# Script integrador: recebe um arquivo-fonte MiniC (.c) e executa, em ordem,
#   1) analise lexica + sintatica (ANTLR, a partir de MiniC.g4)
#   2) analise semantica          (semantic_analyzer.py)
#   3) geracao do codigo de tres enderecos (TAC)  (tac_generator.py)
#   4) geracao do Assembly EduMIPS64              (mips_generator.py)
#
# So chega a gerar TAC/Assembly se as fases 1 e 2 nao acusarem nenhum erro
# (objetivo geral do trabalho). Erros de qualquer fase sao impressos e o
# script encerra com codigo de saida 1.
#
# Uso:
#   python main.py programa.c   -> gera e imprime TAC + Assembly

import sys
from antlr4 import FileStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from MiniCLexer import MiniCLexer
from MiniCParser import MiniCParser

from semantic_analyzer import SemanticAnalyzer
from tac_generator import TACGenerator
from mips_generator import MipsGenerator


class CollectingErrorListener(ErrorListener):
    """Em vez do comportamento padrao do ANTLR (so imprime no console e
    continua tentando parsear), acumula os erros lexicos/sintaticos numa
    lista -- mesmo formato de retorno que o SemanticAnalyzer ja usa."""

    def __init__(self, fase):
        super().__init__()
        self.fase = fase
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"[linha {line}:{column}] Erro {self.fase}: {msg}")


def parar_com_erros(titulo, erros):
    print(f"\n=== {titulo} ===")
    for e in erros:
        print(e)
    print(f"\nTotal: {len(erros)} erro(s). Nenhum codigo foi gerado.")
    sys.exit(1)


def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py <arquivo.c>")
        sys.exit(1)

    caminho_fonte = sys.argv[1]

    # ---------- 1) lexico + sintatico ----------

    input_stream = FileStream(caminho_fonte, encoding='utf-8')
    lexer = MiniCLexer(input_stream)
    lexer.removeErrorListeners()
    lex_listener = CollectingErrorListener('lexico')
    lexer.addErrorListener(lex_listener)

    token_stream = CommonTokenStream(lexer)
    parser = MiniCParser(token_stream)
    parser.removeErrorListeners()
    syn_listener = CollectingErrorListener('sintatico')
    parser.addErrorListener(syn_listener)

    tree = parser.program()

    if lex_listener.errors:
        parar_com_erros("ERROS LEXICOS", lex_listener.errors)
    if syn_listener.errors:
        parar_com_erros("ERROS SINTATICOS", syn_listener.errors)

    print("Lexico e sintatico: OK")

    # ---------- 2) semantico ----------

    semantic = SemanticAnalyzer()
    erros_semanticos = semantic.analyze(tree)

    if erros_semanticos:
        parar_com_erros("ERROS SEMANTICOS", erros_semanticos)

    print("Semantico: OK")

    # ---------- 3) geracao do TAC ----------

    tac_gen = TACGenerator(semantic.global_vars, semantic.functions, semantic.function_locals)
    tac_texto = tac_gen.generate(tree)

    print("\n=== CODIGO DE TRES ENDERECOS (TAC) ===\n")
    print(tac_texto)

    # ---------- 4) geracao do Assembly EduMIPS64 ----------

    mips_gen = MipsGenerator(semantic.global_vars.keys())
    asm_texto = mips_gen.generate(tac_texto)

    print("\n=== ASSEMBLY EduMIPS64 ===\n")
    print(asm_texto)


if __name__ == '__main__':
    main()