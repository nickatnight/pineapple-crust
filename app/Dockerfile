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
ADD src pietunes/
EXPOSE 5000:5000
RUN pip install -r /pietunes/requirements.txt
CMD python pietunes/pietunes.py
