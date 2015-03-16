# For scientific computing
from numpy import *
import scipy
from hypothesis import *

def computeCost(X, y, theta):
	m = len(y)
	term = hypothesis(X, theta) - y
	return (term.T.dot(term) / (2 * m))[0, 0]
	
