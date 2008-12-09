# -*- encoding: utf-8 -*-
# Just some simple data structures for the report mode listctrl examples
import os
columns = ["电子书名称","电子书大小","电子书所在路径"]
f = open('list.list','r')
rows=[(os.path.splitext(os.path.basename(line.split('        ')[0]))[0], line.split('        ')[-1],line.split('        ')[0])for line in f]
f.close()
