from math import factorial

def Gregory_Newton(x0, h, y, z):
    ux = (z - x0)/h
    m = len(y)

    dif = [y[i] for i in range(m)]

    for i in range(1, m):
        for k in range(m-1,i-1,-1):
            dif[k] = dif[k] - dif[k-1]

    r = ux
    s = dif[0]
    for i in range(1, m):
        s += dif[i]*r/factorial(i)
        r = r*(ux - i)

    return s

