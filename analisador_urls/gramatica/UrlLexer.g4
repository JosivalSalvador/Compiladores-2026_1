lexer grammar UrlLexer;

// Regra de teste: Reconhece os protocolos permitidos
PROTOCOL: 'http' | 'https' | 'ftp' ;

// Ignora espaços em branco
WS: [ \t\r\n]+ -> skip ;