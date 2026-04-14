from antlr4 import InputStream, Token
from Tutorial import Tutorial

input_stream = InputStream(input('? '))
lexer = Tutorial(input_stream)
token = lexer.nextToken()

while token.type != Token.EOF:
    print(f"Tipo de token: {lexer.symbolicNames[token.type]}, Valor: {token.text}")
    token = lexer.nextToken()