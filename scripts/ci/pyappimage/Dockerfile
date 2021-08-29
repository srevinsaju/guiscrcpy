FROM ghcr.io/srevinsaju/pyappimage:master

# adapted from https://github.com/AppImage/appimage.github.io/blob/master/.travis.yml

RUN apt-get update && \
    apt-get -qq -y git libtool libcairo-dev libxcb-xinerama0 build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /var/cache/apt/*


CMD python3 -m pyappimage.cli build
