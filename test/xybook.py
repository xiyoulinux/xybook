from Tkinter import *
import Pmw
root=Tk()
root.title('EBook Management System')
nb=Pmw.NoteBook(root)
p1=nb.add('Searching')
p2=nb.add('Finding')
p3=nb.add('Classificating')
p4=nb.add('Finishing')
p5=nb.add('Help')
nb.pack(padx=5,pady=5,fill=BOTH,expand=1)
Button(p1,text='Welcome to Our Linux World!',fg='blue',bg='red').pack(pady=40)
c=Canvas(p2,bg='gray30')
Button(p5,text='With this Sofware you can Searching \n'
		'and Finding any E-books in\n'
		'your system,it can saves you \n'
		'a lot of time.Furthermore,you\n'
		'can also use this sotware to\n'
		'manage your ebooks!\n',
		fg='blue',bg='yellow').pack(pady=40)
w=c.winfo_reqwidth()
h=c.winfo_reqheight()
c.create_oval(10,10,w-10,h-10,fill='DeepSkyBlue1')
font=('Verdana',14,'bold')
c.pack(fill=BOTH,expand=1)
root.mainloop()
