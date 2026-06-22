// tipo char e atribuições compostas
char letra;
int contador;
int valor;

int main() {
    letra = 'A';
    contador = 5;
    valor = 2;
    valor *= contador;
    valor -= 3;
    valor += 1;
    while (contador > 0) {
        --contador;
    }
    return valor;
}