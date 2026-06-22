// fatorial iterativo com while e return
int fat;

int fatorial(int n) {
    int resultado;
    resultado = 1;
    while (n > 1) {
        resultado *= n;
        n -= 1;
    }
    return resultado;
}

int main() {
    fat = fatorial(5);
    return fat;
}