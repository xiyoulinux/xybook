#!/usr/bin/python
import os
key=raw_input("xiyou")
def find(key="xiyou"):
	for line in fp.readlines():
		if key in line :
			print line 
if __name__ == '__main__' :
	fp=open("list.list",'r')
	find(key)
	fp.close()  
