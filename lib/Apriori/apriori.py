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

def aprioriGen(Lk, k):
	retList = []
	lenLk = len(Lk)

	for i in range(lenLk):
		for j in range(i+1, lenLk):
			L1 = list(Lk[i+1])[:k-2]; L2 = list(Lk[j])[:k-2]
			L1.sort(); L2.sort()
			if L1 == L2:
				retList.append(Lk[i] | Lk[j])
	return retList

def apriori(dataSet, minSupport = 0.5):
	C1 = createC1(dataSet)
	D = map(set, dataSet)
	L1, supportData = scanD(D, C1, minSupport)
	L = [L1]	
	k = 2
	while (len(L[k-2]) >0):
		Ck = aprioriGen(L[k-2], k)
		Lk, supK = scanD(D, Ck, minSupport)	
		supportData.update(supK)
		L.append(Lk)
		k += 1
	return L, supportData
	
		

