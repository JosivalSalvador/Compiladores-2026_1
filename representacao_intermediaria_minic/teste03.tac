func main:
    n = 10
    soma = 0
    i = 0
L1:
    t1 = i < n
    if t1 goto L2
    goto L3
L2:
    t2 = i + 1
    i = t2
    t3 = i == 5
    if t3 goto L4
    goto L5
L4:
    goto L1
L5:
    t4 = i == 9
    if t4 goto L6
    goto L7
L6:
    goto L3
L7:
    t5 = soma + i
    soma = t5
    goto L1
L3:
    return soma
endfunc main

