import sys
from antlr4 import InputStream

# Importa a classe do analisador léxico que o Java gerou para nós
from lexer_gerado.UrlLexer import UrlLexer

def main():
    # Verifica se a URL foi passada na linha de comando
    if len(sys.argv) < 2:
        print("Erro: Forneça a URL a ser testada como parâmetro.")
        print('Uso: uv run task run-url "http://sua-url.com"')
        sys.exit(1)
        
    url_texto = sys.argv[1]
    
    # Prepara o fluxo de texto para o ANTLR processar
    input_stream = InputStream(url_texto)
    lexer = UrlLexer(input_stream)
    
    # Extrai todos os tokens identificados pela gramática
    tokens = lexer.getAllTokens()
    
    # O ANTLR sempre adiciona um token EOF (End Of File) no final da lista.
    # Vamos filtrá-lo para trabalhar apenas com os tokens reais.
    tokens_reais = [t for t in tokens if t.type != -1]
    
    # Verifica se o lexer conseguiu agrupar tudo em um ÚNICO token do tipo URL
    # lexer.symbolicNames mapeia o ID numérico do token para o nome dele na gramática (ex: "URL")
    if len(tokens_reais) == 1 and lexer.symbolicNames[tokens_reais[0].type] == "URL":
        print("TOKEN: URL")
        print(f"VALOR: {tokens_reais[0].text}")
    else:
        # Ponto extra do PDF (Observação 4): Aviso de que o token principal falhou
        print("AVISO: A entrada não foi reconhecida como uma URL válida completa.")
        print("Listando sub-tokens reconhecidos:\n")
        
        for token in tokens_reais:
            nome_token = lexer.symbolicNames[token.type]
            # Se for um pedaço de texto que não casou com nenhuma regra, o ANTLR joga erro léxico
            # e o nome do token pode vir vazio ou desconhecido. Tratamos isso por segurança.
            if nome_token == "<INVALID>":
                print(f"ERRO LÉXICO: Caractere(s) não reconhecido(s): '{token.text}'")
            else:
                print(f"TOKEN: {nome_token} | VALOR: {token.text}")

if __name__ == "__main__":
    main()