func main:
    letra = 'A'
    contador = 5
    valor = 2
    t1 = valor * contador
    valor = t1
    t2 = valor - 3
    valor = t2
    t3 = valor + 1
    valor = t3
L1:
    t4 = contador > 0
    if t4 goto L2
    goto L3
L2:
    t5 = contador - 1
    contador = t5
    goto L1
L3:
    return valor
endfunc main

