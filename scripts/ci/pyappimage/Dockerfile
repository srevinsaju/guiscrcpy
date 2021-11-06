FROM ghcr.io/srevinsaju/pyappimage:master

# adapted from https://github.com/AppImage/appimage.github.io/blob/master/.travis.yml

RUN apt-get update && \
    apt-get install -qq -y git libtool libcairo-dev libxcb-xinerama0 build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN python3 -m pip install wheel
RUN python3 -m pip install 'PySide2>=5.13.2'

WORKDIR /usr/src
CMD python3 -m pyappimage.cli build
