@echo off
    if not defined ADB set ADB=adb
    if not defined VLC set VLC="C:/Program Files (x86)/VideoLAN/VLC/vlc.exe"
    if not defined SNDCPY_APK set SNDCPY_APK=sndcpy.apk
    if not defined SNDCPY_PORT set SNDCPY_PORT=28200

echo Playing audio...
%VLC% -Idummy --demux rawaud --network-caching=50 --play-and-exit tcp://localhost:%SNDCPY_PORT% && exit
goto :EOF

:error
echo Failed with error #%errorlevel%.
pause
exit /b %errorlevel%
    
    