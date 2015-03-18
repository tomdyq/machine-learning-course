#!/usr/bin/env python

import scipy.optimize, scipy.special
from numpy import *

def optimize_gradient(costFunction, X, y, theta, iterator, output_status):
	result = scipy.optimize.fmin(costFunction, x0=theta, args = (X, y), maxiter=iterator, full_output=output_status)
	return result[0], result[1]
	
