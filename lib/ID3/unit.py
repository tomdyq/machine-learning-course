#!/usr/bin/env python
from trees import *

def main():
	myDat, labels = createDataSet()
	myTree = createTree(myDat, labels)
	print myTree
if __name__ == '__main__':
	main()
