#!/usr/bin/env python
##########################################################################
# Filename: logistic.py
# Author: wanglichen; Datetime: 2015/03/27
# Description:  implement logistic regression 
# Version: 0.2
#
#########################################################################
import sys
sys.path.append("../../lib/LogisticRegression")
import scipy.optimize, scipy.special
from numpy import *
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D

from optimize_gradient import optimize_gradient
from costFunction_Logistic import costFunction
from sigmoid import *


def plot( data ):
	positives = data[data[:,2] == 1]
	negatives = data[data[:,2] == 0]

	pyplot.xlabel("Exam 1 score")
	pyplot.ylabel("Exam 2 score")
	pyplot.xlim([25, 115])
	pyplot.ylim([25, 115])

	pyplot.scatter( negatives[:, 0], negatives[:, 1], c='y', marker='o', s=40, linewidths=1, label="Not admitted" )
	pyplot.scatter( positives[:, 0], positives[:, 1], c='b', marker='+', s=40, linewidths=2, label="Admitted" )
	pyplot.legend()

def plotBoundary( data, X, theta ):
	plot( data )
	plot_x = array( [min(X[:,1]), max(X[:,1])] )
	plot_y = (-1./ theta[2]) * (theta[1] * plot_x + theta[0])
	pyplot.plot( plot_x, plot_y )

def predict(data, theta):
	return data.dot(theta)

def main():
	set_printoptions(precision=6, linewidth=200)
        data = genfromtxt("/home/lichen/HarperMllib/data/ex2data1.txt", delimiter = ',')
	m, n = shape(data)[0], shape(data)[1] - 1
	X = c_[ones((m,1)), data[:, :n]]
	y = data[:, n:n+1]

	plot(data)
	pyplot.show(block=True)

	theta = zeros((n+1, 1))
	
	theta, cost = optimize_gradient(costFunction, X, y, theta, 500, True)
	plotBoundary(data, X, theta)
	pyplot.show()
	test = array([1,45,85])
	print predict(test, theta)	

if __name__ == '__main__':
	main()
