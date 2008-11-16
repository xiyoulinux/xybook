#!usr/bin/env python
import os
key=raw_input("Please input the key words of the Ebook's name: ")
def find(key):
 count=0
 for line in fp.readlines():
	if key in line:
	   count+=1
           print line
 if count==0:
    print "Sorry,the book doesn't exist!"
if __name__=='__main__':
 fp=open("list.txt","r")
 find(key)
 fp.close()
