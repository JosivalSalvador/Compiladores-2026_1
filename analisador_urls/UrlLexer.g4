lexer grammar UrlLexer;

// Protocolos solicitados no trabalho
PROTOCOL : 'http' | 'https' | 'ftp' ;

// Separador entre o protocolo e o domínio
SEPARADOR : '://' ;

// Token principal que forma a URL.
// Apenas o domínio é obrigatório, o resto usa o '?' indicando que é opcional conforme o PDF.
URL : (PROTOCOL SEPARADOR)? DOMAIN PORT? PATH? QUERY? FRAGMENTO? ;

// Domínio do host ou IP (aceita letras, números, hifens e pontos)
DOMAIN : [a-zA-Z0-9.-]+ ;

// Porta da conexão (opcional, começa com : e tem apenas números)
PORT : ':' [0-9]+ ;

// Caminho no servidor (opcional, começa com /)
PATH : '/' [a-zA-Z0-9./_-]* ;

// Parâmetros de consulta (opcional, começa com ? e tem formato chave=valor)
QUERY : '?' [a-zA-Z0-9=&_-]+ ;

// Fragmento para âncora (opcional, começa com #)
// Nomeado como FRAGMENTO em PT-BR pra não conflitar com a palavra 'fragment' da linguagem
FRAGMENTO : '#' [a-zA-Z0-9_-]+ ;

// Ignora espaços em branco e quebras de linha soltas
WS : [ \t\r\n]+ -> skip ;