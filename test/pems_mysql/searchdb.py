#-*- coding: utf-8 -*-

import os,sys
import MySQLdb
import _mysql_exceptions
db = MySQLdb.connect(host="localhost", user="root", passwd="112358", db="ebook")
cursor = db.cursor()
def visitor(format,dirname,fname):
	for name in fname:
		fpath = os.path.join(dirname,name)
		if os.path.isfile(fpath):
			if os.path.splitext(fpath)[1] in format:
				try:
					cursor.execute("insert into mybook (path,size) values(%s,%s)",[fpath,os.stat(fpath)[6]])
				except _mysql_exceptions.IntegrityError,e:
					pass
#				print >> fp,fpath,str(os.stat(fpath)[6])
#cursor.executemany("insert into python values(%s)",[item[1] for item in enumerate(filelist)])
def searcher(format = ".pdf .chm .doc .odt",path='/'):
	trueformat = format
	truepath=path

	os.path.walk(truepath,visitor,trueformat)
