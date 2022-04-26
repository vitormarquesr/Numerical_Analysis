#Complexity O(n^3)

#Hypothesis
#A must be symmetric: A = A^T
#A must be positive definite

def Cholesky(A):
    n = len(A)

    L = [[0 for k in range(n)] for t in range(n)]

    for j in range(n):
        for i in range(j, n):
            s = 0
            for k in range(0, j):
                s += L[i][k]*L[j][k]
            if i == j:
                t = A[i][j] - s
                if t <= 0:
                    return False
                L[i][j] = t**(1/2)
            else:
                L[i][j] = (A[i][j] - s)/L[j][j]
    return L

