#!/usr/bin/env python
#########################################################################
# Filename: LinearRegression_multi.py
# Author: wanglichen; Datetime: 2015/03/27
# Description: implement linear regression with multi variable
# Version: 0.2
#
########################################################################
import sys
sys.path.append('../../lib/LinearRegression')
sys.path.append('../../lib/LogisticRegression')
#For scientific computing
from numpy import *
import scipy

#For plotting
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D
#From lib
from featureNormalize import featureNormalize
from gradientDescent import gradientDescent

def main():
	set_printoptions(precision=6, linewidth=200)
        
	# loading data
	data = genfromtxt('data/ex1data2.txt', delimiter = ',')
	X = data[:, 0:2]
	y = data[:, 2:3]
	m = shape(X)[0]	

	X, mu, sigma = featureNormalize(X)
#	print X
#	print mu
#	print sigma
	X = c_[ones((m, 1)), X]
	m ,n = shape(X)[0], shape(X)[1]
	iterations = 400
	alphas = [0.01, 0.03, 0.1, 0.3, 1.0] 
	
	for alpha in alphas:
		theta = zeros((n,1))
		J_history, theta = gradientDescent(X, y, theta, alpha, iterations)
		#print theta	
		number_of_iterations = array([x for x in range(1, iterations + 1)]).reshape(iterations, 1)
		pyplot.plot(number_of_iterations, J_history, '-b')
		pyplot.title("Alpha = %f" % (alpha))
		pyplot.xlabel('Number of iterations')
		pyplot.xlim([0, 50])
		pyplot.show(block=True)
			
		
if __name__ == '__main__':
	main()
