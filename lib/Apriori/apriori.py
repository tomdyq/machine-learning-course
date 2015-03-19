#!/usr/bin/env python

import sys
from numpy import *

def loadDataSet():
	return [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]

def createC1(dataset):
	C1 = []
	for transaction in dataset:
		for item in transaction:
			if not [item] in C1:
				C1.append([item])
	C1.sort()
	return map(frozenset, C1)

def scanD(D, Ck, minSupport):
	ssCnt = {}
	for tid in D:
		for can in Ck:
			if can.issubset(tid):
				if not ssCnt.has_key(can): 
					ssCnt[can] = 1
				else:
					ssCnt[can] += 1
		
	tran_nums = float(len(D))
	
	retList = []
	supportData = {}
	
	for key in ssCnt:
		support_cur = ssCnt[key]/tran_nums
		if support_cur >= minSupport:
			retList.insert(0, key)
		supportData[key] = support_cur
	return retList, supportData 
	

