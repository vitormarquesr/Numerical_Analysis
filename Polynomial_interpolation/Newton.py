
def Newton(vx, vy, z):
    v = sorted(zip(vx, vy))
    m = len(v)
    x = [v[i][0] for i in range(m)]
    y = [v[i][1] for i in range(m)]

    dif = [y[i] for i in range(m)]

    for i in range(1, m):
        for k in range(m-1,i-1,-1):
            dif[k] = (dif[k] - dif[k-1])/(x[k]-x[k-i])

    r = (z-x[0])
    s = dif[0]
    for i in range(1, m):
        s += dif[i]*r
        r = r*(z-x[i])
    return s

