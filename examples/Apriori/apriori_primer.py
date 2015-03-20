#!/usr/bin/env python

import sys
sys.path.append('../../lib/Apriori')
from numpy import *
from apriori import *

def main():
	dataset = loadDataSet()
	print dataset

	L, suppData = apriori(dataset)
	print L
	
	bigRuleList = generateRules(L, suppData, 0.5)
	
	
if __name__ == '__main__':
	main()
