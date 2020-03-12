from kmeans import *
import matplotlib.pyplot as plt
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)


project_home = ".."
data_mat = []
with open(project_home + "/visualization_data/EngyTime.lrn" , 'r') as file:
	lines = file.readlines()
	for line in lines:
		first_item = line.split(" ")[0]

		if first_item == '%':

			continue
		else:
			items = line.strip().split("\t")
			data_mat.append(np.asarray(items[1:]).astype(np.float))
data_mat = np.asarray(data_mat)

a = kmeansClusterer(data_mat, 2, 0.1)
a.clustering()

# plt.figure()
# plt.plot(data_mat[:,0], data_mat[:,1], ".")
# plt.show()