# Teste 4 - While com laco (goto para tras)
# Cobre: while, laco real com goto retornando ao inicio, acumulador
#
# Equivalente em alto nivel:
# i = 0
# soma = 0
# while (i < 5) {
#     soma = soma + i;
#     i = i + 1;
# }
# print soma
# print i

i = 0
soma = 0
L1:
t1 = i < 5
if t1 goto L2
goto L3
L2:
soma = soma + i
i = i + 1
goto L1
L3:
print "soma = ", soma
print "i = ", i

# Saida esperada:
# soma = 10   (0+1+2+3+4)
# i = 5