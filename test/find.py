#!usr/bin/env python
import os
key="xiyou"
def find(key):
for line in fp.readlines():
    if key in line :
    print line 
if __name__ == '__main__' :
fp=open("list.list",'r')
find(key)
fp.close()  
