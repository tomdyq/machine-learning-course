#!/usr/bin/env python

from numpy import *

#####################################################
# FunctionName: sigmoid 
# Author: wanglichen
# Desciption: sigmoid function
#
####################################################
def sigmoid(z):
	return 1.0/(1.0 + exp(-z))
