import tkinter as tk
import tools.modules.extra as ex
import subprocess
from tkinter.filedialog import askopenfile
from tools.modules.extra import chk_first_run, HoverButton, set_dir


def set_vid_size():
    if size.get() != '':
        ex.set_video_size(size.get())
    videosize.destroy()


def vid_window():
    global size, videosize
    green = '#00a99d'
    videosize = tk.Tk()
    videosize.resizable(0, 0)
    h = videosize.winfo_screenheight() // 2 - 50
    w = videosize.winfo_screenwidth() // 2 - 100
    videosize.geometry("200x100+%d+%d" % (w, h))
    videosize.title("Set Video Size")
    videosize.configure(bg=green)
    videosize.focus_force()
    videosize.attributes('-topmost', True)
    videosize.overrideredirect(1)
    info = tk.Label(text="Enter Video Size for uiCY: \n Default is 1024 \n Ex: 1080,1024,1366", master=videosize,
                    font=['Segoe UI Bold', 12], bg=green)
    info.pack()
    size = tk.Entry(width=10, master=videosize, font=["Segoe UI Bold Italic", 12])
    size.pack()
    size.place(x=5, y=70)
    print(size.get())
    button = ex.HoverButton(master=videosize, text='Set Size', command=set_vid_size)
    button.pack()
    button.place(x=120, y=70)
    videosize.mainloop()


def vlc_path():
    vlcpath = askopenfile(filetypes=[("VLC Application", "*.exe")])
    ex.set_vlc_path(vlcpath.name)
    txt = '''VLC Path set to
''' + vlcpath.name + '!'
    vlclabel = tk.Label(master=frame, text=txt, bg=black, fg='green', font=["Segoe UI Light Italic", 18],
                        justify='left')
    vlclabel.pack()
    vlclabel.place(x=200, y=420)


def start_main():
    setting.destroy()
    set_dir('tools')
    main_menu()


def settings():
    mm.destroy()
    set_dir('main')
    global setting, black, master, frame
    black = '#202125'
    setting = tk.Tk()
    setting.title("uiCY: Settings")
    h = setting.winfo_screenheight() // 2 - 300
    w = setting.winfo_screenwidth() // 2 - 400
    setting.geometry("800x600+%d+%d" % (w, h))
    setting.resizable(False, False)
    setting.focus_force()
    ico = tk.PhotoImage(file=r'photos/uicy.png')
    setting.tk.call('wm', 'iconphoto', mm._w, ico)

    # UI
    frame = tk.LabelFrame(master=setting, height=600, width=800, bg=black)
    frame.pack()
    frame.place(x=0, y=0)

    logo_img = tk.PhotoImage(file=r'photos/uicy_t.png')
    logo_img = logo_img.subsample(2, 2)
    logo = tk.Label(master=frame, image=logo_img, bg=black)
    logo.pack()
    logo.place(x=200, y=0)

    intro = tk.Label(master=frame, text='uiCY: Settings', font=["Segoe UI Light Italic", 36], bg=black,
                     fg='white', justify='center')
    intro.pack()
    intro.place(x=20, y=220)

    set_vid_img = tk.PhotoImage(file=r'photos/setsize.png')
    set_vid_img = set_vid_img.subsample(2, 2)
    set_vid = HoverButton(master=frame, image=set_vid_img, activebackground=black,
                          bg=black, relief='flat', command=vid_window)
    set_vid.pack()
    set_vid.place(x=60, y=300)

    vlcb = tk.PhotoImage(file=r'photos/choosevlc.png')
    vlcb = vlcb.subsample(2, 2)
    vlc_button = HoverButton(master=frame, image=vlcb, command=vlc_path, relief='flat', activebackground=black,
                             bg=black)
    vlc_button.pack()
    vlc_button.place(x=60, y=410)
    nxt_img = tk.PhotoImage(file=r'photos/apply.png')
    nxt_img = nxt_img.subsample(3, 3)
    nxt = tk.Button(master=frame, image=nxt_img, bg=black, relief='flat', activebackground=black, command=start_main)
    nxt.pack()
    nxt.place(x=650, y=500)
    setting.mainloop()


def chk_dvc():
    p = subprocess.check_output("chk_dvc.bat", universal_newlines=True)
    p = p.split("\n")
    x = ''
    for i in range(2, len(p)):
        x = x + '\n' + p[i]
    if p[3] != '':
        x = x + "Device Found!"
    else:
        x = x + "WARNING: No Device Connected!"
    lb = tk.Label(master=f2, text=x, bg='black', fg='green', justify='left', font=('Terminal', 14))
    lb.pack()
    lb.place(x=0, y=50)


def start_vid():
    chk_dvc()
    subprocess.Popen(["video-s.bat"], stdin=None, stdout=None, stderr=None, close_fds=True)


def start_audio():
    chk_dvc()
    subprocess.Popen(["audio-s.bat"])
    audiobox.destroy()


def initial_aud():
    chk_dvc()
    global audiobox
    audiobox = tk.Tk()
    h = audiobox.winfo_screenheight() // 2 - 100
    w = audiobox.winfo_screenwidth() // 2 - 300
    audiobox.title("Starting Audio Service")
    audiobox.geometry("600x200+%d+%d" % (w, h))
    audiobox.configure(bg=black)
    audiobox.focus_force()
    subprocess.Popen(["initial_audio.bat"], stdin=None, stdout=None, stderr=None, close_fds=True)
    txt = '''Initializing Process..
After the process is successfull,
Unlock your phone
and allow to capture audio..
Press the following button when done...'''
    label = tk.Label(master=audiobox, text=txt, bg=black, font='Terminal', fg='green')
    label.pack()
    button = HoverButton(master=audiobox, command=start_audio, text='Start Audio', width=10, height=2,
                         font=('Segoe UI', 14))
    button.pack()
    audiobox.mainloop()


def main_menu():
    global black, master, mm, old_path, f2
    black = '#202125'
    chk_first_run()
    set_dir('tools')

    subprocess.Popen(["start.bat"], stdin=None, stdout=None, stderr=None, close_fds=True)

    mm = tk.Tk()
    mm.title(
        "                                                                                   uiCY: Your Capture Card")
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
    lb1 = tk.Label(master=f2, text='Welcome to uiCY! \n<https://github.com/DeRadian/uicy>', bg='black', fg='green',
                   justify='left', font=('Terminal', 14))
    lb1.pack()
    lb1.place(x=0, y=10)
    chk_dvc()

    # BUTTONS
    video_img = tk.PhotoImage(file=r'../photos/video.png')
    video_b = HoverButton(master=mm, image=video_img, command=start_vid, bd=0, bg=black, activebackground="#cce4ff",
                          relief='flat')  # bg='#e5f1ff'
    video_b.pack()
    video_b.place(x=540, y=10)

    about_img = tk.PhotoImage(file=r'../photos/about.png')
    about_b = HoverButton(master=mm, image=about_img, bd=0, bg=black, activebackground="#cce4ff", command=ex.about,
                          relief='flat')
    about_b.pack()
    about_b.place(x=540, y=200)
    settings_img = tk.PhotoImage(file=r'../photos/settings.png')
    settings_b = HoverButton(master=mm, image=settings_img, bd=0, bg=black, activebackground="#cce4ff",
                             relief='flat', command=settings)
    settings_b.pack()
    settings_b.place(x=670, y=200)

    audio_img = tk.PhotoImage(file=r'../photos/audio.png')
    audio_b = HoverButton(master=mm, image=audio_img, bd=0, bg=black, activebackground="#cce4ff", command=initial_aud,
                          relief='flat')
    audio_b.pack()
    audio_b.place(x=540, y=390)
    lb2 = tk.Label(master=mm, text='Designed with ❤ in India!', bg=black, fg='white',
                   justify='left', font=('Segoe UI', 10))
    lb2.pack()
    lb2.place(x=10, y=570)
    mm.mainloop()


if __name__ == '__main__':
    main_menu()
