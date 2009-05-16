# -*- encoding: utf-8 -*-
import os
import os.path
import wx
def sort():
        f = open('all.list','r')
        alllines=f.readlines()
        f.close()
        pdf=open('pdf.list','w')
        doc=open('doc.list','w')
        chm=open('chm.list','w')
        other=open('other.list','w')        
        for line in alllines:
            if 'pdf' in  os.path.splitext(os.path.basename(line.split('        ')[0]))[1]:
                pdf.write(line)
            elif 'chm' in os.path.splitext(os.path.basename(line.split('        ')[0]))[1]:
                chm.write(line)
            elif 'doc' in os.path.splitext(os.path.basename(line.split('        ')[0]))[1]:
                doc.write(line)
            else:
                other.write(line)           
        else:
            wx.MessageBox("分类成功！！！")
        pdf.close()
        chm.close()
        doc.close()
        other.close()
