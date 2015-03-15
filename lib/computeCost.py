# For scientific computing
from numpy import *
import scipy

def computeCost(X, y, theta):
	m = len(y)
	hypo = X.dot(theta)
	term = hypo - y
	return term.T.dot(term) / (2*m)
	
