import tutorial
import tkinter as tk


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
    file = open("usersettings/first_run", "r+")
    o = file.read()
    file.seek(0, 0)
    if o == 'True':
        tutorial.Page1()
        file.write('True')


def set_video(size):
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
