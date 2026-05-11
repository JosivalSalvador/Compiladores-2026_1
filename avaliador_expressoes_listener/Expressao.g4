grammar Expressao;

// Regra inicial
prog: expr EOF ;

// Precedência crescente de cima para baixo

expr
    : expr '+' term      # Soma
    | expr '-' term      # Subtracao
    | term               # PassaTerm
    ;

term
    : term '*' power     # Multiplicacao
    | term '/' power     # Divisao
    | power              # PassaPower
    ;

power
    : unary '^' power    # Potenciacao
    | unary              # PassaUnary
    ;

unary
    : 'fact'     unary   # Fatorial
    | 'absoluto' unary   # ValorAbsoluto
    | atom               # PassaAtom
    ;

atom
    : '(' expr ')'       # Parentesis
    | NUMBER             # Numero
    ;

// Tokens
NUMBER : [0-9]+ ('.' [0-9]+)? ;
WS     : [ \t\r\n]+ -> skip ;