// if e if-else
int a;
int b;
int max;

int maior(int x, y) {
    int r;
    if (x > y)
        r = x;
    else
        r = y;
    return r;
}

int main() {
    a = 7;
    b = 12;
    max = maior(a, b);
    if (max == 12)
        a = 1;
    return 0;
}