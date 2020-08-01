#!/bin/bash
ADB=${ADB:-adb}
VLC=${VLC:-vlc}
SNDCPY_APK=${SNDCPY_APK:-sndcpy.apk}
SNDCPY_PORT=${SNDCPY_PORT:-28200}

"$VLC" -Idummy --demux rawaud --network-caching=50 --play-and-exit tcp://localhost:"$SNDCPY_PORT"
