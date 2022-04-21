#Hypothesis: All numbers in the diagonal are different from zero
#nxn matrix

#O(n^2) Complexity

#Upper matrix
def back_substitution(U):
	n = len(U)
	x = [0 for t in range(n)]

	x[n-1] = U[n-1][n]/U[n-1][n-1]

	for k in range(n-2, -1, -1):
		s = 0
		for i in range(n-1, k-1, -1):
			s += U[k][i]*x[i]
		x[k] = (U[k][n]-s)/U[k][k]

	return x


#Lower matrix
def forward_substitution(L):
	n = len(L)
	x = [0 for t in range(n)]

	x[0] = L[0][n]/L[0][0]
	
	for k in range(1, n):
		s = 0
		for i in range(0, k):
			s += L[k][i]*x[i]
		x[k] = (L[k][n] - s)/L[k][k]

	return x 
