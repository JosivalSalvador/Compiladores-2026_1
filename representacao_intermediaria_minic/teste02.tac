func maior:
    param x
    param y
    t1 = x > y
    if t1 goto L1
    goto L3
L1:
    r = x
    goto L2
L3:
    r = y
L2:
    return r
endfunc maior

func main:
    a = 7
    b = 12
    param a
    param b
    t2 = call maior, 2
    max = t2
    t3 = max == 12
    if t3 goto L4
    goto L5
L4:
    a = 1
L5:
    return 0
endfunc main

