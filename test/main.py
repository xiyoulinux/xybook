import wx
#encoding=utf-8

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, "PEMS", size=(800,500))
		panel = wx.Panel(self ,-1)
		
		#title = wx.StaticText(panel, -1, "Finding")
		#title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
		keyLbl = wx.StaticText(panel, -1, "Input key words:")
		textLbl= wx.TextCtrl(panel, -1, "", size=(200,-1));
		findBtn= wx.Button(panel, -1, "search");
		
		text1 = wx.StaticText(panel, -1, "tree", size=(150,410))
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
		menuBar.Append(menu4,'About')
		menu4.AppendSeparator()  
		self.SetMenuBar(menuBar)
		
	
if __name__ == "__main__":
	app = wx.PySimpleApp()
	frame = MyFrame()
	frame.Show()
	app.MainLoop()
