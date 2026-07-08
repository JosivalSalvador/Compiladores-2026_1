# Teste 2 - Operacoes relacionais e logicas
# Cobre: >, >=, <, <=, ==, !=, &&, ||, !
#
# Equivalente em alto nivel:
# a = 5
# b = 8
# maior = a > b
# maiorIgual = a >= b
# menorIgual = a <= b
# igual = a == b
# diferente = a != b
# e = (a < b) && (b > 0)
# ou = (a == b) || (b > 0)
# nao = !igual
# print maior, maiorIgual, menorIgual, igual, diferente, e, ou, nao

a = 5
b = 8
maior = a > b
maiorIgual = a >= b
menorIgual = a <= b
igual = a == b
diferente = a != b
t1 = a < b
t2 = b > 0
e = t1 && t2
t3 = a == b
t4 = b > 0
ou = t3 || t4
nao = !igual

print "maior = ", maior
print "maiorIgual = ", maiorIgual
print "menorIgual = ", menorIgual
print "igual = ", igual
print "diferente = ", diferente
print "e = ", e
print "ou = ", ou
print "nao = ", nao

# Saida esperada:
# maior = 0
# maiorIgual = 0
# menorIgual = 1
# igual = 0
# diferente = 1
# e = 1
# ou = 1
# nao = 1