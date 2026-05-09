grammar MiniC;

// =============================================================================
// REGRAS DO PARSER (análise sintática)
// =============================================================================

// Ponto de entrada: um programa tem uma ou mais definições
// EBNF: program : definition { definition }
program
    : definition+ EOF
    ;

// Uma definição é uma variável global ou uma função
// EBNF: definition : data_definition | function_definition
definition
    : data_definition
    | function_definition
    ;

// Declaração de variável(is) inteira(s)
// EBNF: data_definition : INT declarator { ',' declarator } ';'
// ex: int x, y;
data_definition
    : INT declarator (',' declarator)* ';'
    ;

// Um declarador é um identificador
// EBNF: declarator : Identifier
declarator
    : IDENTIFIER
    ;

// Definição de função; o tipo int é opcional
// EBNF: function_definition : [ INT ] function_header function_body
// ex: int soma(int a, b) { ... }
function_definition
    : INT? function_header function_body
    ;

// Cabeçalho da função: nome + parâmetros
// EBNF: function_header : declarator parameter_list
function_header
    : declarator parameter_list
    ;

// Lista de parâmetros entre parênteses; pode ser vazia
// EBNF: parameter_list : '(' [ parameter_declaration ] ')'
parameter_list
    : '(' parameter_declaration? ')'
    ;

// Parâmetros: um único 'int' para todos os declaradores
// EBNF: parameter_declaration : INT declarator { ',' declarator }
// ex: int a, b, c
parameter_declaration
    : INT declarator (',' declarator)*
    ;

// Corpo da função: variáveis locais seguidas de statements
// EBNF: function_body : '{' { data_definition } { statement } '}'
function_body
    : '{' data_definition* statement* '}'
    ;

// Bloco de statements entre chaves
// EBNF: block : '{' { statement } '}'
block
    : '{' statement* '}'
    ;

// Statement: expressão, if/else, while, break, continue, return, bloco ou vazio
// EBNF: statement : expression ';' | IF ... | WHILE ... | BREAK ';' | ...
statement
    : expression ';'
    | IF '(' expression ')' statement (ELSE statement)?
    | WHILE '(' expression ')' statement
    | BREAK ';'
    | CONTINUE ';'
    | RETURN expression? ';'
    | block
    | ';'
    ;

// Expressão é sempre uma binary
// EBNF: expression : binary
expression
    : binary
    ;

// Expressões binárias e atribuições.
// As 6 primeiras alternativas são atribuições (exigem Identifier à esquerda).
// As demais são operações binárias entre duas expressões binárias.
// Labels (#) são obrigatórios quando há múltiplas alternativas com recursão à esquerda no ANTLR4.
// NOTA: o PDF lista '>=' duas vezes — o segundo é claramente '>' (erro tipográfico no enunciado).
// EBNF: binary : Identifier '=' binary | ... | binary '+' binary | ... | unary
binary
    : IDENTIFIER '='  binary     # assignExpr     // atribuição:          x = expr
    | IDENTIFIER '+=' binary     # assignAddExpr  // atribuição soma:     x += expr
    | IDENTIFIER '-=' binary     # assignSubExpr  // atribuição subtração: x -= expr
    | IDENTIFIER '*=' binary     # assignMulExpr  // atribuição produto:  x *= expr
    | IDENTIFIER '/=' binary     # assignDivExpr  // atribuição divisão:  x /= expr
    | IDENTIFIER '%=' binary     # assignModExpr  // atribuição módulo:   x %= expr
    | binary '==' binary         # eqExpr         // igualdade:   a == b
    | binary '!=' binary         # neqExpr        // diferença:   a != b
    | binary '<'  binary         # ltExpr         // menor que:   a < b
    | binary '<=' binary         # leExpr         // menor/igual: a <= b
    | binary '>'  binary         # gtExpr         // maior que:   a > b 
    | binary '>=' binary         # geExpr         // maior/igual: a >= b
    | binary '+'  binary         # addExpr        // adição:      a + b
    | binary '-'  binary         # subExpr        // subtração:   a - b
    | binary '*'  binary         # mulExpr        // multiplicação: a * b
    | binary '/'  binary         # divExpr        // divisão:     a / b
    | binary '%'  binary         # modExpr        // módulo:      a % b
    | unary                      # unaryExpr      // expressão unária
    ;

// Pré-incremento, pré-decremento ou expressão primária
// EBNF: unary : '++' Identifier | '--' Identifier | primary
unary
    : '++' IDENTIFIER   # preInc      // pré-incremento: ++x
    | '--' IDENTIFIER   # preDec      // pré-decremento: --x
    | primary           # primaryExpr // expressão primária
    ;

// Expressão primária
// Chamada de função vem antes de identificador simples para o ANTLR não confundir soma(...) com soma
// EBNF: primary : IDENTIFIER | CONSTANT_INT | '(' expression ')' | Identifier '(' [ argument_list ] ')'
primary
    : IDENTIFIER '(' argument_list? ')'   # callPrimary   // chamada de função: soma(a, b)
    | IDENTIFIER                          # identPrimary  // variável: x
    | CONSTANT_INT                        # intPrimary    // constante inteira: 42
    | '(' expression ')'                  # parenPrimary  // expressão entre parênteses: (a + b)
    ;

// Lista de argumentos de uma chamada de função
// EBNF: argument_list : binary { ',' binary }
argument_list
    : binary (',' binary)*
    ;

// =============================================================================
// REGRAS DO LEXER (análise léxica)
// =============================================================================

// Palavras reservadas — declaradas ANTES de IDENTIFIER para que o lexer
// as reconheça corretamente e não as trate como identificadores.
// Todas minúsculas conforme especificado no enunciado.
INT      : 'int'      ;
IF       : 'if'       ;
ELSE     : 'else'     ;
WHILE    : 'while'    ;
BREAK    : 'break'    ;
CONTINUE : 'continue' ;
RETURN   : 'return'   ;

// Identificador: letra ou underscore seguido de letras, dígitos ou underscore
IDENTIFIER
    : [a-zA-Z_] [a-zA-Z_0-9]*
    ;

// Constante inteira: um ou mais dígitos decimais
CONSTANT_INT
    : [0-9]+
    ;

// Espaços em branco — ignorados pelo lexer
WS
    : [ \t\r\n]+ -> skip
    ;

// Comentário de linha — ignorado (ex: // comentário)
LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

// Comentário de bloco — ignorado (ex: /* comentário */)
BLOCK_COMMENT
    : '/*' .*? '*/' -> skip
    ;