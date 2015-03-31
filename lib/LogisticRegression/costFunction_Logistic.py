#!/usr/bin/env python

from numpy import *
from sigmoid import *
########################################################
# FunctionName: costFunction
# Author: wanglichen
# Description: cost function for logistic regression
#
#######################################################
def costFunction(theta, X, y):
	m = shape(X)[0]
	hypo = sigmoid(X.dot(theta))
	term1 = log(hypo).T.dot(-y)
	term2 = log(1.0 - hypo).T.dot(1-y)
	return ((term1 - term2)/m).flatten()
