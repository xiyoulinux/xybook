#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import wx.grid
import os
import os.path
from os.path import join
import sys, glob, random
import data
import shutil
import time
import MySQLdb
import _mysql_exceptions
import searchdb
class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        #启动画面splash
        RunPicture = wx.Image("./picture/run.png").ConvertToBitmap()
        wx.SplashScreen(RunPicture, wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT,1000, None, -1)
        wx.Yield()
        wx.Frame.__init__(self, *args, **kwds)
        # Tool Bar
        self.vToolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.vToolbar)
        vTidy = self.vToolbar.AddLabelTool(wx.NewId(), "整理", wx.Bitmap("./picture/tidy.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        vSortbytype = self.vToolbar.AddLabelTool(wx.NewId(), "按文件类型分组", wx.Bitmap("./picture/sort.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        vAbout = self.vToolbar.AddLabelTool(wx.NewId(), "关于", wx.Bitmap("./picture/about.png", wx.BITMAP_TYPE_ANY),wx.NullBitmap, wx.ITEM_NORMAL, "", "")
        # Tool Bar end
        self.vStaticPath = wx.StaticText(self, -1, u"路径", style=wx.ALIGN_CENTER)
        self.vStaticPath.SetFont(wx.Font(15, wx.DECORATIVE , wx.BOLD, wx.NORMAL))
        self.vBeginDir = wx.Button(self, -1, u"选择文件夹")
        self.vInputPath = wx.TextCtrl(self, -1, "/")
        self.vStaticType = wx.StaticText(self, -1, u"类型\n",style=wx.ALIGN_CENTER)
        self.vStaticType.SetFont(wx.Font(15, wx.DECORATIVE , wx.BOLD, wx.NORMAL))
        self.vInputType = wx.TextCtrl(self, -1, "pdf chm odt doc")
        self.vBeginSearch = wx.Button(self, -1, u"开始搜索")
        self.vStaticKey = wx.StaticText(self, -1, u"请输入关键字",style=wx.ALIGN_CENTER)
        self.vStaticKey.SetFont(wx.Font(15, wx.DECORATIVE , wx.BOLD, wx.NORMAL))
        self.vInputKey = wx.TextCtrl(self, -1, "")
        self.vBeginFind = wx.Button(self, -1, u"搜索关键字")
#        self.vLeftListBox = wx.ListBox(self, -1, choices=[os.path.splitext(item)[0] for item in os.listdir(os.getcwd()) if os.path.splitext(item)[1] in ('.list',)]) 
        cursor.execute("show tables")
        self.vLeftListBox = wx.ListBox(self, -1, choices=[dataer[0] for dataer in cursor.fetchall()])
        #listctrl
        il = wx.ImageList(16,16, True)
        for name in glob.glob("./picture/smicon??.png"):
            RunPicture = wx.Bitmap(name, wx.BITMAP_TYPE_PNG)
            il_max = il.Add(RunPicture)
        self.RightCtrl = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
        self.RightCtrl.AssignImageList(il, wx.IMAGE_LIST_SMALL)
        for col, text in enumerate(data.columns):
            self.RightCtrl.InsertColumn(col, text)
        for item in data.rows:
            index = self.RightCtrl.InsertStringItem(sys.maxint, item[0])
            for col, text in enumerate(item[1:]):
                self.RightCtrl.SetStringItem(index, col+1, text)
            img = random.randint(0, il_max)
            self.RightCtrl.SetItemImage(index, img, img)
        self.RightCtrl.SetColumnWidth(0, 150)
        self.RightCtrl.SetColumnWidth(1, 150)
        self.RightCtrl.SetColumnWidth(2, 150)
        #end listctrl

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TOOL, self.Tidy, vTidy)
        self.Bind(wx.EVT_TOOL, self.Sortbytype, vSortbytype)
        self.Bind(wx.EVT_TOOL, self.About, vAbout)
        self.Bind(wx.EVT_BUTTON, self.Search, self.vBeginSearch)
        self.Bind(wx.EVT_BUTTON, self.ChooseDir, self.vBeginDir)
        self.Bind(wx.EVT_BUTTON, self.Find, self.vBeginFind)
        self.Bind(wx.EVT_CONTEXT_MENU, self.ListRightButton, self.vLeftListBox)
        self.Bind(wx.EVT_LISTBOX, self.ButtonClick, self.vLeftListBox)
        self.RightCtrl.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)
        # end wxGlade

    def __set_properties(self):
        self.SetTitle("Python e-book Management System")
        self.SetSize((900, 650))
        self.vToolbar.Realize()
        # end wxGlade

    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(self.vStaticPath, 1, wx.EXPAND, 0)
        sizer_4.Add(self.vInputPath, 4, wx.EXPAND, 0)
        sizer_4.Add(self.vBeginDir, 2, wx.EXPAND, 0)
        sizer_4.Add(self.vStaticType, 1, wx.EXPAND, 0)
        sizer_4.Add(self.vInputType, 6, wx.EXPAND, 0)
        sizer_4.Add(self.vBeginSearch, 2, wx.ALL|wx.EXPAND, 0)
        sizer_2.Add(sizer_4, 1, wx.EXPAND, 5)
        sizer_5.Add(self.vStaticKey, 3, wx.EXPAND, 0)
        sizer_5.Add(self.vInputKey, 15, wx.EXPAND, 0)
        sizer_5.Add(self.vBeginFind, 2, wx.EXPAND, 0)
        sizer_2.Add(sizer_5, 1, wx.EXPAND, 5)
        sizer_3.Add(self.vLeftListBox, 1, wx.EXPAND, 0)
        sizer_3.Add(self.RightCtrl, 4, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 20, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def ButtonClick(self, event):
        n=self.vLeftListBox.GetSelection()
        cursor.execute("show tables")
        sampleList = [dataer[0] for dataer in cursor.fetchall()]
#        f = open(sampleList[n],'r')
        cursor.execute("select * from `%s`"%sampleList[n])
#        data.rows=[(os.path.splitext(os.path.basename(line.split('        ')[0]))[0], line.split('        ')[-1],line.split('        ')[0])for line in f]
        data.rows=[(os.path.splitext(os.path.basename(datarow[0]))[0],datarow[1],datarow[0]) for datarow in cursor.fetchall()]
#        f.close()
        #listctrl
        self.RightCtrl.Destroy()#销毁之前的窗口
        il = wx.ImageList(16,16, True)#随机显示图片
        for name in glob.glob("./picture/smicon??.png"):
            RunPicture = wx.Bitmap(name, wx.BITMAP_TYPE_PNG)
            il_max = il.Add(RunPicture)
        self.RightCtrl = wx.ListCtrl(self, -1, style=wx.LC_REPORT)#建立右边窗体
        self.RightCtrl.AssignImageList(il, wx.IMAGE_LIST_SMALL)#定义窗体显示类型
        self.__do_layout()#重新加载窗体布局
        for col, text in enumerate(data.columns):
            self.RightCtrl.InsertColumn(col, text)
        for item in data.rows:
            index = self.RightCtrl.InsertStringItem(sys.maxint, item[0])
            for col, text in enumerate(item[1:]):
                self.RightCtrl.SetStringItem(index, col+1, text)
            img = random.randint(0, il_max)
            self.RightCtrl.SetItemImage(index, img, img)                
        self.RightCtrl.SetColumnWidth(0, 150)
        self.RightCtrl.SetColumnWidth(1, 150)
        self.RightCtrl.SetColumnWidth(2, 150|wx.LIST_AUTOSIZE)
        self.RightCtrl.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)
        event.Skip()
       #选择目录
    def ChooseDir(self,event):
        dialog = wx.DirDialog(None, "Choose a directory:",style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.vInputPath = wx.TextCtrl(self, -1, dialog.GetPath())#将选择的路径现示在左边的窗体中
            self.__do_layout()

      #右键菜单
    def OnContextMenu(self, event):
        menu = wx.Menu()
        itemopenitem  = wx.MenuItem(menu, wx.NewId(), "打开文件")
        menu.AppendItem(itemopenitem)
        self.Bind(wx.EVT_MENU, self.Open,itemopenitem)
        itemopenitemDir  = wx.MenuItem(menu, wx.NewId(), "打开文件夹")
        menu.AppendItem(itemopenitemDir)
        self.Bind(wx.EVT_MENU, self.openDir,itemopenitemDir)
        itemdetail = wx.MenuItem(menu, wx.NewId(), "详细信息")
        menu.AppendItem(itemdetail)
        itemmoveitem = wx.MenuItem(menu, wx.NewId(), '移动')
        menu.AppendItem(itemmoveitem)
        self.Bind(wx.EVT_MENU, self.Move, itemmoveitem)
        itemaddtolist=wx.MenuItem(menu, wx.NewId(), '增加到组')
        menu.AppendItem(itemaddtolist)
        itemdeleteitem=wx.MenuItem(menu, wx.NewId(), '删除此项')
        menu.AppendItem(itemdeleteitem)        
        
        self.itemid = self.RightCtrl.GetFirstSelected()
        if self.itemid == -1:#如果没有选中任何项
            itemdetail.Enable(False)
            itemopenitem.Enable(False)
            itemopenitemDir.Enable(False)
            itemmoveitem.Enable(False)
            itemaddtolist.Enable(False)
            itemdeleteitem.Enable(False)
        else:
            itemdetail.Enable(True)
            itemopenitem.Enable(True)
            itemopenitemDir.Enable(True)
            itemmoveitem.Enable(True)
            itemaddtolist.Enable(True)
            itemdeleteitem.Enable(True)
        #弹出菜单
        self.Bind(wx.EVT_MENU, self.Detail, itemdetail)
        self.Bind(wx.EVT_MENU, self.addtolist,itemaddtolist)
        self.Bind(wx.EVT_MENU, self.Deleteitem,itemdeleteitem)
        self.PopupMenu(menu)
        #最后销毁前面创建的菜单
        menu.Destroy()
        event.Skip()

    def Detail(self,event):
        st = os.stat(data.rows[self.itemid][2])
        wx.MessageBox("路径:%s\n大小:%dbytes     %fMbytes\n属主:%s  %s\n创建时间:%s\n最后访问:%s\n最后修改:%s"% (data.rows[self.itemid][2],st.st_size,st.st_size*1.0/1048576.0,st.st_uid,st.st_gid,time.ctime(st.st_ctime),time.ctime(st.st_atime),time.ctime(st.st_mtime)))
    def Deleteitem(self,event):
        if os.path.isfile(data.rows[self.itemid][2]):
            os.remove(data.rows[self.itemid][2])
            self.RightCtrl.DeleteItem(self.itemid)
            wx.MessageBox("删除成功")
        else:
            wx.MessageBox("文件不存在，请刷数据库")
            self.RightCtrl.DeleteItem(self.itemid)
    def addtolist(self,event):
        dialog = wx.TextEntryDialog(None,"请输入列表名","增加到列表","",style=wx.OK|wx.CANCEL)
        if dialog.ShowModal()==wx.ID_OK:
            try:
                cursor.execute("CREATE TABLE `%s` (`path` char(255) NOT NULL,`size` char(15) NOT NULL,PRIMARY KEY (`path`))"%dialog.GetValue())
            except _mysql_exceptions.OperationalError,e:
                pass
            cursor.execute("insert into `%s` (path,size) values(`%s`,`%s`)"%(dialog.GetValue(),data.rows[self.itemid][2],os.stat(data.rows[self.itemid][2])[6]))
            ##########此处后面传进的参数不能用［］，要使用（），不明白为什么？
#            name= dialog.GetValue()+".list"


#        if os.path.isfile(name):
#            f=open(name,'a')
#            f.write(data.rows[self.itemid][2]+'          '+str(os.stat(data.rows[self.itemid][2])[6])+'\n')
#            f.close()
#        else:
#            f=open(name,'w')
#            f.write(data.rows[self.itemid][2]+'          '+str(os.stat(data.rows[self.itemid][2])[6])+'\n')
#            f.close()
        self.vLeftListBox.Destroy()#销毁之前的窗口
        cursor.execute("show tables")
        self.vLeftListBox = wx.ListBox(self, -1, choices=[dataer[0] for dataer in cursor.fetchall()])
#        self.vLeftListBox = wx.ListBox(self, -1, choices=[os.path.splitext(item)[0] for item in os.listdir(os.getcwd()) if os.path.splitext(item)[1] in ('.list',)])
        self.__do_layout()#重新加载窗体布局
        self.Bind(wx.EVT_CONTEXT_MENU, self.ListRightButton, self.vLeftListBox)
        self.Bind(wx.EVT_LISTBOX, self.ButtonClick, self.vLeftListBox)
        event.Skip()

    def openDir(self,event):
        cmd=str('xdg-open'+' '+'\''+os.path.split(data.rows[self.itemid][2])[0]+'\'')
        os.system(cmd)


    def Open(self,event):
        cmd=str('xdg-open'+' '+'\''+data.rows[self.itemid][2]+'\'')
        os.system(cmd)
        event.Skip()

    def Move(self,event):
        self.dialog = wx.TextEntryDialog(None,"请输入目的路径","文件移动",os.path.expanduser('~/'),style=wx.OK|wx.CANCEL)
        if self.dialog.ShowModal()==wx.ID_OK:
            dstname = self.dialog.GetValue().encode("utf-8").replace("\n","") + "/"
            if "/" not in dstname:
                wx.MessageBox("请输入绝对路径")
            if os.path.isfile(dstname+os.path.basename(data.rows[self.itemid][2].replace("\n",""))):
                wx.MessageBox("目的文件已存在")
            else:
                shutil.move(data.rows[self.itemid][2], dstname)
        event.Skip()

    def Sortbytype(self,event):
        cursor.execute("select * from mybook")
        datalines=cursor.fetchall()
        try:
            cursor.execute("CREATE TABLE pdf (`path` char(255) NOT NULL,`size` char(15) NOT NULL,PRIMARY KEY (`path`))")
        except _mysql_exceptions.OperationalError,e:
            pass
        try:
            cursor.execute("CREATE TABLE doc (`path` char(255) NOT NULL,`size` char(15) NOT NULL,PRIMARY KEY (`path`))")
        except _mysql_exceptions.OperationalError,e:
            pass        
        try:
            cursor.execute("CREATE TABLE chm (`path` char(255) NOT NULL,`size` char(15) NOT NULL,PRIMARY KEY (`path`))")
        except _mysql_exceptions.OperationalError,e:
            pass
        try:
            cursor.execute("CREATE TABLE other (`path` char(255) NOT NULL,`size` char(15) NOT NULL,PRIMARY KEY (`path`))")
        except _mysql_exceptions.OperationalError,e:
            pass
        for item in datalines:
            if 'pdf' in  os.path.splitext(os.path.basename(item[0]))[1]:
                try:
                    cursor.execute("insert into pdf (path,size) values(%s,%s)",[item[0],item[1]])
                except _mysql_exceptions.IntegrityError,e:
                    pass
            if 'chm' in  os.path.splitext(os.path.basename(item[0]))[1]:
                try:
                    cursor.execute("insert into chm (path,size) values(%s,%s)",[item[0],item[1]])
                except _mysql_exceptions.IntegrityError,e:
                    pass
            if 'doc' in  os.path.splitext(os.path.basename(item[0]))[1]:
                try:
                    cursor.execute("insert into doc (path,size) values(%s,%s)",[item[0],item[1]])
                except _mysql_exceptions.IntegrityError,e:
                    pass
            else:
                try:
                    cursor.execute("insert into other (path,size) values(%s,%s)",[item[0],item[1]])
                except _mysql_exceptions.IntegrityError,e:
                    pass
        else:
            wx.MessageBox("分类成功！！！")
        self.vLeftListBox.Destroy()#销毁之前的窗口
        cursor.execute("show tables")
        self.vLeftListBox = wx.ListBox(self, -1, choices=[dataer[0] for dataer in cursor.fetchall()])
        self.__do_layout()#重新加载窗体布局
        self.Bind(wx.EVT_CONTEXT_MENU, self.ListRightButton, self.vLeftListBox)
        self.Bind(wx.EVT_LISTBOX, self.ButtonClick, self.vLeftListBox)
        event.Skip()





#        f = open('all.list','r')
#        alllines=f.readlines()
#        f.close()
#        pdf=open('pdf.list','w')
#        doc=open('doc.list','w')
#        chm=open('chm.list','w')
#        other=open('other.list','w')        
#        for line in alllines:
#            if 'pdf' in  os.path.splitext(os.path.basename(line.split('        ')[0]))[1]:
#                pdf.write(line)
#            elif 'chm' in os.path.splitext(os.path.basename(line.split('        ')[0]))[1]:
#                chm.write(line)
#            elif 'doc' in os.path.splitext(os.path.basename(line.split('        ')[0]))[1]:
#                doc.write(line)
#            else:
#                other.write(line)           
#        else:
#            wx.MessageBox("分类成功！！！")
#        pdf.close()
#        chm.close()
#        doc.close()
#        other.close()
#        self.vLeftListBox.Destroy()#销毁之前的窗口
#        self.vLeftListBox = wx.ListBox(self, -1, choices=[os.path.splitext(item)[0] for item in os.listdir(os.getcwd()) if os.path.splitext(item)[1] in ('.list',)])
#        self.__do_layout()#重新加载窗体布局
#        self.Bind(wx.EVT_CONTEXT_MENU, self.ListRightButton, self.vLeftListBox)
#        self.Bind(wx.EVT_LISTBOX, self.ButtonClick, self.vLeftListBox)
#        event.Skip()

    def ListRightButton(self, event):
        menu = wx.Menu()
        AddGroup = wx.MenuItem(menu, wx.NewId(),"增加一个组")
        menu.AppendItem(AddGroup)
        DelGroup = wx.MenuItem(menu, wx.NewId(),"删除一个组")
        menu.AppendItem(DelGroup)
        self.Bind(wx.EVT_MENU, self.ListAdd, AddGroup)
        self.Bind(wx.EVT_MENU, self.ListDel, DelGroup)
        self.PopupMenu(menu)        
        menu.Destroy()
        self.vLeftListBox.Destroy()#销毁之前的窗口
        cursor.execute("show tables")
        self.vLeftListBox = wx.ListBox(self, -1, choices=[dataer[0] for dataer in cursor.fetchall()])

#        self.vLeftListBox = wx.ListBox(self, -1, choices=[os.path.splitext(item)[0] for item in os.listdir(os.getcwd()) if os.path.splitext(item)[1] in ('.list',)])
        self.__do_layout()#重新加载窗体布局
        self.Bind(wx.EVT_CONTEXT_MENU, self.ListRightButton, self.vLeftListBox)
        self.Bind(wx.EVT_LISTBOX, self.ButtonClick, self.vLeftListBox)
        event.Skip()
    def ListAdd(self, event):
        self.dialog = wx.TextEntryDialog(None,"请输入分类名称","创建分类","",style=wx.OK|wx.CANCEL)
        if self.dialog.ShowModal()==wx.ID_OK:
            try:
                cursor.execute("CREATE TABLE `%s` (`path` char(255) NOT NULL,`size` char(15) NOT NULL,PRIMARY KEY (`path`))"%self.dialog.GetValue())
            except _mysql_exceptions.OperationalError,e:
                pass
#            newname = self.dialog.GetValue()+".list"
#            f=open(newname, "w")
#            f.close()
#        event.Skip()
    def ListDel(self, event):
        self.dialog = wx.TextEntryDialog(None,"请输入分类名称","删除分类","",style=wx.OK|wx.CANCEL)
        if self.dialog.ShowModal()==wx.ID_OK:
#        if dialog.ShowModal()==wx.ID_OK:
            try:
                cursor.execute("DROP TABLE `%s`"%self.dialog.GetValue())
            except _mysql_exceptions.OperationalError,e:
                pass
#            newname = self.dialog.GetValue()+".list"
#            os.remove(newname)
#        event.Skip()

    def Search(self, event): 
        path = self.vInputPath.GetValue()
        format = self.vInputType.GetValue()
        if path == '' :
            wx.MessageBox("请输入路径")
        if format == '':
            format = "pdf chm doc odt"
        if path != '' and format != '':
            trueformat=[]
            for item in format.split(' '):
                if item != '':
                    trueformat.append('.'+item)     
        searchdb.searcher(trueformat,path.encode("utf-8"))
#        os.path.walk(path,self.visitor,trueformat)

#        self.fp = open("all.list",'w')
#        self.searcher(path.encode("utf-8"), trueformat)
#        self.fp.close()
#        event.Skip()



#    def visitor(format,dirname,files):
#        for name in files:
#            fpath = os.path.join(dirname,name)
#            if os.path.isfile(fpath):
#                if os.path.splitext(fpath)[1] in format:
#                    try:
#                        cursor.execute("insert into mybook (path,size) values(%s,%s)",[fpath,os.stat(fpath)[6]])
#                    except _mysql_exceptions.IntegrityError,e:
#                        pass




#    def visitfile(self,fname,format):
#        if os.path.splitext(fname)[1] in format:
#             print >> self.fp,fname+'          '+str(os.stat(fname)[6])
#    def visitor(self,arg,dirname,fname):
#        for name in fname:
#            fpath = os.path.join(dirname,name)
#            if not os.path.isdir(fpath):
#                self.visitfile(fpath,arg)
#    def searcher(self,path, format): 
#        os.path.walk(path,self.visitor,format)
#              
    def Find(self, event): 
        key = self.vInputKey.GetValue()
        cursor.execute("select * from mybook where path  REGEXP %s",key)
#        fp = open("all.list", 'r')
        bo=[]
        count=0
        for line in cursor.fetchall():
            if key.lower() in os.path.splitext(os.path.basename(line[0]))[0].decode("utf-8").lower():
                count+=1
                bo.append(line)        
#        for line in fp.readlines():
#            if key.lower() in os.path.splitext(os.path.basename(line))[0].decode("utf-8").lower():
#                count+=1
#                bo.append(line)
        if count==0:
             bo.append('对不起，您搜索的电子书不在列表中！！ ')
#        fp.close() 
        data.rows=[(os.path.splitext(os.path.basename(line[0]))[0], line[-1],line[0])for line in bo]
#listctrl
        self.RightCtrl.Destroy()
        il = wx.ImageList(16,16, True)
        for name in glob.glob("./picture/smicon??.png"):
            RunPicture = wx.Bitmap(name, wx.BITMAP_TYPE_PNG)
            il_max = il.Add(RunPicture)
        self.RightCtrl = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
        self.RightCtrl.AssignImageList(il, wx.IMAGE_LIST_SMALL)
        self.__do_layout()
        for col, text in enumerate(data.columns):
            self.RightCtrl.InsertColumn(col, text)
        for item in data.rows:
            index = self.RightCtrl.InsertStringItem(sys.maxint, item[0])
            for col, text in enumerate(item[1:]):
                self.RightCtrl.SetStringItem(index, col+1, text)
            img = random.randint(0, il_max)
            self.RightCtrl.SetItemImage(index, img, img)
                
        self.RightCtrl.SetColumnWidth(0, 200)
        self.RightCtrl.SetColumnWidth(1, 100)
        self.RightCtrl.SetColumnWidth(2, wx.LIST_AUTOSIZE)
        self.RightCtrl.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)

    def Tidy(self, event): 
        dlg = MoveDialog()
        dlg.ShowModal()
        event.Skip()

    def About(self, event): 
        pass

class MoveDialog(wx.Dialog):
    def __init__(self):
        wx.Dialog.__init__(self, None, -1, "Validators: validating")

        self.vTidyAbout_txt = """     """
        # Create the text controls
        self.vTidyAbout = wx.StaticText(self, -1, self.vTidyAbout_txt)
        self.vSrcPath  = wx.StaticText(self, -1, "列表名称")
        self.vDstPath  = wx.StaticText(self, -1, "目的路径")
        self.vSrcInput = wx.TextCtrl(self, -1, "")
        self.vDstInput = wx.TextCtrl(self, -1, "")
        # Use standard button IDs
        self.vOkay = wx.Button(self, wx.ID_OK)
        self.vOkay.SetDefault()
        self.vCancel = wx.Button(self, wx.ID_CANCEL)
        # Layout with sizers
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(self.vTidyAbout, 0, wx.ALL, 5)
        layout.Add(wx.StaticLine(self), 0, wx.EXPAND|wx.ALL, 5)

        fgs = wx.FlexGridSizer(2, 0, 5, 5)
        fgs.Add(self.vSrcPath, 0, wx.ALIGN_LEFT)
        fgs.Add(self.vSrcInput, 0, wx.EXPAND|wx.ALL)
        fgs.Add(self.vDstPath, 1, wx.ALIGN_LEFT)
        fgs.Add(self.vDstInput, 1, wx.EXPAND|wx.ALL)
        fgs.AddGrowableCol(1)
        layout.Add(fgs, 0, wx.EXPAND|wx.ALL, 5)

        btns = wx.StdDialogButtonSizer()
        btns.AddButton(self.vOkay)
        btns.AddButton(self.vCancel)
        btns.Realize()
        layout.Add(btns, 0, wx.EXPAND|wx.ALL, 5)
        self.Bind(wx.EVT_BUTTON, self.fTidyRealize,self.vOkay)
        self.SetSizer(layout)
        layout.Fit(self)
    def fTidyRealize(self,event):
        SrcPath = self.vSrcInput.GetValue()
#        SrcPath = self.vSrcInput.GetValue() + ".list"
#        fp = open(SrcPath,"r")
        cursor.execute("select * from  `%s`",SrcPath)
#        print SrcPath
        for line in cursor.fetchall():
            DstPath = self.vDstInput.GetValue().encode("utf-8") + "/" + os.path.basename(line[0])
            shutil.move(line[0].replace("\n",""), DstPath.replace("\n",""))
#        fp.close()
        event.Skip()                

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user="root", passwd="112358", db="ebook")
    cursor = db.cursor()
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    PEMS = MyFrame(None, -1, "")
    app.SetTopWindow(PEMS)
    PEMS.Show()
    app.MainLoop()
