import sys
from antlr4 import FileStream, CommonTokenStream
from TACLexer import TACLexer
from TACParser import TACParser
from TACInterpreterVisitor import TACInterpreterVisitor

# Carregar a entrada do terminal
input_stream = FileStream(sys.argv[1])
# Criar um lexer
lexer = TACLexer(input_stream)
# Criar um fluxo de tokens a partir do lexer
token_stream = CommonTokenStream(lexer)
# Criar um parser com o fluxo de tokens
parser = TACParser(token_stream)
# Chamar o metodo inicial do parser
tree = parser.prog()
# Chamar o visitor passando a Arvore de Parser como parametro, e executar o codigo
visitor = TACInterpreterVisitor()

try:
    visitor.visit(tree)
except RuntimeError as e:
    print(f"Erro de execucao: {e}")
    sys.exit(1)