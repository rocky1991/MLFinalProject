# Two steps
# 1. cluster assignment
# 2. centroid update
import random
import numpy as np
import math

import sys
np.set_printoptions(threshold=sys.maxsize)


class kmeansClusterer:
	def	__init__(self, data_mat, k, epsilon):
		self.data_mat = data_mat
		self.k = k
		self.epsilon = epsilon
		self.dimension = len(data_mat[0])
		self.n_points = len(data_mat)

		self.centroids = []
		self.labels = np.zeros(self.n_points)

	def init_mu_arr(self):
		mu_arr = np.zeros(self.dimension)
		for i in range(self.dimension):
			mu_arr[i] = random.uniform(np.amin(self.data_mat[:,i]), np.amax(self.data_mat[:,i]))
		return mu_arr

	def init_centroids(self):
		for i in range(self.k):
			self.centroids.append(self.init_mu_arr())

	def euc_distance(self,x, mu):
		return np.sqrt(np.sum(np.square(x -mu)))

	def assign_labels(self):
		min_dist = math.inf
		centroid_choice = 0

		for i in range(self.n_points):
			for j in range(len(self.centroids)):
				cur_dist = self.euc_distance(self.data_mat[i], self.centroids[j])
				if (cur_dist < min_dist):
					min_dist = cur_dist
					centroid_choice = j
			self.labels[i] = centroid_choice

	def update_centroids(self):

		#  Pay attention to the empty list creation here
		# doing [[]] * length would result in list of lists reference to same object,
		# making change to one list would do the same to the rest
		cluster_lists = [[] for _ in range (len(self.centroids))]

		cluster_lists[0].append(1)

		for j in range(len(self.centroids)):
			for i in range(self.n_points):
				if int(self.labels[i]) == j:
					cluster_lists[j].append(i)

		for j in range(len(self.centroids)):
			cluster_points = np.array([self.data_mat[k] for k in cluster_lists[j]])
			
			# there is a risk here, if for a label, the number of points belonging to that label is 0, cannot divide
			# to solve this problem, re-assign a random centroid
			if (len(cluster_points) == 0):
				for i in range(self.dimension):
					self.centroids[j][i] = random.uniform(np.amin(self.data_mat[:,i]), np.amax(self.data_mat[:,i]))
				continue
 
			self.centroids[j] = np.divide(np.sum(cluster_points, axis=0), len(cluster_points))


	def clustering(self):
		iter = 0
		self.init_centroids()


		# using .copy() so that it's copying the value, not the reference
		prev_centroid = self.centroids.copy()
		
		while True:
			print("Iteration >> " + str(iter))
			self.assign_labels()


			self.update_centroids()
			print(self.centroids)

			squared_diff = np.square(np.subtract(np.array(self.centroids),np.array(prev_centroid)))

			centroids_diff = np.sum(np.sum(squared_diff, axis=1))
			

			print("diff is " + str(centroids_diff))
			if centroids_diff <= self.epsilon:
				break
			
			prev_centroid = self.centroids.copy()
			iter+= 1
			print()