grammar TAC;

// Um programa é uma sequência de itens: instruções soltas ou definições de função
prog: item+ EOF;

item: funcDef
    | instr;

// Definição de função: func nome, N: <instruções> endfunc
funcDef: 'func' ID ',' INT ':' instr* 'endfunc';

// Uma instrução pode ter um rótulo opcional na frente (ex: "L1: t1 = a < b")
// ou ser somente um rótulo sozinho (ex: "L3:")
instr: label? stmt
     | label;

label: ID ':';

stmt: assign
    | ifGoto
    | goto
    | printStat
    | paramStat
    | returnStat;

// x = y | x = y op z | x = -y | x = !y | x = call f, N
assign: ID '=' rhs ';'?;

rhs: 'call' ID ',' INT     # callRhs
   | operand op operand    # binaryRhs
   | '-' operand           # negRhs
   | '!' operand           # notRhs
   | operand               # copyRhs;

op: '+' | '-' | '*' | '/' | '>' | '>=' | '<' | '<=' | '==' | '!=' | '&&' | '||';

operand: ID | INT;

// Salto condicional: if <operando> goto <rótulo>
ifGoto: 'if' operand 'goto' ID ';'?;

// Salto incondicional: goto <rótulo>
goto: 'goto' ID ';'?;

// print <var|const> | print "texto" | print "texto", <var|const>
printStat: 'print' printArg (',' printArg)* ';'?;

printArg: operand | STRING;

// Empilha um argumento antes de uma chamada de função
paramStat: 'param' operand ';'?;

// Retorno de valor dentro de uma função
returnStat: 'return' operand ';'?;

ID     : [a-zA-Z_][a-zA-Z_0-9]* ;
INT    : [0-9]+ ;
STRING : '"' (~["\r\n])* '"' ;
WS     : [ \t\r\n]+ -> skip ;
COMMENT: '#' ~[\r\n]* -> skip ;