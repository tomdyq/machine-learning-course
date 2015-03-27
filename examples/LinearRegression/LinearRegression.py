#!/usr/bin/env python
##########################################################################
# Filename: LinearRegression.py
# Author: wanglichen; Datetime:2015/03/27
# Description: implement linear regression and get to see it work
# Version: 0.1
#
#########################################################################
import sys
sys.path.append("../../lib/LinearRegression")
#Import python modules for scientific
from numpy import *
import scipy

#Import python modules for plotting
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D
from plot_simple import plot

#Import lib
from computeCost import computeCost
from gradientDescent import gradientDescent
DATA_DIRECTORY_PATH = '/home/lichen/HarperMllib/data'

def main():
	set_printoptions(precision=6, linewidth=200)
	A = eye(5)
	print A
	
	print 'load data from labeled txt file which delimited by ","'
	data = genfromtxt(DATA_DIRECTORY_PATH + "/ex1data1.txt", delimiter = ',')
	X, y = data[:, 0], data[:, 1]
	m = len(y)
	y = y.reshape(m,1)
	print 'The length of matrix labeled file is ', m
	
	print 'Show 2D data'
	plot(X, y)
	pyplot.show(block=True)
		
	X = c_[ones((m,1)), X]
	theta = zeros((2,1))
	iterations = 1500
	alpha = 0.01

	cost = computeCost(X,y,theta)
	print cost
	cost, theta = gradientDescent(X, y, theta, alpha, iterations)	
	#print cost
	print 'theta = ', theta	
	
	print 'prediction1: population city in ', 3.5, 's'
	predict1 = array([1, 3.5]).dot(theta)
	print 'profit is ', predict1
        
	plot(X[:,1], y)
	pyplot.plot(X[:, 1], X.dot(theta), 'b-')
	pyplot.show(block=True)
	
if __name__ == '__main__':
	main()

