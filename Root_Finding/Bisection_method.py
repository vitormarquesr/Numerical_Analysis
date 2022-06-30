
def bisection(f, a, b, eps=10**(-3), iter_max=1000, start=1):
    x1 = (a + b)/2
    if iter_max == 1:
        return x1
    for i in range(start+1, iter_max+1):
        x0 = x1
        if f(a)*f(x0) < 0:
            b = x0
        else:
            a = x0
        x1 = (a + b)/2
        if abs(x1-x0) < eps:
            return x1
    return x1

