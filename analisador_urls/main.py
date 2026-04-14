import sys
from antlr4 import InputStream, Token
from antlr4.error.ErrorListener import ErrorListener
from UrlLexer import UrlLexer

# Classe para silenciar os erros padrão do ANTLR
class SilenciadorDeErros(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        pass

# Verifica se a pessoa passou a URL pelo terminal na hora de rodar
if len(sys.argv) < 2:
    print("Erro: Faltou passar a URL! Exemplo: python main.py 'http://site.com'")
    sys.exit(1)

# Pega o primeiro argumento depois do nome do script (a própria URL)
url_entrada = sys.argv[1]

# Prepara a entrada pro ANTLR engolir
input_stream = InputStream(url_entrada)
lexer = UrlLexer(input_stream)

# Remove os erros em inglês do ANTLR e coloca o silenciador
lexer.removeErrorListeners()
lexer.addErrorListener(SilenciadorDeErros())

# Vamos guardar todos os tokens gerados numa lista pra analisar
tokens_encontrados = []
token = lexer.nextToken()

while token.type != Token.EOF:
    tokens_encontrados.append(token)
    token = lexer.nextToken()

# Lógica principal: se a lista só tem 1 token e ele é do tipo 'URL',
# quer dizer que a regra principal conseguiu abraçar a string inteira!
if len(tokens_encontrados) == 1 and lexer.symbolicNames[tokens_encontrados[0].type] == 'URL':
    print(f"TOKEN: {lexer.symbolicNames[tokens_encontrados[0].type]}")
    print(f"VALOR: {tokens_encontrados[0].text}")

else:
    # Bônus (Regra 4): Aviso se o token principal não engoliu a URL inteira
    print("AVISO: A entrada não formou uma URL completa válida.")
    print("Imprimindo os sub-tokens reconhecidos:")
    
    # Imprime os pedacinhos que ele conseguiu entender (Regra do PDF)
    for t in tokens_encontrados:
        nome_token = lexer.symbolicNames[t.type]
        print(f"Tipo de token: {nome_token}, Valor: {t.text}")