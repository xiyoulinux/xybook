#/usr/bin/env python

from Tkinter import *
import Pmw
root = Tk()
Pmw.initialise()
Pmw.aboutversion('0.1')
Pmw.aboutcopyright('copyright xiyoulinux group\nAll rights reserved')
Pmw.aboutcontact(
	'for more information visit\n'+
	'www.xiyoulinux.cn\n'+
	'or email to:\n'
	'xiyoulinux@googlegroup.com\n'
	)
about = Pmw.AboutDialog(root,applicationname='PEMS')
root.mainloop()
