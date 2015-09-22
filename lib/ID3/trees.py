#!/usr/bin/env python
###########################################################################
# Filename: ID3.py
# Author: wanglichen; Datetime: 2015/03/25
# Description: Decision tree lib
# Version: 0.1
#
###########################################################################
from math import log
import operator
##########################################################################
# Function: calcShannonEnt
# Description: calculate Shannon entropy value
# Input: [[feature1, feature2 ..., label1 ],[],[]] 
# Output: floatShannon entropy value
#
#########################################################################
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
###########################################################################
# Function: createDataSet
# Input: nil
# Output: [[f1,f2,label1], [f1,f2,label2]], labels
# 
##########################################################################
def createDataSet():
	dataSet = [[1,1,'yes'], [1,1,'yes'],[1,0,'no'], [0,1,'no'], [0,1,'no']]
	labels = ['no surfacing', 'flippers']
	return dataSet, labels	
##########################################################################
# Function: splitDataSet
# Description: Extract specific value(value) of specific feature(axis) from
# dataSet
# Input: dataSet, axis, value
# Output: extract dataset
#
##########################################################################
def splitDataSet(dataSet, axis, value):
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet
##########################################################################
# Function: chooseBestFeatureToSplit
# Desciption: choose the feature which has larget entropy value
# Input: datasSet
# Output: feature
##########################################################################
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

###################################################################################################
# Function: majorityCnt
# Description: return the most frequent features in classlist
# Input: classlist 
# Output: feature
####################################################################################################
def majorityCnt(classList):
	classCount = {}
	for vote in classList:
		if vote not in classCount.keys(): classCount[vote] = 0
		classCount[vote] += 1
	
	#sort class count from large to small
	sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse=True) 
	return sortedClassCount[0][0]	# return larget
####################################################################################################
# Function: createTree
# Description:  create tree stored in dictionary 
# Input: dataset, label
# Output: tree
#
####################################################################################################
def createTree(dataSet, labels):
	classList = [example[-1] for example in dataSet]
	# classify are all the same, stop split
	if classList.count(classList[0]) == len(classList):
		return classList[0]
	if len(dataSet[0]) == 1:
		return majorityCnt(classList)
	bestFeat = chooseBestFeatureToSplit(dataSet)
	bestFeatLabel = labels[bestFeat]
	myTree = {bestFeatLabel:{}}
	del(labels[bestFeat])  
	featValues = [example[bestFeat] for example in dataSet]
	uniqueVals = set(featValues)
	for value in uniqueVals:
		subLabels = labels[:]
		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
	return myTree
