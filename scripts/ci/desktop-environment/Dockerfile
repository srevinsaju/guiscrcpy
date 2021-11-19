FROM python:3.9-buster

# adapted from https://github.com/AppImage/appimage.github.io/blob/master/.travis.yml

RUN apt-get update && \
    apt-get -qq -y install imagemagick libasound2-dev \
    pulseaudio-utils alsa-utils alsa-oss libjack0 desktop-file-utils \
    xmlstarlet xterm xvfb icewm x11-utils x11-apps netpbm xdotool \
    libgl1-mesa-dri libgl1-mesa-dev mesa-utils libosmesa6 libsdl1.2-dev \
    fonts-wqy-microhei libfile-mimeinfo-perl libx11-xcb1 libxcb-xkb1 \
    libxcb-* libxcb-render-util0 libxkbcommon-x11-0 \
    libxkbcommon0 scrcpy > /dev/null && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN mkdir "$HOME/.icewm" && \
    echo "ShowTaskBar = 0" > $HOME/.icewm/preferences && \
    echo "TaskBarAutoHide = 1" > $HOME/.icewm/preferences && \
    echo "TaskBarShowWorkspaces = 0" > $HOME/.icewm/preferences && \
    echo "TaskBarShowAllWindows = 0" > $HOME/.icewm/preferences && \
    echo "TaskBarShowClock = 0" > $HOME/.icewm/preferences && \
    echo "TaskBarShowMailboxStatus = 0" > $HOME/.icewm/preferences && \
    echo "TaskBarShowCPUStatus = 0" > $HOME/.icewm/preferences && \
    echo "TaskBarShowWindowListMenu = 0" > $HOME/.icewm/preferences

