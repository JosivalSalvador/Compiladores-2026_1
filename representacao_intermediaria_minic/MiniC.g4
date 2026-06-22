grammar MiniC;

// =============================================================================
// REGRAS DO PARSER (análise sintática)
// =============================================================================

// Ponto de entrada: um programa tem uma ou mais definições
program
    : definition+ EOF
    ;

// Uma definição é uma variável global ou uma função
definition
    : data_definition
    | function_definition
    ;

// Declaração de variáveis: aceita int OU char como tipo
// ex: int x, y;   char c;
// ALTERAÇÃO (item 1): o tipo passou de apenas INT para (INT | CHAR),
// permitindo declarar variáveis do tipo char além de int
data_definition
    : (INT | CHAR) declarator (',' declarator)* ';'
    ;

// Um declarador é simplesmente um identificador
declarator
    : IDENTIFIER
    ;

// Definição de função: tipo de retorno int é opcional (funções sem retorno omitem)
// ex: int soma(...) { ... }   ou   semRetorno() { ... }
function_definition
    : INT? function_header function_body
    ;

// Cabeçalho da função: nome seguido da lista de parâmetros
function_header
    : declarator parameter_list
    ;

// Lista de parâmetros entre parênteses; pode estar vazia
// ex: ()   ou   (int a, b)   ou   (char c)
parameter_list
    : '(' parameter_declaration? ')'
    ;

// Declaração de parâmetros: aceita int OU char como tipo, seguido dos nomes
// ALTERAÇÃO (item 1): o tipo passou de apenas INT para (INT | CHAR),
// permitindo parâmetros do tipo char
// ex: int a, b, c   ou   char x
parameter_declaration
    : (INT | CHAR) declarator (',' declarator)*
    ;

// Corpo da função: zero ou mais declarações locais, depois zero ou mais statements
function_body
    : '{' data_definition* statement* '}'
    ;

// Bloco de statements entre chaves (não admite declarações, só statements)
block
    : '{' statement* '}'
    ;

// Statement: as várias formas possíveis de comando
statement
    : expression ';'                                     // expressão seguida de ;
    | IF '(' expression ')' statement (ELSE statement)?  // if com else opcional
    | WHILE '(' expression ')' statement                 // laço while
    | BREAK ';'                                          // break (só dentro de while)
    | CONTINUE ';'                                       // continue (só dentro de while)
    | RETURN expression? ';'                             // return com ou sem valor
    | block                                              // bloco aninhado
    | ';'                                                // statement vazio
    ;

// Expressão: atribuição (direito-associativa) ou expressão aritmética/relacional
// ALTERAÇÃO: separado em dois níveis para corrigir precedência —
// atribuições ficam em 'expression' e operadores aritméticos/relacionais em 'binary',
// evitando que 'x = a + b' seja parseado como '(x = a) + b'
expression
    : IDENTIFIER '='  expression    # assignExpr     // atribuição simples:   x = expr
    | IDENTIFIER '+=' expression    # assignAddExpr  // atribuição soma:      x += expr
    | IDENTIFIER '-=' expression    # assignSubExpr  // atribuição subtração: x -= expr
    | IDENTIFIER '*=' expression    # assignMulExpr  // atribuição produto:   x *= expr
    | IDENTIFIER '/=' expression    # assignDivExpr  // atribuição divisão:   x /= expr
    | IDENTIFIER '%=' expression    # assignModExpr  // atribuição módulo:    x %= expr
    | binary                        # binaryExpr     // expressão sem atribuição
    ;

// Operadores binários aritméticos e relacionais (sem atribuição)
binary
    : binary '==' binary    # eqExpr   // igualdade:        a == b
    | binary '!=' binary    # neqExpr  // diferença:        a != b
    | binary '<'  binary    # ltExpr   // menor que:        a < b
    | binary '<=' binary    # leExpr   // menor ou igual:   a <= b
    | binary '>'  binary    # gtExpr   // maior que:        a > b
    | binary '>=' binary    # geExpr   // maior ou igual:   a >= b
    | binary '+'  binary    # addExpr  // adição:           a + b
    | binary '-'  binary    # subExpr  // subtração:        a - b
    | binary '*'  binary    # mulExpr  // multiplicação:    a * b
    | binary '/'  binary    # divExpr  // divisão:          a / b
    | binary '%'  binary    # modExpr  // módulo:           a % b
    | unary                 # unaryExpr // expressão unária
    ;

// Pré-incremento, pré-decremento ou expressão primária
unary
    : '++' IDENTIFIER   # preInc      // pré-incremento: ++x
    | '--' IDENTIFIER   # preDec      // pré-decremento: --x
    | primary           # primaryExpr // expressão primária
    ;

// Expressão primária.
// Chamada de função vem antes de identificador simples para o ANTLR não confundir f(...) com f.
// ALTERAÇÃO (item 1): adicionada alternativa CONSTANT_CHAR (label charPrimary),
// que representa uma literal de caractere como 'a' ou '\n'.
// O analisador semântico usa esse label para inferir o tipo char da expressão.
primary
    : IDENTIFIER '(' argument_list? ')'   # callPrimary   // chamada de função: soma(a, b)
    | IDENTIFIER                          # identPrimary  // variável: x
    | CONSTANT_INT                        # intPrimary    // constante inteira: 42
    | CONSTANT_CHAR                       # charPrimary   // constante char: 'a'
    | '(' expression ')'                  # parenPrimary  // expressão entre parênteses: (a + b)
    ;

// Lista de argumentos de uma chamada de função
argument_list
    : expression (',' expression)*
    ;

// =============================================================================
// REGRAS DO LEXER (análise léxica)
// =============================================================================

// Palavras reservadas declaradas ANTES de IDENTIFIER para que o lexer
// não as confunda com identificadores comuns.
INT      : 'int'      ; // tipo inteiro
CHAR     : 'char'     ; // tipo caractere — ADICIONADO (item 1 do trabalho)
IF       : 'if'       ;
ELSE     : 'else'     ;
WHILE    : 'while'    ;
BREAK    : 'break'    ;
CONTINUE : 'continue' ;
RETURN   : 'return'   ;

// Identificador: começa com letra ou underscore, seguido de letras, dígitos ou underscore
IDENTIFIER
    : [a-zA-Z_] [a-zA-Z_0-9]*
    ;

// Constante inteira: um ou mais dígitos decimais
CONSTANT_INT
    : [0-9]+
    ;

// Constante char — ADICIONADA (item 1 do trabalho).
// Um único caractere entre aspas simples, incluindo sequências de escape
// como '\n', '\t', '\\', '\'', '\0', etc., seguindo a sintaxe do C.
CONSTANT_CHAR
    : '\'' ( EscapeSequence | ~['\\\r\n] ) '\''
    ;

// Fragmento auxiliar para sequências de escape dentro de CONSTANT_CHAR.
// "fragment" significa que essa regra não gera token próprio, só é reutilizada internamente.
fragment EscapeSequence
    : '\\' [btnfr0\\'"]
    ;

// Espaços em branco: ignorados pelo lexer
WS
    : [ \t\r\n]+ -> skip
    ;

// Comentário de linha: ignorado
LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

// Comentário de bloco: ignorado
BLOCK_COMMENT
    : '/*' .*? '*/' -> skip
    ;
