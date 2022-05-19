
def Lagrange(vx, vy, z):
    v = sorted(zip(vx, vy))
    m = len(v)
    s = 0

    for i in range(m):
        r = v[i][1]
        for j in range(m):
            if i != j:
                r = r*(z-v[j][0])/(v[i][0]-v[j][0])
        s += r
    return s



