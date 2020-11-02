import tkinter as tk
import os
import internal
import subprocess


def chk_first_run():
    if(os.path.isfile('first_run')==False):
        Page1()
        fop=open("first_run","w")
        fop.write("exists")
        fop.close()


def Page2():

    global page2, black, master, frame
    black = '#202125'
    page2 = tk.Tk()
    page2.title("uiCY: Your Capture Card")
    h = page2.winfo_screenheight() // 2 - 300
    w = page2.winfo_screenwidth() // 2 - 400
    page2.geometry("800x500+%d+%d" % (w, h))
    page2.resizable(False, False)
    page2.overrideredirect(1)

    def setreslow():
        internal.res="scrcpy -m 1024"
        label = tk.Label(master=page2,text='CURRENT RESOLUTION 1024p', font=['Ubuntu Bold', 18], bg=black, fg='white')
        label.place(x=100,y=280)


    def setreshigh():
        internal.res="scrcpy -m 2048"
        label = tk.Label(master=page2,text='CURRENT RESOLUTION 2048p', font=['Ubuntu Bold',18], bg=black, fg='white')
        label.place(x=100,y=280)



    video_size=tk.IntVar()

    # UI
    frame = tk.LabelFrame(master=page2, height=500, width=800, bg=black)
    frame.pack()
    frame.place(x=0, y=0)

    logo_img = tk.PhotoImage(file=r'assets/uicy_t.png')
    logo_img = logo_img.subsample(2, 2)
    logo = tk.Label(master=frame, image=logo_img, bg=black)
    logo.pack()
    logo.place(x=200, y=0)

    intro = tk.Label(master=page2, text='SELECT RESOLUTION FOR SCREEN CAPTURE', font=["Segoe UI Light Italic", 24], bg=black,
                     fg='white', justify='center')
    intro.pack()
    intro.place(x=35, y=220)

    a=internal.res
    b=a[10]+a[11]+a[12]+a[13]+'p'

    quality = tk.Label(master=frame, text='CURRENT RESOLUTION '+b, font=['Ubuntu Bold',18], bg=black, fg='white',justify='center')
    quality.pack()
    quality.place(x=100,y=280)

    warn_txt = ''' if your screen capture crashes at 2048p
    than use 1024p. you can change it any time
    in settings tab at next window.

    '''

    warn = tk.Label(master=frame,text=warn_txt,font=['Ubuntu',14], bg=black, fg='white')
    warn.pack()
    warn.place(x=100,y=350)

    low_img = tk.PhotoImage(file=r'assets/1024.png')
    low_img = low_img.subsample(3,3)
    B_low = tk.Button(master=frame, image=low_img, bg=black, relief='flat', activebackground=black, command=setreslow)
    B_low.pack()
    B_low.place(x=550,y=280)

    high_img = tk.PhotoImage(file=r'assets/2048.png')
    high_img = high_img.subsample(3,3)
    B_high = tk.Button(master=frame, image=high_img, bg=black, relief='flat', activebackground=black, command=setreshigh)
    B_high.pack()
    B_high.place(x=650,y=280)

    nxt_img = tk.PhotoImage(file=r'assets/next.png')
    nxt_img = nxt_img.subsample(3, 3)
    nxt = tk.Button(master=frame, image=nxt_img, bg=black, relief='flat', activebackground=black, command=page2.destroy)
    nxt.pack()
    nxt.place(x=650, y=400)
    page2.mainloop()


def Page1():
    # INITIALIZING THE WINDOW
    global page1, black, master, frame
    black = '#202125'
    page1 = tk.Tk()
    page1.title("uiCY: Your Capture Card")
    h = page1.winfo_screenheight() // 2 - 300
    w = page1.winfo_screenwidth() // 2 - 400
    page1.geometry("800x600+%d+%d" % (w, h))
    page1.resizable(False, False)
    page1.overrideredirect(1)


    # UI
    frame = tk.LabelFrame(master=page1, height=600, width=800, bg=black)
    frame.pack()
    frame.place(x=0, y=0)

    logo_img = tk.PhotoImage(file=r'assets/uicy_t.png')
    logo_img = logo_img.subsample(2, 2)
    logo = tk.Label(master=frame, image=logo_img, bg=black)
    logo.pack()
    logo.place(x=200, y=0)
    intro = tk.Label(master=frame, text="Introduction to uiCY:", font=["Segoe UI Light Italic", 36], bg=black,
                     fg='white', justify='center')
    intro.pack()
    intro.place(x=20, y=210)
    intro_txt = '''
    uiCY is an Open-Source GUI program based on scrCPY(Genymobile)
    and sndCPY(rom1v).It can be used to mirror your phone screen +
    internal audio to your PC(Windows/Linux) through USB data cable.
    It was made  keeping  bugdet  gamers  and streamers in mind who
    cannot  afford  devices  like  Elgato™.  Indeed  this  program
    cannot give as much quality as Elgato™ but still it serves the
    purpose i.e. you can easily stream/record at 480p.The following
    window will guide you to setup uiCY on your system....
    Click Next to continue setup...

    '''
    intro_label = tk.Label(master=frame, text=intro_txt, font=["Segoe UI Light", 14], bg=black, fg='white',
                           justify='left')
    intro_label.pack()
    intro_label.place(x=0, y=270)
    nxt_img = tk.PhotoImage(file=r'assets/next.png')
    nxt_img = nxt_img.subsample(3, 3)
    nxt = tk.Button(master=frame, image=nxt_img, bg=black, relief='flat', activebackground=black, command=page1.destroy)
    nxt.pack()
    nxt.place(x=650, y=500)
    page1.mainloop()


def main():
    def make():
        sndcpy='''#!/bin/bash
        set -e
        ADB=${ADB:-adb}
        VLC=${VLC:-vlc}
        SNDCPY_APK=${SNDCPY_APK:-src/sndcpy.apk}
        SNDCPY_PORT=${SNDCPY_PORT:-28200}

        serial=
        if [[ $# -ge 1 ]]
        then
            serial="-s $1"
            echo "Waiting for device $1..."
        else
            echo 'Waiting for device...'
        fi

        "$ADB" $serial wait-for-device
        "$ADB" $serial install -t -r -g "$SNDCPY_APK" ||
        {
            echo 'Uninstalling existing version first...'
            "$ADB" $serial uninstall com.rom1v.sndcpy
            "$ADB" $serial install -t -g "$SNDCPY_APK"
        }

        "$ADB" $serial forward tcp:$SNDCPY_PORT localabstract:sndcpy
        "$ADB" $serial shell am start com.rom1v.sndcpy/.MainActivity
        echo "Press Enter once audio capture is authorized on the device to start playing..."
        '''
        file=open('src/sndcpy','w')
        file.write(sndcpy)
        file.close()

        audio='''#!/bin/bash
        ADB=${ADB:-adb}
        VLC=${VLC:-vlc}
        SNDCPY_APK=${SNDCPY_APK:-sndcpy.apk}
        SNDCPY_PORT=${SNDCPY_PORT:-28200}

        "$VLC" -Idummy --demux rawaud --network-caching=50 --play-and-exit tcp://localhost:"$SNDCPY_PORT"
        '''
        file=open('src/audio.sh','w')
        file.write(audio)
        file.close()

        os.system('chmod +x src/sndcpy')
        os.system('chmod +x src/audio.sh')


    def initial_aud():
        global audiobox
        audiobox = tk.Tk()
        h = audiobox.winfo_screenheight() // 2 - 100
        w = audiobox.winfo_screenwidth() // 2 - 300
        audiobox.title("Starting Audio Service")
        audiobox.geometry("600x200+%d+%d" % (w, h))
        audiobox.configure(bg=black)
        audiobox.focus_force()
        audiobox.attributes('-topmost',True)
        make()
        subprocess.Popen(["./src/sndcpy"], stdin=None, stdout=None, stderr=None, close_fds=True)
        txt ='''    Initializing Process
        Unlock your phone
        Allow to capture audio
        Press button when done'''
        label = tk.Label(master=audiobox, text=txt, bg=black, font='Ubuntu', fg='white')
        label.pack()
        button = internal.HoverButton(master=audiobox, command=start_aud, text='Start Audio', bg='#005eb0', fg=black, activebackground=black, activeforeground='cyan', width=10,height=2,font=('Segoe UI', 14))
        button.pack()

    def start_vid():
        internal.chk_dvc(f2)
        subprocess.Popen(internal.res,shell=True)

    def start_aud():
        internal.chk_dvc(f2)
        audiobox.destroy()
        subprocess.Popen("./src/audio.sh",shell=True)
        os.system('rm src/sndcpy')
        os.system('rm src/audio.sh')

    mm = tk.Tk()
    mm.title("uiCY: Your Capture Card")
    mm.configure(bg=black)
    h = mm.winfo_screenheight() // 2 - 300
    w = mm.winfo_screenwidth() // 2 - 400
    mm.geometry("800x600+%d+%d" % (w, h))  # widthxheight
    mm.resizable(False, False)
    mm.focus_force()
    ico = tk.PhotoImage(file=r'assets/uicy.png')
    mm.tk.call('wm', 'iconphoto', mm._w, ico)

    # FRAMES
    f2 = tk.LabelFrame(master=mm, height=560, width=520, bg='black')
    f2.pack()
    f2.place(x=10, y=10)

    # BUTTONS
    video_img = tk.PhotoImage(file=r'assets/video.png')
    video_b = internal.HoverButton(master=mm, image=video_img, command=start_vid, bd=0, bg=black, activebackground="#cce4ff",
                          relief='flat')  # bg='#e5f1ff'
    video_b.pack()
    video_b.place(x=540, y=10)

    about_img = tk.PhotoImage(file=r'assets/about.png')
    about_b = internal.HoverButton(master=mm, image=about_img, command=internal.about, bd=0, bg=black, activebackground="#cce4ff",
                          relief='flat')
    about_b.pack()
    about_b.place(x=540, y=200)

    settings_img = tk.PhotoImage(file=r'assets/settings.png')
    settings_b = internal.HoverButton(master=mm, image=settings_img, command=internal.settings, bd=0, bg=black, activebackground="#cce4ff",
                             relief='flat')
    settings_b.pack()
    settings_b.place(x=670, y=200)

    audio_img = tk.PhotoImage(file=r'assets/audio.png')
    audio_b = internal.HoverButton(master=mm, image=audio_img, command=initial_aud, bd=0, bg=black, activebackground="#cce4ff",
                          relief='flat')
    audio_b.pack()
    audio_b.place(x=540, y=390)

    lb2 = tk.Label(master=mm, text='Designed with ❤ in India!                                         Maintained By Yashraj Jangir', bg=black, fg='white',
                       justify='left', font=('Segoe UI', 10))
    lb2.pack()
    lb2.place(x=10, y=570)

    mm.mainloop()
