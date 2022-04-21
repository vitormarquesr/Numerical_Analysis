#O(n^3) Complexity

def Gauss(M):
    n = len(M)
    M = [l[:] for l in M]
    for k in range(n):
        #Partial Pivoting
        all = [abs(M[t][k]) for t in range(k, n)]
        i_m = all.index(max(all)) + k

        M[k], M[i_m] = M[i_m], M[k]

        #Elimination
        for i in range(k+1, n):
            M[i] = [M[i][t] - M[k][t]*(M[i][k]/M[k][k]) for t in range(0, n+1)]

    return M


