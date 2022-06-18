def mult(gl):
    if gl == 1:
        return 1/2
    elif gl == 2:
        return 1/3
    elif gl == 3:
        return 3/8

def coef(i, n, gl):
    if i == 0 or i == n:
        return 1
    elif gl == 2 and i % 2 != 0:
        return 4
    elif gl == 3 and i % 3 != 0:
        return 3
    return 2


def Newton_Cotes(f, a, b, n, gl=1):
    if (gl < 1 or gl > 3) or (n % gl != 0):
        return False
    #For gl=k we need k intervals for each
    #repetition. So, n must be divisible by k.

    h = (b - a)/n
    s = 0
    x0 = a

    for i in range(0, n+1):
        s += coef(i,n,gl)*f(x0+i*h)

    s = s*h*mult(gl)

    return s

