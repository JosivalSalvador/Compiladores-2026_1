# Teste 5 - Definicao e chamada de funcao (caso mais complexo)
# Cobre: func/endfunc, parametros (p0, p1...), funcao com 0 parametros,
#        return, param, call, combinado com while e if dentro da funcao
#
# Equivalente em alto nivel:
# int fatorial(int n) {
#     int i = 1;
#     int fat = 1;
#     while (i <= n) {
#         fat = fat * i;
#         i = i + 1;
#     }
#     return fat;
# }
#
# int soma(int a, int b) {
#     return a + b;
# }
#
# int maiorQue10(int x) {
#     if (x > 10) {
#         return 1;
#     }
#     return 0;
# }
#
# int constante() {
#     int x = 42;
#     int y = 8;
#     return x + y;
# }
#
# n = 5
# f = fatorial(n);
# print f
#
# r = soma(7, 8);
# print r
#
# print maiorQue10(f)
# print maiorQue10(r)
#
# print constante()

func fatorial, 1:
i = 1
fat = 1
L1:
t1 = i <= p0
if t1 goto L2
goto L3
L2:
fat = fat * i
i = i + 1
goto L1
L3:
return fat
endfunc

func soma, 2:
r = p0 + p1
return r
endfunc

func maiorQue10, 1:
t1 = p0 > 10
if t1 goto L4
return 0
L4:
return 1
endfunc

func constante, 0:
x = 42
y = 8
soma2 = x + y
return soma2
endfunc

n = 5
param n
f = call fatorial, 1
print "fatorial(5) = ", f

param 7
param 8
resultadoSoma = call soma, 2
print "soma(7,8) = ", resultadoSoma

param f
maior1 = call maiorQue10, 1
print "maiorQue10(f) = ", maior1

param resultadoSoma
maior2 = call maiorQue10, 1
print "maiorQue10(soma) = ", maior2

r0 = call constante, 0
print "constante() = ", r0

# Saida esperada:
# fatorial(5) = 120
# soma(7,8) = 15
# maiorQue10(f) = 1     (120 > 10)
# maiorQue10(soma) = 1  (15 > 10)
# constante() = 50      (42 + 8, chamada sem parametros)