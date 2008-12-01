#!/usr/bin/env python

#-*- coding: utf-8 -*-
import os

def add2group():
	dir=raw_input('please input the name of new group:')
	p=open(dir,'a')
	f=open('list.list','r')
	filename=raw_input('please input the filename you want to add to the group:')
	for line in f.readlines():
		if filename in os.path.splitext(os.path.basename(line))[0]:
			p.write(line)
		else :
			print 'no file name %s' % filename
	p.close()
	f.close()

if __name__=='__main__':
	add2group()
