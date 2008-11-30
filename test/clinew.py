#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import os.path
import os.path


format = ['.pdf','.chm']

#增加文件到分组列表
def add2group():
	dir=raw_input('please input the name of new group:')
	p=open(dir,'a')
	f=open('list.list','r')
	filename=raw_input('please input the filename you want to add to the group:')
	for line in f.readlines():
		if filename in os.path.splitext(os.path.basename(line))[0]:
				p.write(line)
	p.close()
	f.close()


#删除文件
def delete():
	pass

#查找某一个特定的文件
def find():
	key=raw_input("Please input the key words of the Ebook's name: ")
	fp=open('list.list','r')
	count=0
	for line in fp.readlines():
		if key in line:
			count+=1
			print line,
	if count==0:
		print "Sorry,the book doesn't exist!"
	fp.close()




#按照文件的后缀名分组
def sortbytype():
	f = open('list.list','r')
	alllines=f.readlines()
	f.close()
	pdf=open('pdf.list','w')
	doc=open('doc.list','w')
	chm=open('chm.list','w')
	other=open('other.list','w')
	for line in alllines:
		if 'pdf' in os.path.splitext(line)[1]:
			pdf.write(line)
			
		elif 'chm' in os.path.splitext(line)[1]:
			chm.write(line)
		
		elif 'doc' in os.path.splitext(line)[1]:
			doc.write(line)
		
		else:
			other.write(line)
	else:
		print '分类成功！！！'
	pdf.close()
	chm.close()
	doc.close()
	other.close()






#移动
def move():

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
		if key in booklist:
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
		else:
			print '没有这本书，请重新输入'

	dst=raw_input('请输入目的目录：').strip()
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




#搜索计算机中的电子书


def visitfile(fname):
	fp = file("list.list",'a')
	if os.path.splitext(fname)[1] in format:
		print >> fp,fname
	fp.close()

def visitor(arg,dirname,fname):
	for name in fname:
		fpath = os.path.join(dirname,name)
		if not os.path.isdir(fpath):
			visitfile(fpath)

def searcher(path="/"):
	os.path.walk(path,visitor,"")

#if __name__ == '__main__' :
#	fp = file("list.list",'w')
#	searcher(path)
#	fp.close()






def showmenu():
	promet="""
	(S)earch ebook on disk  在磁盘上搜索电子书
	(F)ind in the list      在列表中查找电子书
	s(O)rt by type          按照文件类型给电子书分类
	(A)dd to group          增加电子书到某一分类
	(M)ove                  转移
	(Q)uit                  退出
	Enter your choice:"""


	done=False
	while not done:

		chosen=False
		while not chosen:
			try:

				choice=raw_input(promet).strip()[0].lower()
			
			except (EOFError,KeyboardInterrupt):
				choice='q'

			print '\n你选择了:[%s]' % choice

			if choice not in 'sfoamq':
				print '输入错误，重新输入'
			else:
				chosen=True

		if choice=='q':
			done=True
			break	
		if choice=='s':
			path=raw_input('请输入您要搜索的路径（默认为根/）:')
			searcher(path)
		if choice=='f':
			find()
		if choice=='o':
			sortbytype()
		if choice=='a':
			add2group()
		if choice=='m':
			move()


if __name__=='__main__':
	showmenu()
