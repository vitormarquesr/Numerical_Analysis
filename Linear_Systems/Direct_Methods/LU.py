
def LU(M):

	U = [l[:] for l in M]
	n = len(U)

	#Lower triangular matrix
	L = [[0 for q in range(n)] for y in range(n)]
	
	#Vector of swaps
	p = [t for t in range(n)]

	for i in range(n):

		#Partial pivoting
		piv = [abs(U[k][i]) for k in range(i, n)]
		r = piv.index(max(piv)) + i

		U[i], U[r] = U[r], U[i]

		L[i], L[r] = L[r], L[i]

		p[i], p[r] = p[r], p[i]


		#Gaussian elimination
		for t in range(i+1, n):
			m = U[t][i]/U[i][i]

			L[t][i] = m

			for f in range(i, n):
				U[t][f] -= m*U[i][f]

	for k in range(n):
		L[k][k] = 1

	#Converting the vector into the permutation matrix
	P = [[0 for i in range(n)] for t in range(n)]
	for k in range(n):
		P[k][p[k]] = 1

	return L, U, P
