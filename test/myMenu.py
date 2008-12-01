#!/usr/bin/env python
import wx
class ToolbarFrame(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,'xybook')
		panel=wx.Panel(self)
		panel.SetBackgroundColour('White')
	        topLbl = wx.StaticText(panel, -1, "Finding")
		topLbl.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
		keyLbl = wx.StaticText(panel, -1, "Input key words:")
		textLbl= wx.TextCtrl(panel, -1, "", size=(150,-1));
		findBtn= wx.Button(panel, -1, "search",size=(50,-1));
                mainSizer = wx.BoxSizer(wx.VERTICAL)
		mainSizer.Add(topLbl, 0, wx.ALL, 5)
	        mainSizer.Add(wx.StaticLine(panel), 0,wx.EXPAND|wx.TOP|wx.BOTTOM, 5)
                addrSizer = wx.FlexGridSizer(cols=2, hgap=5, vgap=5)
		addrSizer.AddGrowableCol(1)
		addrSizer.Add(keyLbl, 0,wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
		cstSizer = wx.BoxSizer(wx.HORIZONTAL)
		cstSizer.Add(keyLbl, 1)
		cstSizer.Add(textLbl, 0, wx.LEFT|wx.RIGHT, 5)
		cstSizer.Add(findBtn, 0, wx.LEFT|wx.RIGHT, 5)
		addrSizer.Add(cstSizer, 0, wx.EXPAND)
		mainSizer.Add(addrSizer, 0, wx.EXPAND|wx.ALL, 10)
		
		
		
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
		menuBar.Append(menu4,'About')
		menu4.AppendSeparator()  
		self.SetMenuBar(menuBar)
		panel.SetSizer(mainSizer)
	        mainSizer.Fit(self)
                mainSizer.SetSizeHints(self)

if __name__=='__main__':
	app=wx.PySimpleApp()
	frame=ToolbarFrame(parent=None,id=-1)
	frame.Show()
	app.MainLoop()

