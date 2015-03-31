#For plotting
#!/usr/bin/env python

from matplotlib import pyplot,cm
from mpl_toolkits.mplot3d import Axes3D

##########################################################
# FunctionName: plot
# Author: wanglichen
# Description: plot the ex1data1.txt 
#
##########################################################
def plot(X,y):
	pyplot.plot(X, y, 'rx', markersize=5)
	pyplot.ylabel('Profit in $10,000s')
	pyplot.xlabel('Population of City in 10,000s')
#	pyplot.show(block=True)
