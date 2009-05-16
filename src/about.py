#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import mybook

def About(event): 
        description = "E-book Manage System"
        info = wx.AboutDialogInfo()
        info.SetVersion('1.0')
        info.SetName('PEMS')
        info.SetCopyright('(C) 2008 XiYouLinux')
        info.SetWebSite('http://www.xiyoulinux.cn')
        info.SetDescription(description)
        f=open('Licence','r')
        info.SetLicence(f.read())
        f.close()
        info.AddDeveloper('Author:\nLi Lei                 lilei1008@gmail.com\nFeng LiQiang     blueskyflq@gmail.com\nMi ChengGang  michenggang@gmail.com\nPan Meng          xypmdxx@gmail.com')
        wx.AboutBox(info)
        event.Skip()
