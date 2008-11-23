#!usr/bin/env python
import os
key=raw_input("Please input the key words of the Ebook's name: ")
def find(key):
<<<<<<< .mine
	count=0
	for line in fp.readlines():
        	if key in line:
	    		count+=1
            		print line
	if count==0:
        	print "Sorry,the book doesn't exist!"
=======
	count=0
	for line in fp.readlines():
		if key in line:
			count+=1
			print line
	if count==0:
		print "Sorry,the book doesn't exist!"
>>>>>>> .r7
if __name__=='__main__':
<<<<<<< .mine
    	fp=open("list.list","r")
    	find(key)
    	fp.close()
=======
	fp=open("list.list","r")
	find(key)
	fp.close()
>>>>>>> .r7
