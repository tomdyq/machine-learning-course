#!/usr/bin/env python
#######################################################################################################
# FileName: k_Mean.py
# Author: wanglichen; Datetime: 2015/3/29
# Desciption: k-means related functions
# 
#######################################################################################################
import sys

# For scientific computing
from numpy import *
import scipy.misc, scipy.io, scipy.optimize, scipy.cluster.vq

########################################################################################################
# FunctionName: findClosetCentroids
# Description: find the closet Centroids 
# Input: X belongs m*n dimensional, centroids belongs to k*n dimensinal matrix. 
# Output: idx belongs to m*1 dimensional matrix, each entry contains the index of K which closet to itself
#
#########################################################################################################
def findClosetCentroids(X, centroids):
	K = shape(centroids)[0] # K = k 
	m = shape(X)[0] 
	
	idx = zeros((m,1))
	for i in range(0,m):
		lowest = 999
		lowest_index = 0
		
		for k in range(0, K):
			cost = X[i] - centroids[k] 
			cost = cost.T.dot(cost)
			if cost < lowest:
				lowest_index = k
				lowest = cost
		idx[i] = lowest_index
	return idx+1 
	
########################################################################################################
# FunctionName: computeCentroids
# Description: compute new centroids according to last labeled data
# 
#
#########################################################################################################
def computeCentroids(X, idx, K):
	m, n = shape(X)
	centroids = zeros((K,n))

	data = c_[X, idx]
	
	for k in range(1, K+1):
		temp = data[data[:, n] == k] # quickly extract X that falls into the cluster
		count = shape(temp)[0]

		for j in range(0, n):
			centroids[k-1, j] = sum(temp[:,j]) / count
	return centroids


