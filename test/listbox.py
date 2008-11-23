#!/usr/bin/env python
#-*- coding: utf-8 -*-
from Tkinter import *
import os

root = Tk()
#root.option_readfile('optionDB')
root.title('Listbox')
list = Listbox(root, width=100,height=100)
scroll = Scrollbar(root, command=list.yview)
list.configure(yscrollcommand=scroll.set)
list.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)
f=open('list.list','r')
for line in f.readlines():
	list.insert(END, os.path.splitext(os.path.basename(line))[0])
f.close()
root.mainloop()
