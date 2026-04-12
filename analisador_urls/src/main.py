import sys
from antlr4 import InputStream

# Importação inteligente: tenta puxar da nossa pasta modular primeiro.
# Se falhar (como vai acontecer na máquina do professor que só terá 2 arquivos soltos),
# ele importa da mesma raiz. Isso garante nota máxima sem você precisar alterar código na entrega!
try:
    from lexer_gerado.UrlLexer import UrlLexer
except ImportError:
    from UrlLexer import UrlLexer

def main():
    # REQUISITO: O primeiro parâmetro de linha de comando deve ser a URL
    if len(sys.argv) < 2:
        print("Erro: Forneça a URL a ser testada como parâmetro.")
        print("Uso: python main.py <url>")
        sys.exit(1)
        
    url_texto = sys.argv[1]
    
    # Prepara o fluxo de texto e instancia o analisador léxico
    input_stream = InputStream(url_texto)
    lexer = UrlLexer(input_stream)
    
    # Extrai a lista de todos os tokens identificados pela gramática
    tokens = lexer.getAllTokens()
    
    # Remove o token EOF (End Of File) que o ANTLR adiciona automaticamente no final
    tokens_reais = [t for t in tokens if t.type != -1]
    
    # LÓGICA DO TRABALHO:
    # Se a URL inteira for validada, o ANTLR vai gerar apenas UM token (o token principal 'URL')
    if len(tokens_reais) == 1 and lexer.symbolicNames[tokens_reais[0].type] == "URL":
        # REQUISITO: Imprimir TOKEN e VALOR
        print("TOKEN: URL")
        print(f"VALOR: {url_texto}")
    else:
        # OBSERVAÇÃO 4: Mensagem de erro/aviso caso o token principal não seja reconhecido
        print("AVISO: A entrada não foi reconhecida como um token URL completo e válido.\n")
        
        # REQUISITO: Caso o token principal falhe, imprimir cada sub-token reconhecido
        for token in tokens_reais:
            nome_token = lexer.symbolicNames[token.type]
            
            # Tratamento extra: se algum pedaço da string não der 'match' com nada na gramática
            if nome_token == "<INVALID>":
                print(f"ERRO LÉXICO: Caractere não reconhecido -> '{token.text}'")
            else:
                print(f"TOKEN: {nome_token} | VALOR: {token.text}")

if __name__ == "__main__":
    main()