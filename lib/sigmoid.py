#!/usr/bin/env python

from numpy import *

def sigmoid(z):
	return 1.0/(1.0 + exp(-z))
