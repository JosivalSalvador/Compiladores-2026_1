/* Arquivo de teste completo para a gramatica miniC.
   Cobre todas as regras do EBNF: variaveis globais, funcoes com e sem
   retorno, todos os operadores, todos os statements e estruturas de controle. */

// --- variaveis globais (data_definition no nivel do programa) ---
int g1, g2, g3;
int contador;

// --- funcao sem tipo de retorno e sem parametros ---
semRetorno() {
    ;
}

// --- funcao com retorno int e sem parametros ---
int semParametros() {
    return 0;
}

// --- funcao com um unico parametro ---
int umParam(int x) {
    return x;
}

// --- funcao com multiplos parametros (int a, b, c) ---
int multiParam(int a, b, c) {
    int local1, local2;
    local1 = a + b;
    local2 = local1 * c;
    return local2;
}

// --- funcao que exercita todos os operadores de atribuicao ---
int operadoresAtribuicao(int n) {
    n += 10;
    n -= 5;
    n *= 2;
    n /= 3;
    n %= 4;
    return n;
}

// --- funcao que exercita todos os operadores binarios relacionais e aritmeticos ---
int operadoresBinarios(int a, b) {
    int r;
    r = a == b;
    r = a != b;
    r = a < b;
    r = a <= b;
    r = a > b;
    r = a >= b;
    r = a + b;
    r = a - b;
    r = a * b;
    r = a / b;
    r = a % b;
    return r;
}

// --- funcao que exercita operadores unarios (pre-incremento e pre-decremento) ---
int operadoresUnarios(int x) {
    ++x;
    --x;
    return x;
}

// --- funcao que exercita expressao entre parenteses ---
int parenteses(int a, b) {
    return (a + b) * (a - b);
}

// --- funcao que exercita if sem else ---
int ifSemElse(int x) {
    if (x > 0)
        return x;
    return 0;
}

// --- funcao que exercita if com else ---
int ifComElse(int x) {
    if (x >= 0) {
        return x;
    } else {
        return 0;
    }
}

// --- funcao que exercita if-else encadeado ---
int ifElseEncadeado(int x) {
    if (x > 0) {
        return 1;
    } else {
        if (x < 0) {
            return 0;
        } else {
            return 0;
        }
    }
}

// --- funcao que exercita while ---
int somaAte(int n) {
    int acum;
    acum = 0;
    while (n > 0) {
        acum += n;
        n -= 1;
    }
    return acum;
}

// --- funcao que exercita break e continue dentro de while ---
int breakContinue(int n) {
    int i;
    i = 0;
    while (i < n) {
        if (i == 5) {
            break;
        }
        if (i == 3) {
            ++i;
            continue;
        }
        ++i;
    }
    return i;
}

// --- funcao que exercita return sem expressao ---
semRetornoExpr() {
    return;
}

// --- funcao que exercita statement vazio ---
int statementVazio() {
    ;;
    return 0;
}

// --- funcao que exercita blocos aninhados (block so aceita statements, sem data_definition) ---
int blocosAninhados(int x) {
    {
        {
            x = x + 1;
        }
        x = x * 2;
    }
    return x;
}

// --- funcao que exercita chamada de funcao sem argumentos ---
int chamadaSemArgs() {
    int r;
    r = semParametros();
    return r;
}

// --- funcao que exercita chamada de funcao com argumentos ---
int chamadaComArgs(int a, b) {
    int r;
    r = multiParam(a, b, 10);
    return r;
}

// --- funcao que exercita chamada de funcao como parte de expressao ---
int chamadaEmExpr(int x) {
    return umParam(x) + umParam(x);
}

// --- funcao principal exercitando tudo junto ---
int main() {
    int a, b, resultado;
    a = 10;
    b = 3;
    resultado = operadoresBinarios(a, b);
    resultado = operadoresAtribuicao(resultado);
    resultado = operadoresUnarios(resultado);
    resultado = somaAte(resultado);
    resultado = breakContinue(resultado);
    resultado = blocosAninhados(resultado);
    if (resultado > 0) {
        return resultado;
    } else {
        return 0;
    }
}