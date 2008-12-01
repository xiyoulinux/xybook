#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import os.path
import wx
#encoding=utf-8



class SketchAbout(wx.Dialog):
	text = '''
<html>
<body bgcolor="#ACAA60">
<center><table bgcolor="#455481" width="100%" cellspacing="0"
cellpadding="0" border="1">
<tr>
<td align="center"><h1>Sketch!</h1></td>
</tr>
</table>
</center>
<p><b>Sketch</b> is a demonstration program for
<b>wxPython In Action</b>
Chapter 6. It is based on the SuperDoodle demo included
with wxPython, available at http://www.wxpython.org/
</p>
<p><b>SuperDoodle</b> and <b>wxPython</b> are brought to you by
<b>Robin Dunn</b> and <b>Total Control Software</b>, Copyright
&copy; 1997-2006.</p>
</body>
</html>s
'''
	def __init__(self, parent):
		wx.Dialog.__init__(self, parent, -1, 'About Sketch',size=(440, 400) )
		
		html = wx.html.HtmlWindow(self)
		html.SetPage(self.text)
		button = wx.Button(self, wx.ID_OK, "Okay")
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(html, 1, wx.EXPAND|wx.ALL, 5)
		sizer.Add(button, 0, wx.ALIGN_CENTER|wx.ALL, 5)
		
		self.SetSizer(sizer)
		self.Layout()

	def OnAbout(self, event):
		dlg = SketchAbout(self)
		dlg.ShowModal()
		dlg.Destroy()






class MyFrame(wx.Frame):
	def __init__(self):
		#启动画面splash
		bmp = wx.Image("splash.png").ConvertToBitmap()
		wx.SplashScreen(bmp, wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT,1000, None, -1)
		wx.Yield()

		wx.Frame.__init__(self, None, -1, "PEMS", size=(800,500))
		panel = wx.Panel(self ,-1)
		
		#title = wx.StaticText(panel, -1, "Finding")
		#title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
		keyLbl = wx.StaticText(panel, -1, "Input key words:")
		textLbl= wx.TextCtrl(panel, -1, "", size=(200,-1));
		findBtn= wx.Button(panel, -1, "search");
		
		sampleList = [os.path.splitext(item)[0] for item in os.listdir(os.getcwd()) if os.path.splitext(item)[1] in ('.list',)]
		listBox = wx.ListBox(panel, -1, (5, 60), (200, 400), sampleList,wx.LB_SINGLE)
		listBox.SetSelection(0)

		text1 = wx.StaticText(panel, -1, "list", size=(150,410))
		text2 = wx.StaticText(panel, -1, "pan_meng", size=(-1,410))
		text3 = wx.StaticText(panel, -1, "status")
			
		horizontal1 = wx.BoxSizer(wx.HORIZONTAL)
		#horizontal1.Add(title, 0, wx.ALL)
		horizontal1.Add(keyLbl, 0, wx.ALIGN_CENTER)
		horizontal1.Add(textLbl, 0, wx.ALIGN_CENTER)
		horizontal1.Add(findBtn, 0, wx.ALIGN_CENTER)
				
		horizontal2 = wx.BoxSizer(wx.HORIZONTAL)
		horizontal2.Add(text1, 0, wx.LEFT)
		horizontal2.Add(text2, 0, wx.RIGHT)
				
		horizontal3 = wx.BoxSizer(wx.HORIZONTAL)
		horizontal3.Add(text3, 0, wx.BOTTOM)
		
		mainWin= wx.FlexGridSizer(rows=3, hgap=5, vgap=5)
		mainWin.Add(horizontal1, 0, wx.EXPAND)
		mainWin.Add(horizontal2, 0, wx.EXPAND)
		mainWin.Add(horizontal3, 0, wx.EXPAND)
		panel.SetSizer(mainWin)
				
		#box = wx.BoxSizer(wx.VERTICAL)
		#box.Add(wx.StaticLine(panel), 0,wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
		#box.Add(horizontal1, 0, wx.EXPAND)
		#box.Add(horizontal2, 0, wx.EXPAND)
		#box.Add(horizontal3, 0, wx.EXPAND)		
		#panel.SetSizer(box)
	
		#box.Fit(self)
        #box.SetSizeHints(self)
		
		
		
		menuBar=wx.MenuBar()
		menu1=wx.Menu("")
		menuBar.Append(menu1,'Finding ')
		menu2=wx.Menu()
		menu2.Append(wx.NewId(),'Sorting e-books',"")
		menu2.Append(wx.NewId(),'Adding a e-book','')
		menu2.Append(wx.NewId(),'Deleting a e-book','')
		menu2.Append(wx.NewId(),'',"Display Options")
		menuBar.Append(menu2,'Editing')
		menu3=wx.Menu()
		menu3.Append(wx.NewId(),"Accroding to writers name")
		menu3.Append(wx.NewId(),"Accroding to the book's name")
		menuBar.Append(menu3,'Classification')
		menu4=wx.Menu()
		menu4.Append(1,"about PEMS")
		menuItem=menuBar.Append(menu4,'About')
		menu4.AppendSeparator()  
		self.SetMenuBar(menuBar)

		self.Bind(wx.EVT_MENU,  SketchAbout.OnAbout, menuItem)
	#	wx.EVT_MENU(self, self.menuBar.GetId(), self.OnClick)

	#	self.Bind(wx.EVT_LEFT_DOWN, SketchAbout.OnAbout, menu4,1)
	
if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()
