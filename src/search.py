#-*- coding: utf-8 -*-

import os,sys
import string



def visitfile(fname,format):
	#print os.path.splitext(fname)[1].translate(unknow, '.') 
	unknow = string.maketrans('','')
	loop = '.'
	if os.path.splitext(fname)[1].translate(unknow,loop) in format :
		print >> fp,fname
		

def visitor(arg,dirname,fname):
	for name in fname:
		fpath = os.path.join(dirname,name)
		if not os.path.isdir(fpath):
			visitfile(fpath,arg)
			


def searcher(path, format):
	fp = open("list.list",'w')
	os.path.walk(path,visitor,format)
	fp.close()
	


if __name__ == '__main__' :
	fp = open("list.list",'w')
	searcher(path)
	fp.close()
