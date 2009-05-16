# -*- encoding: utf-8 -*-
# Just some simple data structures for the report mode listctrl examples
import os
import MySQLdb
import _mysql_exceptions
db = MySQLdb.connect(host="localhost", user="root", passwd="112358", db="ebook")
cursor = db.cursor()
columns = ["电子书名称","电子书大小","电子书所在路径"]
cursor.execute("select * from mybook")
rows=[(os.path.splitext(os.path.basename(datarow[0]))[0],datarow[1],datarow[0]) for datarow in cursor.fetchall()]
#if os.path.isfile('all.list'):
#    f = open('all.list','r')
#    rows=[(os.path.splitext(os.path.basename(line.split('        ')[0]))[0], line.split('        ')[1],line.split('        ')[0])for line in f]
#    f.close()
#else:
#    f = open('all.list','w')
#    rows=[]
#    f.close()
#cursor.execute("create table new (path char(255),size char(15),primary key path)")
#CREATE TABLE `mybook` (`path` char(255) NOT NULL,`size` char(15) NOT NULL,PRIMARY KEY  (`path`))
