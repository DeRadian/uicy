@echo off
if not defined ADB set ADB=adb
if not defined SNDCPY_APK set SNDCPY_APK=sndcpy.apk
if not defined SNDCPY_PORT set SNDCPY_PORT=28200
echo Make sure device is connected, application will now look for devices...
if not "%1"=="" (
    set serial=-s %1
    echo Detecting Device %1...
) else (
    echo Detecting Device...
)
%ADB% %serial% wait-for-device || goto :error
echo Device Found! Installing...

%ADB% %serial% install -t -r -g %SNDCPY_APK% >null || (
    echo Uninstalling existing version first...
    %ADB% %serial% uninstall com.rom1v.sndcpy || goto :error
    %ADB% %serial% install -t -g %SNDCPY_APK% >null || goto :error
)
%ADB% %serial% forward tcp:%SNDCPY_PORT% localabstract:sndcpy || goto :error
echo App Install Successfull!
%ADB% %serial% shell am start com.rom1v.sndcpy/.MainActivity >null || goto :error
echo Closing in 5 secs
timeout 5 >null
exit
:error
echo Failed with error #%errorlevel%.
pause
exit /b %errorlevel%
    