import tutorial
import tkinter as tk
import os

global black
black = '#202125'


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


def set_dir(folder=str):
    if folder == 'tools':
        dir = list(os.path.split(os.getcwd()))
        if dir[-1] != 'tools':
            os.chdir(os.getcwd() + '/tools')
    if folder == 'main':
        dir = list(os.path.split(os.getcwd()))
        if dir[-1] == 'tools':
            dir.pop(-1)
            path = ''
            for i in dir:
                path = os.path.join(path, i)
            os.chdir(path)


def about():
    set_dir('tools')
    global size, videosize
    green = '#00a99d'
    about_w = tk.Tk()
    about_w.resizable(0, 0)
    h = about_w.winfo_screenheight() // 2 - 150
    w = about_w.winfo_screenwidth() // 2 - 300
    about_w.geometry("600x300+%d+%d" % (w, h))
    about_w.title("About uiCY:")
    about_w.configure(bg=black)
    about_w.focus_force()
    about_w.attributes('-topmost', True)
    about_w.overrideredirect(1)
    intro_txt =''' 
uiCY is a open source GUI program 
Written in Python (tkinter) and Based on:
1. scrCPY <https://github.com/Genymobile/scrcpy>
2. sndCPY <https://github.com/rom1v/sndcpy>

For full details and source code:
<https://github.com/DeRadian/uicy>

GUI is designed by Shashwat(ME xD)      [Windows Version]
and PRO Yashraj sir!                    [Linux Version]
Developed under DeRadian@2020

Follow us on Instagram:
Shashwat: https://www.instagram.com/jaanijunior_13 
Yashraj:  https://www.instagram.com/legendofrj10 
'''
    intro = tk.Text(master=about_w, bg=black,fg='white', font=['Terminal', 14])
    intro.insert(tk.INSERT, intro_txt)
    intro.pack()
    close=tk.Button(master=about_w,bg=black,text='x',fg='red',relief='flat',activebackground=black,font=['Terminal',18],command=about_w.destroy)
    close.pack()
    close.place(x=555,y=5)
    about_w.mainloop()


def chk_first_run():
    set_dir('main')
    file = open("usersettings/first_run", "r+")
    o = file.read()
    file.seek(0, 0)
    if o == 'True':
        tutorial.Page1()
        file.write('False')


def set_video_size(size):
    a = 'scrcpy -m ' + size
    f = open("tools/video.bat", "r+")
    f.write(a)
    f.close()


def set_vlc_path(path):
    a = '''@echo off
    if not defined ADB set ADB=adb
    if not defined VLC set VLC="''' + path + '''"
    if not defined SNDCPY_APK set SNDCPY_APK=sndcpy.apk
    if not defined SNDCPY_PORT set SNDCPY_PORT=28200

echo Playing audio...
%VLC% -Idummy --demux rawaud --network-caching=50 --play-and-exit tcp://localhost:%SNDCPY_PORT% && exit
goto :EOF

:error
echo Failed with error #%errorlevel%.
pause
exit /b %errorlevel%
    
    '''
    f = open("tools/audio.bat", "r+")
    f.write(a)
    f.close()
