func fatorial:
    param n
    resultado = 1
L1:
    t1 = n > 1
    if t1 goto L2
    goto L3
L2:
    t2 = resultado * n
    resultado = t2
    t3 = n - 1
    n = t3
    goto L1
L3:
    return resultado
endfunc fatorial

func main:
    param 5
    t4 = call fatorial, 1
    fat = t4
    return fat
endfunc main

