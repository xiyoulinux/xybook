#-*- coding: utf-8 -*-

import os,sys

format = ['.pdf','.chm']
path = "/media/DATA/ebook"

def visitfile(fname):
	if os.path.splitext(fname)[1] in format:
		print >> fp,fname+'          '+str(os.lstat(fname)[6])

def visitor(arg,dirname,fname):
	for name in fname:
		fpath = os.path.join(dirname,name)
		if not os.path.isdir(fpath):
			visitfile(fpath)

def searcher(path):
	os.path.walk(path,visitor,"")

if __name__ == '__main__' :
	fp = file("list.list",'w')
	searcher(path)
	fp.close()
