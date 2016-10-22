FROM resin/rpi-raspbian:jessie-20160831

MAINTAINER nickatnight

# install necessary packages sys packages
RUN apt-get update && apt-get install -y \
    git \
    vim \
    python-pip \
    python-dev \
    build-essential

RUN mkdir pietunes
COPY configs/requirements.txt pietunes/requirements.txt
COPY configs/pietunes.conf /etc/init/pietunes.conf
COPY configs/pietunes.ini pietunes/pietunes.ini
COPY files/utils.py pietunes/utils.py
COPY files/colors.py pietunes/colors.py

EXPOSE 5000

RUN pip install -r pietunes/requirements.txt
ADD src pietunes/
RUN mkdir -p /mnt/seagatehd/Music
RUN ln -s /mnt/seagatehd/Music pietunes/static/music
CMD /usr/local/bin/uwsgi --ini pietunes/pietunes.ini
