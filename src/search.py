#-*- coding: utf-8 -*-

import os,sys



def visitfile(fname,format):
	if os.path.splitext(fname)[1] in format:
		fp = open("list.list",'a')
		print >> fp,fname
		fp.close()

def visitor(arg,dirname,fname):
	for name in fname:
		fpath = os.path.join(dirname,name)
		if not os.path.isdir(fpath):
			visitfile(fpath,arg)
#			if format in os.path.splitext(fname)[1]:
#				print >> fp,fname


def searcher(path, format):
	
	os.path.walk(path,visitor,format)



if __name__ == '__main__' :
	fp = file("list.list",'w')
	searcher(path)
	fp.close()

