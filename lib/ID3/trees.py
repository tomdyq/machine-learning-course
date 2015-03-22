from math import log

def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet:
		currentLabel = featVec[-1]
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1
	
	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key]) / numEntries
		shannonEnt -= prob * log(prob,2)
	return shannonEnt
def createDataSet():
	dataSet = [[1,1,'yes'], [1,1,'yes'],[1,0,'no'], [0,1,'no'], [0,1,'no']]
	return dataSet	

def splitDataSet(dataSet, axis, value):
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet

def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet[0]) -1
	baseEntroy = calcShannonEnt(dataSet)
	bestInfoGain = 0.0;
	bestFeature = -1
	
	for i in range (numFeatures):
		featList = [example[i] for example in dataSet]
		uniqueVals = set(featList)
		newEntroy = 0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet, i, value)
			prob = len(subDataSet)/float(len(dataSet))
			newEntroy += prob * calcShannonEnt(subDataSet)
		
		infoGain = baseEntroy - newEntroy
		if (infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i
	return bestFeature

	
