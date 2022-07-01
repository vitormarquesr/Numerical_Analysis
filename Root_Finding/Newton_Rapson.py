
def Newton_Rapson(f, f1, x0, eps=10**(-3), iter_max=1000):
    x = [x0]
    for i in range(1, iter_max+1):
        x.append(x[i-1] - f(x[i-1])/f1(x[i-1]))
        if abs(x[i] - x[i-1]) < eps:
            return x[i]


    return x[i]



