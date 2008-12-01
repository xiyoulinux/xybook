#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import shutil
import os.path

#src = ['/media/DATA/ebook/shell与基础/A Practical Guide to Linux Commands Editors and Shell Programming.chm','/media/DATA/ebook/shell与基础/《LINUX与UNIX SHELL编程指南》.pdf']
#dst = "/media/DATA/"


def move():

#if __name__ == '__main__' :
	src=[]

	f = open('list.list','r')
	alllines=f.readlines()
	f.seek(0,0)
	booklist=[os.path.splitext(os.path.basename(line))[0] for line in f]
	f.close()

	while True:
		key=raw_input('请输入你要转移的文件的文件名(输入.结束):').strip()
		if key=='.':
			break
#		if key in booklist:
#			src.append(key)
#		else:
#			print '没有这本书，请重新输入'
		for item in booklist:#判断书是否在列表中，模糊匹配
			if key in item:
				bookdict={}
				n=1
				for line in alllines:
					if key in os.path.splitext(os.path.basename(line))[0]:
						print '%d.%s'%(n,line),
						bookdict[n]=line
						n+=1
				if n==1:
					print '没有这本书，请重新输入'
				if n==2:
					src.append(bookdict[1][:-1])
					print '已经添加'
				else:
					no=raw_input('上面是搜索到的可能有您想要得书，请输入编号(若没有请输入0):')
					if int(no)==0:
						continue
					elif 0<int(no)<n:
						print '你选择了《%s》' %(bookdict[int(no)][:-1])
						src.append(bookdict[int(no)][:-1])
						print '《%s》已经添加' %(bookdict[int(no)][:-1])
					else :
						continue
#				break
#			else:
#				print '没有这本书，请重新输入'

	dst=raw_input('请输入目的目录：').strip()
#	move(src,dst)
	sum = 0L
	moved = 0L
	for fname in src:
		if os.path.isfile(fname):
			sum += os.path.getsize(fname)
		else:
			print '文件%s不存在，已经略过' %(os.path.basename(fname))
	print '要转移的文件总大小为%d' % sum
	for fname in src:
		if os.path.isfile(fname):
			moved += os.path.getsize(fname)
			shutil.move(fname,dst)
			print '文件《%s》已经转移已经转移大小为%s占所有文件总量的%d%%' %(os.path.splitext(os.path.basename(fname))[0],moved,int(100*moved/sum))

if __name__ == '__main__' :
	move()
