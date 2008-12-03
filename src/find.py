#!/usr/bin/python
import os

fp = open("list.list", 'r')

def keyfind(key="xiyou"):
	for line in fp.readlines():
		if key in line :
			print line 
	fp.close()
if __name__ == '__main__' :
	fp=open("list.list",'r')
	find(key)
	fp.close()  
