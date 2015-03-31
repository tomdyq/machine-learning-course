#!/usr/bin/env python
#For scientific computing
from numpy import *
import scipy
#########################################################
# FunctionName: hypothesis
# Author: wanglichen
# Description: compute hypothesis; X * theta
#
#########################################################
def hypothesis(X, theta):
	return X.dot(theta)

