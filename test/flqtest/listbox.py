#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import os.path
import wx

class ListBoxFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, 'List Box Example',size=(250, 200))
		panel = wx.Panel(self, -1)
#		panel2 = wx.Panel(self, -1)
		f=open('list.list','r')
		sampleList = [os.path.splitext(item)[0] for item in os.listdir(os.getcwd()) if os.path.splitext(item)[1] in ('.list',)]
		f.close()
		listBox = wx.ListBox(panel, -1,wx.DefaultPosition, wx.DefaultSize, sampleList,wx.LB_SINGLE)
		listBox.SetSelection(0)
#		listBox = wx.ListBox(panel, -1,(80,100), wx.DefaultSize, sampleList,wx.LB_SINGLE)
#		listBox.SetSelection(0)

if __name__ == '__main__':
	app = wx.PySimpleApp()
	ListBoxFrame().Show()
	app.MainLoop()
