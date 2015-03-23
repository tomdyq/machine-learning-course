#!/usr/bin/env python
import sys
sys.path.append('/data')
sys.path.append('../../lib/kNN')
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
from kNN import *

def main():
#	print 'Start to load data from txt, delimiter = "	"'
	data = genfromtxt('data/datingTestSet.txt', delimiter = '	')
	datingDataMat =  data[:,0:-1] # features
	datingLabels = data[:,-1]     #lables
	
#	plot data
#	fig = plt.figure()
#	ax = fig.add_subplot(111)
#	ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15.0*array(datingLabels), 15.0*array(datingLabels))
#	plt.show()
	
	normMat, ranges, minVals = autoNorm(datingDataMat)
	print ranges
	print minVals	
	
if __name__ == '__main__':
	main()
 

