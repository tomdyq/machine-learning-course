#!/usr/bin/env python
from numpy import *
import scipy
#From lib
from computeCost import computeCost
from hypothesis import hypothesis

####################################################################
# FunctionName: gradientDescent
# Author: wanglichen
# Description: implement gradient descent, trying to optimize theta
# 
####################################################################
def gradientDescent(X, y, theta, alpha, iterations):
	grad = copy(theta)
	m = len(y)
	J_history = []
	
	for counter in range(0, iterations):
		inner_sum = X.T.dot(hypothesis(X, grad) - y)
		grad -= alpha / m * inner_sum
		J_history.append(computeCost(X, y, grad))
	return J_history, grad
