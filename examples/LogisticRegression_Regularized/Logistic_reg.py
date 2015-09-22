#!/usr/bin/env python
#########################################################################################################
# Filename: Logistic_reg.py
# Author: wanglichen; Datetime: 2015/03/20
# Description: implement regularized logistic regression
# to predict whether microchips from a fabrication plant passes quality assur-
# ance (QA).
# Version: 0.1
# 
##########################################################################################################
import sys
sys.path.append("../../lib")
import scipy.optimize, scipy.special
from numpy import *
from matplotlib import pyplot, cm
from mpl_toolkits.mplot3d import Axes3D

#from optimize_gradient import optimize_gradient
from costFunction_Logistic_reg import costFunction
from sigmoid import *

def plot( data ):
	negatives = data[data[:, 2] == 0]
	positives = data[data[:, 2] == 1]
	pyplot.xlabel("Microchip test 1")
	pyplot.ylabel("Microchip test 2")
	pyplot.xlim([-1.0, 1.5])
	pyplot.ylim([-1.0, 1.5])
	pyplot.scatter( negatives[:,0], negatives[:,1], c='y', marker='o', linewidths=1, s=40, label='y=0' )
	pyplot.scatter( positives[:,0], positives[:,1], c='k', marker='+', linewidths=2, s=40, label='y=1' )
	pyplot.legend()

def mapFeature( X1, X2 ):
	degrees = 6
	out = ones( (shape(X1)[0], 1) )
	for i in range(1, degrees+1):
		for j in range(0, i+1):
			term1 = X1 ** (i-j)
			term2 = X2 ** (j)
			term = (term1 * term2).reshape( shape(term1)[0], 1 )
			out = hstack(( out, term ))
	return out

def optimize_reg(theta, X, y, lamda):
	result = scipy.optimize.minimize(costFunction, theta, args= (X, y, lamda), method = 'BFGS', options={"maxiter":500, "disp":True})
	return result.x, result.fun

def main():
	set_printoptions(precision=6, linewidth=200)
	data = genfromtxt("/home/lichen/HarperMllib/data/ex2data2.txt", delimiter = ',')
	plot(data)
	pyplot.show()

	X = mapFeature( data[:,0], data[:, 1])
	y = data[:,2]
	
	theta = zeros(shape(X)[1])
	lamdas = [0.0, 1.0, 100]
	#print costFunction(theta, X, y, lamda)		
	
	#theta, cost = optimize_reg(theta, X, y, lamda)
	for lamda in lamdas:
		theta, J_history = optimize_reg(theta, X, y, lamda)
		
		pyplot.text(0.15, 1.4, 'Lamda %.1f' %lamda)
		plot(data)
		u = linspace( -1, 1.5, 50 )
		v = linspace( -1, 1.5, 50 )
		z = zeros( (len(u), len(v)) )
		for i in range(0, len(u)):
			for j in range(0, len(v)):
				mapped = mapFeature( array([u[i]]), array([v[j]]) )
				z[i,j] = mapped.dot( theta )
		z = z.transpose()
		u, v = meshgrid( u, v )
		pyplot.contour( u, v, z, [0.0, 0.0], label='Decision Boundary' )
		pyplot.show()
		
if __name__ == '__main__':
	main()
