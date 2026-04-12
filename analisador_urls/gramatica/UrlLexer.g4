lexer grammar UrlLexer;

// =========================================================================
// 1. TOKEN PRINCIPAL (Deve ser o primeiro para ter prioridade máxima)
// Regra: Composto pelos tokens secundários. Protocolo, porta, caminho, 
// query e fragmento são opcionais (marcados com '?').
// =========================================================================
URL: PROTOCOLO? DOMINIO PORTA? CAMINHO? QUERY? FRAGMENTO? ;


// =========================================================================
// 2. SUB-TOKENS (Tokens secundários)
// Regra: Usar expressões regulares para identificar cada item.
// =========================================================================

// Protocolo: Considerar somente http, https e ftp (inclui o separador ://)
PROTOCOLO: ('http' | 'https' | 'ftp') '://' ;

// Domínio: Nome do host ou IP. Inicia com alfanumérico, seguido de 
// alfanuméricos, pontos ou hifens. (Ex: www.example.com, secure.example.com)
DOMINIO: [a-zA-Z0-9] [a-zA-Z0-9.-]* ;

// Porta: Número da porta, iniciado com ':' (Ex: :80, :443)
PORTA: ':' [0-9]+ ;

// Caminho: Começa com '/' e pode conter caracteres alfanuméricos e 
// símbolos comuns de diretório (Ex: /path/to/file, /downloads/file.zip)
CAMINHO: ('/' [a-zA-Z0-9_.~%-]*)+ ;

// Query: Começa com '?' e contém o formato chave=valor separado por '&'
// (Ex: ?search=query&sort=ascending)
QUERY: '?' [a-zA-Z0-9_=&.~%-]+ ;

// Fragmento: Começa com '#' e indica uma âncora (Ex: #section2, #signup)
FRAGMENTO: '#' [a-zA-Z0-9_.~%-]+ ;


// =========================================================================
// 3. REGRAS DE IGNORAR (Boa prática em compiladores)
// =========================================================================

// Ignorar espaços em branco, tabulações e quebras de linha na entrada.
WS: [ \t\r\n]+ -> skip ;