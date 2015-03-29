#!/usr/bin/env python
############################################################################################
# Filename: k_Mean_prime.py
# Author: wanglichen; Datetime: 2015/03/29
# Description: implement k-means 
#
###########################################################################################
import sys
sys.path.append('../../lib/k-Mean')
from numpy import *
import scipy.misc, scipy.io, scipy.optimize, scipy.cluster.vq
from k_Mean import * # import all libs functions

def main():
	mat = scipy.io.loadmat('data/ex7data2.mat') # load data
	X = mat['X']
	K = 3  # K 
	
	initial_centroids = array([[3,3], [6,2], [8,5]])
	idx = findClosetCentroids(X, initial_centroids)
	print idx[0:3] # should be [1,3,2]
	
	centroids = computeCentroids(X, idx, K)
	print centroids	
		

if __name__ == '__main__':
	main()
