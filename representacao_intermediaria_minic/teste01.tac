func soma:
    param a
    param b
    t1 = a + b
    resultado = t1
    return resultado
endfunc soma

func main:
    x = 10
    y = 3
    t2 = x + y
    t3 = t2 * 2
    z = t3
    param x
    param y
    t4 = call soma, 2
    x = t4
    return 0
endfunc main

