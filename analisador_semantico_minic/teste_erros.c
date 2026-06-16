/* teste_erros.c
   Cada funcao provoca exatamente um erro semantico.
   Itens: a, b, c, d, e, f, g */

// funcao auxiliar usada nos testes c e d
int aux(int x) {
    return x;
}

// funcao auxiliar com parametro char usada no teste d
int auxChar(char c) {
    return 0;
}

// ------------------------------------------------------------------
// item a: uso de variavel nao declarada
// Esperado: erro em 'y' — variavel 'y' nao declarada
// ------------------------------------------------------------------
int testeA() {
    int x;
    x = y;
    return x;
}

// ------------------------------------------------------------------
// item b: variavel declarada mais de uma vez no mesmo escopo
// Esperado: erro em 'z' — 'z' ja foi declarado neste escopo
// ------------------------------------------------------------------
int testeB() {
    int z;
    int z;
    return z;
}

// ------------------------------------------------------------------
// item c: numero errado de argumentos na chamada
// Esperado: erro — 'aux' espera 1 argumento, recebeu 2
// ------------------------------------------------------------------
int testeC() {
    return aux(1, 2);
}

// ------------------------------------------------------------------
// item d: tipo errado no argumento da chamada
// Esperado: erro — argumento 1 de 'aux': esperado 'int', recebido 'char'
// ------------------------------------------------------------------
int testeD() {
    char c;
    c = 'a';
    return aux(c);
}

// ------------------------------------------------------------------
// item e: atribuicao incompativel (int recebendo char)
// Esperado: erro — atribuicao incompativel: 'n' e 'int', mas expressao e 'char'
// ------------------------------------------------------------------
int testeE() {
    int n;
    char c;
    c = 'b';
    n = c;
    return n;
}

// ------------------------------------------------------------------
// item e (composto): += em variavel char
// Esperado: erro — operador '+=' requer variavel do tipo int, mas 'c' e 'char'
// ------------------------------------------------------------------
int testeEComposto() {
    char c;
    c = 'a';
    c += 1;
    return 0;
}

// ------------------------------------------------------------------
// item f: operando de operador aritmetico e char
// Esperado: erro — operando de '+' deve ser int, mas e 'char'
// ------------------------------------------------------------------
int testeF() {
    char c;
    int n;
    c = 'x';
    n = 0;
    n = n + c;
    return n;
}

// ------------------------------------------------------------------
// item g: break fora de while
// Esperado: erro — 'break' utilizado fora de laco while
// ------------------------------------------------------------------
int testeGBreak() {
    break;
    return 0;
}

// ------------------------------------------------------------------
// item g: continue fora de while
// Esperado: erro — 'continue' utilizado fora de laco while
// ------------------------------------------------------------------
int testeGContinue() {
    continue;
    return 0;
}