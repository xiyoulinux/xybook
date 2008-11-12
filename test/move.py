#-*- coding: utf-8 -*-

import os

from os.path import join,getsize

src = ['/root/pdf/1.pdf','/root/pdf/2.pdf']
dst = "/home/python"

def mv(src,dst):
	for fname in src:
		cmd=' '.join(['mv',fname,dst])
		os.system(cmd)

def move(src,dst):
	sum = 0L
	for fname in src:
		sum += getsize(fname)
		print sum
	mv(src,dst)


if __name__ == '__main__' :
	move(src,dst)
