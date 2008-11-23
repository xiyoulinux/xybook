#!/usr/bin/env python
#-*- coding: utf-8 -*-
from Tkinter import *
import os

root = Tk()
#root.option_readfile('optionDB')
root.title('Listbox')
list = Listbox(root, width=30,height=50)
scroll = Scrollbar(root, command=list.yview)
list.configure(yscrollcommand=scroll.set)
list.pack(side=LEFT)
scroll.pack(side=RIGHT, fill=Y)

for item in os.listdir(os.getcwd()):
	if os.path.splitext(item)[1] in ('.list',):
		list.insert(END,item)
root.mainloop()
