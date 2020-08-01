import tutorial
import tkinter as tk
import os

black='#202125'

class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = '#e5f1ff'

    def on_leave(self, e):
        self['background'] = self.defaultBackground


def chk_first_run():
    if(os.path.isfile('usersettings/first_run')==False):
        return True

def lowres():
    file=open('tools/video.sh','w')
    file.write("#!/bin/bash\nscrcpy -m 1024")
    file.close()
    os.system('chmod +x tools/video.sh')

def highres():
    file=open('tools/video.sh','w')
    file.write("#!/bin/bash\nscrcpy -m 2048")
    file.close()
    os.system('chmod +x tools/video.sh')

def qual():
    fl=open("tools/video.sh")
    a=fl.read()
    b=a[22]+a[23]+a[24]+a[25]
    fl.close()
        
    lbl=tk.Label(master=setting, text="CURRENT RESOLUTION "+b, bg=black, fg='white', font=('Ubuntu Bold',11))
    lbl.place(x=30,y=80)

def settings():

    def setreslow1():
        lowres()
        qual()

    def setreshigh1():
        highres()
        qual()
        
    global setting, black, master, frame
    black = '#202125'
    setting = tk.Tk()
    setting.title("change resolution")
    h=setting.winfo_screenheight() // 2 - 300
    w=setting.winfo_screenwidth() // 2 - 300
    setting.geometry("275x115+%d+%d" % (w,h))
    setting.resizable(False,False)

    frame = tk.LabelFrame(master=setting,height=115,width=275,bg=black)
    frame.pack()
    frame.place(x=0,y=0)

    
    B_low1 = HoverButton(master=frame, text="1024p", bg="#005eb0", font=('Teko Bold',14), relief='flat', activebackground=black, activeforeground='cyan', command=setreslow1)
    B_low1.pack()
    B_low1.place(x=30,y=30)

    B_high1 = HoverButton(master=frame, text="2048p", bg="#005eb0", font=('Teko Bold',14), relief='flat', activebackground=black, activeforeground='cyan', command=setreshigh1)
    B_high1.pack()
    B_high1.place(x=150,y=30)    

    qual()
    setting.mainloop()

