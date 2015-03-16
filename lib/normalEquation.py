#Std python modules
import sys
#For scientific computing
from numpy import *
import scipy

def normalEquation(X, y):
	return linalg.inv(X.T.dot(X)).dot(X.T).dot(y)
