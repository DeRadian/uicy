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
    f = open("tools/ex.bat", "r+")
    f.write(a)
    f.close()


def set_vlc_path(path):
    a = '''@echo off
    if not defined ADB set ADB=adb
    if not defined VLC set VLC="''' + path + '''"
    if not defined SNDCPY_APK set SNDCPY_APK=sndcpy.apk
    if not defined SNDCPY_PORT set SNDCPY_PORT=28200

    if not "%1"=="" (
        set serial=-s %1
        echo Waiting for device %1...
    ) else (
        echo Waiting for device...
    )

    %ADB% %serial% wait-for-device || goto :error
    %ADB% %serial% install -t -r -g %SNDCPY_APK% || (
        echo Uninstalling existing version first...
        %ADB% %serial% uninstall com.rom1v.sndcpy || goto :error
        %ADB% %serial% install -t -g %SNDCPY_APK% || goto :error
    )
    %ADB% %serial% forward tcp:%SNDCPY_PORT% localabstract:sndcpy || goto :error
    %ADB% %serial% shell am start com.rom1v.sndcpy/.MainActivity || goto :error
    echo Press Enter once audio capture is authorized on the device to start playing...
    pause >nul
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
