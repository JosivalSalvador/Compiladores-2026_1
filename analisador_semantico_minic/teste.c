/* teste.c
   Arquivo sem erros semanticos.
   Cobre todos os itens do trabalho: a, b, c, d, e, f, g */

// variaveis globais
int g1, g2;
char gc1, gc2;

// funcao sem retorno e sem parametros
semRetorno() {
    ;
}

// funcao com retorno int sem parametros
int semParam() {
    return 0;
}

// funcao com um parametro int
int umParamInt(int x) {
    return x;
}

// funcao com um parametro char
int umParamChar(char c) {
    int n;
    n = 0;
    return n;
}

// funcao com multiplos parametros int
int multiParam(int a, b, c) {
    int resultado;
    resultado = a + b + c;
    return resultado;
}

// funcao que testa todos os operadores aritmeticos com int (item f ok)
int aritmetica(int a, b) {
    int r;
    r = a + b;
    r = a - b;
    r = a * b;
    r = a / b;
    r = a % b;
    return r;
}

// funcao que testa todos os operadores relacionais (item f ok)
int relacionais(int a, b) {
    int r;
    r = a == b;
    r = a != b;
    r = a < b;
    r = a <= b;
    r = a > b;
    r = a >= b;
    return r;
}

// funcao que testa todas as atribuicoes compostas com int (item e ok)
int atribuicoes(int n) {
    n += 10;
    n -= 5;
    n *= 2;
    n /= 3;
    n %= 4;
    return n;
}

// funcao que testa atribuicao simples char = char (item e ok)
int atribuicaoChar() {
    char c1, c2;
    c1 = 'a';
    c2 = c1;
    return 0;
}

// funcao que testa atribuicao simples int = int (item e ok)
int atribuicaoInt() {
    int a, b;
    a = 42;
    b = a;
    return b;
}

// funcao que testa pre-incremento e pre-decremento
int incDec(int x) {
    ++x;
    --x;
    return x;
}

// funcao que testa if sem else (item g: break/continue dentro de while ok)
int ifSemElse(int x) {
    if (x > 0)
        return x;
    return 0;
}

// funcao que testa if com else
int ifComElse(int x) {
    if (x >= 0) {
        return x;
    } else {
        return 0;
    }
}

// funcao que testa while com break e continue (item g ok)
int whileComBreakContinue(int n) {
    int i;
    i = 0;
    while (i < n) {
        if (i == 3) {
            ++i;
            continue;
        }
        if (i == 7) {
            break;
        }
        ++i;
    }
    return i;
}

// funcao que testa while aninhado com break em cada nivel (item g ok)
int whileAninhado(int n) {
    int i, j;
    i = 0;
    while (i < n) {
        j = 0;
        while (j < n) {
            if (j == 2) {
                break;
            }
            ++j;
        }
        if (i == 3) {
            break;
        }
        ++i;
    }
    return i;
}

// funcao que testa chamada sem argumentos (item c ok)
int chamadaSemArgs() {
    int r;
    r = semParam();
    return r;
}

// funcao que testa chamada com argumentos int (itens c e d ok)
int chamadaComArgsInt(int a, b) {
    int r;
    r = multiParam(a, b, 10);
    return r;
}

// funcao que testa chamada com argumento char (itens c e d ok)
int chamadaComArgChar(char c) {
    int r;
    r = umParamChar(c);
    return r;
}

// funcao que testa expressao entre parenteses
int parenteses(int a, b) {
    return (a + b) * (a - b);
}

// funcao que testa blocos aninhados
int blocosAninhados(int x) {
    {
        {
            x = x + 1;
        }
        x = x * 2;
    }
    return x;
}

// funcao que testa statement vazio
int statementVazio() {
    ;;
    return 0;
}

// funcao que testa return sem expressao
semRetornoExpr() {
    return;
}

// funcao principal
int main() {
    int a, b, r;
    char c1, c2;

    a = 10;
    b = 3;
    c1 = 'z';
    c2 = c1;

    r = aritmetica(a, b);
    r = relacionais(a, b);
    r = atribuicoes(r);
    r = incDec(r);
    r = whileComBreakContinue(r);
    r = whileAninhado(r);
    r = chamadaSemArgs();
    r = chamadaComArgsInt(a, b);
    r = parenteses(a, b);
    r = blocosAninhados(r);
    r = statementVazio();

    if (r > 0) {
        return r;
    } else {
        return 0;
    }
}