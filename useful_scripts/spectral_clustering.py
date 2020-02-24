import numpy as np


# A is the adjacency matrix (a square matrix)
A = np.array([[0,1,0,1,0,1,0],
			  [1,0,1,1,0,0,0],
			  [0,1,0,1,0,0,1],
			  [1,1,1,0,1,0,0],
			  [0,0,0,1,0,1,1],
			  [1,0,0,0,1,0,1],
			  [0,0,1,0,1,1,0]
			])
# delta is the degress matrix(also a square matrix)

delta = np.zeros((len(A), len(A[0])))

for i in range(0, len(A)):
	delta[i][i] = np.sum(A[i])

laplacian = delta - A
print(laplacian)

def find_weight(i, j):
	return A[i][j]

# print(find_weight(1,2))

B = np.array([0,1,0,1,0,1,0])

vals, vecs = np.linalg.eig(A)

# the number of 0 eigenvalues corresponds to the number of connected components