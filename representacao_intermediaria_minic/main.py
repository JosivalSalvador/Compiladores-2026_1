import sys
import os
from antlr4 import CommonTokenStream, FileStream

from MiniCLexer                   import MiniCLexer
from MiniCParser                  import MiniCParser
from analisador_semantico         import analisar
from MiniCThreeAddressCodeVisitor import MiniCThreeAddressCodeVisitor

if len(sys.argv) < 2:
    print("Uso: python main.py <arquivo.c>")
    sys.exit(1)

caminho = sys.argv[1]

# análise léxica
try:
    entrada = FileStream(caminho, encoding='utf-8')
except FileNotFoundError:
    print(f"Erro: arquivo '{caminho}' não encontrado.")
    sys.exit(1)

lexer  = MiniCLexer(entrada)
tokens = CommonTokenStream(lexer)

# análise sintática
parser = MiniCParser(tokens)
tree   = parser.program()

print(f"Arquivo: {caminho}")

if parser.getNumberOfSyntaxErrors() > 0:
    print(f"Análise sintática: {parser.getNumberOfSyntaxErrors()} erro(s) — geração cancelada.")
    sys.exit(1)

print("Análise sintática: OK")

# análise semântica — só continua se não houver erros
erros = analisar(tree, parser)

if erros:
    print("Geração de código intermediário cancelada (erros semânticos).")
    sys.exit(1)

# geração do código de três endereços
visitor = MiniCThreeAddressCodeVisitor()
visitor.visit(tree)

base          = os.path.splitext(caminho)[0]
caminho_saida = base + '.tac'

with open(caminho_saida, 'w', encoding='utf-8') as f:
    f.write(visitor.get_code())
    f.write('\n')

print(f"Código intermediário gerado em: {caminho_saida}")