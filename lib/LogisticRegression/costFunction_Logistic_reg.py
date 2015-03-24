#!/usr/bin/env python

from numpy import *
from sigmoid import *

def costFunction(theta, X, y, lamda):
	m = shape(X)[0]
	hypo = sigmoid(X.dot(theta))
	term1 = log(hypo).T.dot(-y)
	term2 = log(1.0 - hypo).T.dot(1-y)

	left = (term1 - term2)/m
	right = theta.T.dot(theta)*lamda/(2*m)
	return left + right
