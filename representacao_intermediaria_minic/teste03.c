// while com break e continue
int i;
int soma;
int n;

int main() {
    n = 10;
    soma = 0;
    i = 0;
    while (i < n) {
        ++i;
        if (i == 5)
            continue;
        if (i == 9)
            break;
        soma += i;
    }
    return soma;
}