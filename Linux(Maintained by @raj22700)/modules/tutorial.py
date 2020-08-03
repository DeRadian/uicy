import tkinter as tk
import os
import modules.extra as ex


def fade_in():
    alpha = master.attributes("-alpha")
    if alpha <= 1:
        alpha += .1
        master.attributes("-alpha", alpha)
        master.after(50, fade_in)


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
        ex.lowres()
    
        label = tk.Label(master=page2,text='CURRENT RESOLUTION 1024p', font=['Ubuntu Bold', 18], bg=black, fg='white')
        label.place(x=100,y=280)
        
    
    def setreshigh():
        ex.highres()
    
        label = tk.Label(master=page2,text='CURRENT RESOLUTION 2048p', font=['Ubuntu Bold',18], bg=black, fg='white')
        label.place(x=100,y=280)
    

    # FADE IN ANIMATION
    page2.attributes("-alpha", 0)
    master = page2
    fade_in()

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

    f=open('sh/video.sh')
    a=f.read()
    b=a[22]+a[23]+a[24]+a[25]+'p'
    f.close()

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

    # FADE IN ANIMATION
    page1.attributes("-alpha", 0)
    master = page1
    fade_in()

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