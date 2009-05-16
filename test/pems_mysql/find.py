#!/usr/bin/python
import os
import MySQLdb

def find(key="xiyou"):
	cursor.execute("select * from mybook where path  REGEXP %s",key)
#	cursor.execute("select * from mybook where path like '\%%s\%'",[key])
	for data in cursor.fetchall():
		print '%s\t%s' % data

if __name__ == '__main__' :
	db = MySQLdb.connect(host="localhost", user="root", passwd="112358", db="ebook")
	cursor = db.cursor()
	find('py')
