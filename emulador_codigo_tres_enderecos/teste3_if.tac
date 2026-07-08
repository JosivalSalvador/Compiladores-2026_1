# Teste 3 - If com goto e rotulos
# Cobre: if, goto, rotulos, if/else simulado
#
# Equivalente em alto nivel:
# a = 10
# b = 60
# if (b > 50) {
#     a = a + 5;
# } else {
#     a = a - 3;
# }
# print a

a = 10
b = 60
t1 = b > 50
if t1 goto L1
a = a - 3
goto L2
L1:
a = a + 5
L2:
print "a = ", a

# Segundo caso: mesma logica, mas com a condicao falsa
c = 10
d = 20
t2 = d > 50
if t2 goto L3
c = c - 3
goto L4
L3:
c = c + 5
L4:
print "c = ", c

# Saida esperada:
# a = 15   (b=60 > 50, entra no if)
# c = 7    (d=20, nao > 50, entra no else)