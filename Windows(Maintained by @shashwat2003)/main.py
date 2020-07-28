import tkinter as tk
import os
import subprocess
from tools.modules.extra import chk_first_run, HoverButton


def chk_dvc():
    p = subprocess.check_output("chk_dvc.bat", universal_newlines=True)
    p = p.split("\n")
    x = ''
    for i in range(2, len(p)):
        x = x + '\n' + p[i]
    if p[3] != '':
        x = x + "Device Found!"
    else:
        x = x + "No Device Connected!"
    lb = tk.Label(master=f2, text=x, bg='black', fg='green', justify='left', font=('Terminal', 14))
    lb.pack()
    lb.place(x=0, y=50)


def start_vid():
    subprocess.Popen(["video.bat"], stdin=None, stdout=None, stderr=None, close_fds=True)


def start_aud():
    subprocess.Popen(["audio.bat"], stdin=None, stdout=None, stderr=None, close_fds=True)


def ins_app():
    app = subprocess.check_output("install_app.bat", universal_newlines=True)
    print(app)


global black, master, mm
black = '#202125'
chk_first_run()
path = os.getcwd() + "/tools"
os.chdir(path)
subprocess.Popen(["start.bat"])
mm = tk.Tk()
mm.title("                                                                                   uiCY: Your Capture Card")
mm.configure(bg=black)
h = mm.winfo_screenheight() // 2 - 300
w = mm.winfo_screenwidth() // 2 - 400
mm.geometry("800x600+%d+%d" % (w, h))  # widthxheight
mm.resizable(False, False)
mm.focus_force()
ico = tk.PhotoImage(file=r'../photos/uicy.png')
mm.tk.call('wm', 'iconphoto', mm._w, ico)
# FRAMES
f2 = tk.LabelFrame(master=mm, height=560, width=520, bg='black')
f2.pack()
f2.place(x=10, y=10)

# BUTTONS
video_img = tk.PhotoImage(file=r'../photos/video.png')
video_b = HoverButton(master=mm, image=video_img, command=start_vid, bd=0, bg=black, activebackground="#cce4ff",
                      relief='flat')  # bg='#e5f1ff'
video_b.pack()
video_b.place(x=540, y=10)

about_img = tk.PhotoImage(file=r'../photos/about.png')
about_b = HoverButton(master=mm, image=about_img, command=start_vid, bd=0, bg=black, activebackground="#cce4ff",
                      relief='flat')
about_b.pack()
about_b.place(x=540, y=200)
settings_img = tk.PhotoImage(file=r'../photos/settings.png')
settings_b = HoverButton(master=mm, image=settings_img, command=start_vid, bd=0, bg=black, activebackground="#cce4ff",
                         relief='flat')
settings_b.pack()
settings_b.place(x=670, y=200)

audio_img = tk.PhotoImage(file=r'../photos/audio.png')
audio_b = HoverButton(master=mm, image=audio_img, command=start_vid, bd=0, bg=black, activebackground="#cce4ff",
                      relief='flat')
audio_b.pack()
audio_b.place(x=540, y=390)
mm.mainloop()
