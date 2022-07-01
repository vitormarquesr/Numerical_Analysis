
def Bisection(f, a, b, eps=10**(-3), iter_max=1000):
    x = []
    for i in range(0, iter_max + 1):
        x.append((a+b)/2)
        if f(a)*f(x[i]) < 0:
            b = x[i]
        else:
            a = x[i]

        if i != 0 and abs(x[i] - x[i-1]) < eps:
            return x[i]
    return x[i]


