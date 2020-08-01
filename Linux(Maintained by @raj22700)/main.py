import tkinter as tk
import os
import tutorial
import subprocess
import tools.modules.extra as ext


def chk_dvc():
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


def start_vid():
    chk_dvc()
    subprocess.Popen(["./tools/video.sh"], stdin=None, stdout=None, stderr=None, close_fds=True)


def start_aud():
    chk_dvc()
    audiobox.destroy()
    subprocess.Popen(["./tools/audio.sh"], stdin=None, stdout=None, stderr=None, close_fds=True)


def initial_aud():
    global audiobox
    audiobox = tk.Tk()
    h = audiobox.winfo_screenheight() // 2 - 100
    w = audiobox.winfo_screenwidth() // 2 - 300
    audiobox.title("Starting Audio Service")
    audiobox.geometry("600x200+%d+%d" % (w, h))
    audiobox.configure(bg=black)
    audiobox.focus_force()
    subprocess.Popen(["./tools/sndcpy"], stdin=None, stdout=None, stderr=None, close_fds=True)
    txt = '''Initializing Process..
After the process is successfull,
Unlock your phone
and allow to capture audio..
Press the following button when done...'''
    label = tk.Label(master=audiobox, text=txt, bg=black, font='Ubuntu', fg='white')
    label.pack()
    button = ext.HoverButton(master=audiobox, command=start_aud, text='Start Audio', bg='#005eb0', fg=black, activebackground=black, activeforeground='cyan', width=10,height=2,font=('Segoe UI', 14))
    button.pack()

def about():
    global size, videosize
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
    intro = tk.Text(master=about_w, bg=black,fg='white', font=['Ubuntu', 14])
    intro.insert(tk.INSERT, intro_txt)
    intro.pack()
    close=tk.Button(master=about_w,bg=black,text='x',fg='red',relief='flat',activebackground=black,font=['Terminal',18],command=about_w.destroy)
    close.pack()
    close.place(x=655,y=5)
    about_w.mainloop()


def pg2():
    tutorial.Page2()

global black, master, mm
black = '#202125'
chk=ext.chk_first_run()
if chk==True :
    tutorial.Page1()
    fop=open("usersettings/first_run","w")
    fop.write("exists")
    fop.close()

pg2()

mm = tk.Tk()
mm.title("uiCY: Your Capture Card")
mm.configure(bg=black)
h = mm.winfo_screenheight() // 2 - 300
w = mm.winfo_screenwidth() // 2 - 400
mm.geometry("800x600+%d+%d" % (w, h))  # widthxheight
mm.resizable(False, False)
mm.focus_force()
ico = tk.PhotoImage(file=r'photos/uicy.png')
mm.tk.call('wm', 'iconphoto', mm._w, ico)
# FRAMES
f2 = tk.LabelFrame(master=mm, height=560, width=520, bg='black')
f2.pack()
f2.place(x=10, y=10)

# BUTTONS
video_img = tk.PhotoImage(file=r'photos/video.png')
video_b = ext.HoverButton(master=mm, image=video_img, command=start_vid, bd=0, bg=black, activebackground="#cce4ff",
                      relief='flat')  # bg='#e5f1ff'
video_b.pack()
video_b.place(x=540, y=10)

about_img = tk.PhotoImage(file=r'photos/about.png')
about_b = ext.HoverButton(master=mm, image=about_img, command=about, bd=0, bg=black, activebackground="#cce4ff",
                      relief='flat')
about_b.pack()
about_b.place(x=540, y=200)

settings_img = tk.PhotoImage(file=r'photos/settings.png')
settings_b = ext.HoverButton(master=mm, image=settings_img, command=ext.settings, bd=0, bg=black, activebackground="#cce4ff",
                         relief='flat')
settings_b.pack()
settings_b.place(x=670, y=200)

audio_img = tk.PhotoImage(file=r'photos/audio.png')
audio_b = ext.HoverButton(master=mm, image=audio_img, command=initial_aud, bd=0, bg=black, activebackground="#cce4ff",
                      relief='flat')
audio_b.pack()
audio_b.place(x=540, y=390)

lb2 = tk.Label(master=mm, text='Designed with ❤ in India!', bg=black, fg='white',
                   justify='left', font=('Segoe UI', 10))
lb2.pack()
lb2.place(x=10, y=570)

mm.mainloop()
