import numpy as np
import math
import matplotlib.cm as cm
import matplotlib.pyplot as plt


np.set_printoptions(threshold=math.inf)

def read_sample_num_data_and_plot(file_path):
	result_mat = []
	with open(file_path, 'r') as file:
		lines = file.readlines()
		for line in lines:
			row_items = line.strip().split("\t")
			if line.split(" ")[0] !='%':
				result_mat.append(np.asarray(row_items[1:]).astype(np.float))
	result_mat = np.asarray(result_mat)
	plt.figure()
	plt.plot(result_mat[:,0], result_mat[:,1], '.')
	plt.show()
	return result_mat

# mat = read_sample_num_data_and_plot("../Clustering_visualization_data/EngyTime.lrn")


def cal_sim_Gaussian(data_matrix, sigma):
	length = len(data_matrix[:,0])
	dim = len(data_matrix[0,:])

	sim_mat = np.zeros((length,length))

	for i in range(0, length):
		for j in range(1, length):
			squared_diff = np.square(data_matrix[i,:] - data_matrix[j,:])
			sum_squared_diff = np.sum(squared_diff)
			pair_wise_sim = np.sqrt(sum_squared_diff)
			sim_mat[i][j] = pair_wise_sim
			sim_mat[j][i] = pair_wise_sim
	return sim_mat

# A is similarity matrix between points, A is required to be symmetric and non-negative 
A = np.array([[0,1,0,1,0,1,0],
			  [1,0,1,1,0,0,0],
			  [0,1,0,1,0,0,1],
			  [1,1,1,0,1,0,0],
			  [0,0,0,1,0,1,1],
			  [1,0,0,0,1,0,1],
			  [0,0,1,0,1,1,0]
			])

cal_sim_Gaussian(A, 1)

# delta is the degress matrix(also a square matrix)

degree_mat = np.zeros((len(A), len(A[0])))

for i in range(0, len(A)):
	degree_mat[i][i] = np.sum(A[i])

# print(degree_mat)

laplacian = degree_mat - A
# print(laplacian)

def find_weight(i, j):
	return A[i][j]

# print(find_weight(1,2))

B = np.array([0,1,0,1,0,1,0])

vals, vecs = np.linalg.eig(A)


# the number of 0 eigenvalues corresponds to the number of connected componen
