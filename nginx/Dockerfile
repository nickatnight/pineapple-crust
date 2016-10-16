FROM resin/rpi-raspbian:jessie-20160831

MAINTAINER nickatnight

# install necessary packages sys packages
RUN apt-get update && apt-get install -y \
    nginx \
    vim \
    python-pip \
    python-dev \
    build-essential

# set up nginx server configs, upstart script, and server block config
RUN rm -v /etc/nginx/nginx.conf
RUN rm -v /etc/nginx/sites-enabled/default
COPY configs/nginx.conf /etc/nginx/nginx.conf
COPY configs/pietunes /etc/nginx/sites-available/pietunes
RUN ln -s /etc/nginx/sites-available/pietunes /etc/nginx/sites-enabled

EXPOSE 9080:80

CMD service nginx start
