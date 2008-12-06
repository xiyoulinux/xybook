#-*- coding: utf-8 -*-

import os,sys



def visitfile(fname,format):
	if format in os.path.splitext(fname)[1]:		
		print >> fp,fname
		

def visitor(arg,dirname,fname):
	for name in fname:
		fpath = os.path.join(dirname,name)
		if not os.path.isdir(fpath):
			visitfile(fpath,arg)
#			if format in os.path.splitext(fname)[1]:
#				print >> fp,fname


def searcher(path, format):
	fp = open("list.list",'a')
	os.path.walk(path,visitor,format)
	fp.close()


if __name__ == '__main__' :
	fp = file("list.list",'w')
	searcher(path)
	fp.close()
