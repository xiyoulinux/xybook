# -*- encoding: utf-8 -*-
# Just some simple data structures for the report mode listctrl examples
import os
columns = ["BookName","Size","CreateDate","BookDir"]
f = open('list.list','r')
rows=[(os.path.splitext(os.path.basename(line))[0],line)for line in f]
f.close()
