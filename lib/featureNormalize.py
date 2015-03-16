#For scientific computing
import sys
from numpy import *
import scipy

def featureNormalize(data):
	mu = mean(data, axis=0)
	data_norm = data - mu
	sigma = std(data_norm, axis=0, ddof=1)
	data_norm = data_norm / sigma
	return data_norm, mu, sigma
