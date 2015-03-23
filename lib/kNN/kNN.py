#!/usr/bin/env python

from numpy import *
import operator

def createDataSet():
	dataSet = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A', 'A', 'B', 'B']
	return dataSet, labels
	
def classify0(intX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0]
	diffMat = tile(intX, (dataSetSize,1)) - dataSet
	sqDiffMat = diffMat**2
	sqDistance = sqDiffMat.sum(axis=1) # sum each row
	distances = sqDistance**0.5
	sortedDistIndicies = distances.argsort() # indices of sorted array using quick sort
	print sortedDistIndicies

	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) +1
 	sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]

def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals;
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	
	normDataSet = dataSet - tile(minVals, (m,1))
	normDataSet = normDataSet/tile(ranges, (m,1))
	return normDataSet, ranges, minVals
	
#def main():
#	data, label = createDataSet()
#	print data
#	print label
#	
#	print classify0([0,0], data, label, 3)

#if __name__ == '__main__':
#	main()

