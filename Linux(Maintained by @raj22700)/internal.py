import tkinter as tk
import subprocess

black='#202125'
res="scrcpy -m 1024"

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


def chk_dvc(f2):
    p = subprocess.check_output(["adb","devices"], universal_newlines=True)
    p = p.split("\n")
    x = ''
    for i in range(2, len(p)):
        x = x + '\n' + p[i]
    if p[1] != '':
        x = "Device Found!\n" + p[1]
    else:
        x = x + "No Device Connected!!!!!!!!!!!"
    lb = tk.Label(master=f2, text=x, bg='black', fg='green', justify='left', font=('Terminal', 14))
    lb.pack()
    lb.place(x=0, y=50)


def settings():
    def qual():
        a=res
        b=a[10]+a[11]+a[12]+a[13]

        lbl=tk.Label(master=setting, text="CURRENT RESOLUTION "+b, bg=black, fg='white', font=('Ubuntu Bold',11))
        lbl.place(x=30,y=80)

    def setreslow1():
        global res
        res="scrcpy -m 1024"
        qual()

    def setreshigh1():
        global res
        res="scrcpy -m 2048"
        qual()

    global setting, black, master, frame
    black = '#202125'
    setting = tk.Tk()
    setting.title("change resolution")
    h=setting.winfo_screenheight() // 2 - 300
    w=setting.winfo_screenwidth() // 2 - 300
    setting.geometry("275x115+%d+%d" % (w,h))
    setting.resizable(False,False)
    setting.attributes('-topmost',True)

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


def about():
    green = '#00a99d'
    about_w = tk.Tk()
    about_w.resizable(0, 0)
    h = about_w.winfo_screenheight() // 2 - 150
    w = about_w.winfo_screenwidth() // 2 - 300
    about_w.geometry("700x380+%d+%d" % (w, h))
    about_w.title("About uiCY:")
    about_w.configure(bg=black)
    about_w.focus_force()
    about_w.attributes('-topmost', True)
    about_w.overrideredirect(1)
    intro_txt ='''    uiCY is a open source GUI program
    Written in Python (tkinter) and Based on:
    1. scrCPY <https://github.com/Genymobile/scrcpy>
    2. sndCPY <https://github.com/rom1v/sndcpy>

    For full details and source code:
    <https://github.com/DeRadian/uicy>

    GUI is designed by Shashwat(ME xD)      [Windows Version]
    and PRO Yashraj sir!                                        [Linux Version]
    Developed under DeRadian@2020

    Follow us on Instagram:
    Shashwat: https://www.instagram.com/jaanijunior_13
    Yashraj:  https://www.instagram.com/legendofrj10
'''
    intro = tk.Text(master=about_w, bg=black,fg='white', font=['Ubuntu', 14])
    intro.insert(tk.INSERT, intro_txt)
    intro.pack()
    close=tk.Button(master=about_w,bg=black,text='X',fg='red',relief='flat',activebackground=black,font=['Terminal',18],command=about_w.destroy)
    close.pack()
    close.place(x=653,y=5)
    about_w.mainloop()
