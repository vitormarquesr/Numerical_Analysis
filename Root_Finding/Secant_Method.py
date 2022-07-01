
def Secant_Method(f, x0, x1, eps=10**(-3), iter_max=1000):
    x = [x0, x1]
    for i in range(2, iter_max + 2):
        x.append((x[i-2]*f(x[i-1]) -x[i-1]*f(x[i-2]))/(f(x[i-1]) - f(x[i-2])))

        if abs(x[i] - x[i - 1]) < eps:
            return x[i]

    return x[i]



