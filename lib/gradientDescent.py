#For scientific computing

from numpy import *
import scipy

from hypothesis import hypothesis
def gradientDescent(X, y, theta, alpha, iterations):
	grad = copy(theta)
	m = len(y)
	for counter in range(0, iterations):
		inner_sum = X.T.dot(hypothesis(X, grad) - y)
		grad -= alpha / m * inner_sum
	return grad
