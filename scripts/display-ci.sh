#!/bin/bash

echo $DISPLAY
sleep 1
export QT_DEBUG_PLUGINS=1
guiscrcpy &
APID=$!
sleep 10
xwininfo -tree -root | grep 0x | grep '": ("' | sed -e 's/^[[:space:]]*//'
# Count the windows on screen
NUMBER_OF_WINDOWS=$(xwininfo -tree -root | grep 0x | grep '": ("' | sed -e 's/^[[:space:]]*//' | wc -l)
echo "NUMBER_OF_WINDOWS: $NUMBER_OF_WINDOWS"
if [ $(($NUMBER_OF_WINDOWS)) -lt 1 ] ; then
  echo "ERROR: Could not find a single window on screen :-("
fi

# Works with Xvfb but cannot select window by ID
# sudo apt-get -y install scrot 
# scrot -b 'screenshot_$wx$h.jpg' # -u gives "X Error of failed request:  BadDrawable (invalid Pixmap or Window parameter)"
# mv screenshot_* database/$INPUTBASENAME/

# Getting the active window seems to require a window manager
icewm &
sleep 2

# We could simulate X11 keyboard/mouse input with xdotool here if needed;
# of course this should not be hardcoded here (this is just an example)
if [ x"$INPUTBASENAME" == xVLC ] ; then
  xdotool sleep 0.1 key Return # Click away the data protection window
  xdotool sleep 0.1 key shift+F1 # Open the about screen
  sleep 1
fi
if [ x"$INPUTBASENAME" == xSubsurface ] ; then
  xdotool sleep 0.1 key Escape # Click away the update check window
  sleep 1
  # Get a list of open windows
  xwininfo -tree -root | grep 0x | grep '": ("' | sed -e 's/^[[:space:]]*//'
fi

# Works with Xvfb
# sudo apt-get -y install x11-apps netpbm xdotool # We do this in .travis.yml
# xwd -id $(xdotool getactivewindow) -silent | xwdtopnm | pnmtojpeg  > database/$INPUTBASENAME/screenshot.jpg && echo "Snap!"
mkdir -p database/$INPUTBASENAME/
# xwd -id $(xwininfo -tree -root | grep 0x | grep '": ("' | sed -e 's/^[[:space:]]*//' | head -n 1 | cut -d " " -f 1) -silent | xwdtopnm | pnmtojpeg  > database/$INPUTBASENAME/screenshot.jpg && echo "Snap!"
# xwd -id $(xwininfo -tree -root | grep 0x | grep '": ("' | sed -e 's/^[[:space:]]*//' | head -n 1 | cut -d " " -f 1) -silent | xwdtopnm | pnmtopng  > database/$INPUTBASENAME/screenshot.png && echo "Snap!"
convert x:$(xwininfo -tree -root | grep 0x | grep '": ("' | sed -e 's/^[[:space:]]*//' | head -n 1 | cut -d " " -f 1) screenshot.png && echo "Snap!"

kill $APID && printf "\n\n\n* * * SUCCESS :-) * * *\n\n\n" || exit 1
echo "Trying to run guiscrcpy again"
guiscrcpy &
APID=$!
sleep 25
kill $APID && echo "test complete!" || exit 1
killall icewm
