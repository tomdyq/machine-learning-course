#!/usr/bin/env python
###########################################################################
# Filename: datingkNN.py 
# Author: wanglichen ; Dateime: 2015/03/24
# Description: A simple test for kNN algorithm, calculate error rate
# Version: 0.1
#
###########################################################################
import sys
sys.path.append('/data')
sys.path.append('../../lib/kNN')
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
from kNN import *

def main():
	print 'Start to load data from txt, delimiter = "	"'
	data = genfromtxt('data/datingTestSet.txt', delimiter = '	')
	print 'Get features from txt except last column'
	datingDataMat =  data[:,0:-1] # features
	print 'Get lables from txt which at last colum'
	datingLabels = data[:,-1]     #lables
	print 'There are ', shape(datingDataMat)[1], ' features'
	print 'There are ', shape(datingDataMat)[0], ' examples'
	
	print 'normalize data'
	normMat, ranges, minVals = autoNorm(datingDataMat)
	m = shape(datingDataMat)[0]  #examples number
	
	numTestVecs = int(m * 0.1)   # 10% 
	
	print 'Choose 10% of examples test data to calculate system error rate'
	
	errorCount = 0.0 
	
	print ""
	for i in range(numTestVecs):
		classfierResult = classify(normMat[i,:], normMat[numTestVecs:m,:], datingLabels[numTestVecs:m],3) # k = 3, training by rest of selected example
		print 'The classfier result = %d, the real answer is %d' % (classfierResult, datingLabels[i])
		if (classfierResult != datingLabels[i]): errorCount += 1.0
	print "the total error rate is %f" % (errorCount/float(numTestVecs))  # error rate = errorcount / vector number

if __name__ == '__main__':
	main()
 

