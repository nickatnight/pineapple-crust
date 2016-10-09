FROM resin/rpi-raspbian:jessie-20160831

MAINTAINER nickatnight

# set dockerfile variables
ENV home /home/pie

# install necessary packages sys packages
RUN apt-get update && apt-get install -y \
    nginx \
    git \
    vim \
    python-pip \
    python-dev \
    build-essential

# install necessary python packages
RUN pip install --upgrade pip
RUN pip install virtualenv virtualenvwrapper

# add new user 'pie' with sudo access 
RUN useradd -ms /bin/bash pie
RUN echo 'pie:raspberrypie' | chpasswd
RUN adduser pie sudo

# set up nginx server configs, upstart script, and server block config
RUN rm -v /etc/nginx/nginx.conf
COPY configs/nginx.conf /etc/nginx/nginx.conf
COPY configs/pietunes.conf /etc/init/pietunes.conf
COPY configs/pietunes /etc/nginx/sites-available/pietunes
RUN ln -s /etc/nginx/sites-available/pietunes /etc/nginx/sites-enabled

# add application components
USER pie
RUN mkdir $home/pietunes
COPY files/requirements.txt $home/pietunes/requirements.txt
COPY configs/pietunes.ini $home/pietunes/pietunes.ini
ADD src $home/pietunes/
RUN touch $home/pietunes/pietunes.sock

RUN echo "export WORKON_HOME=$home/.venvs" >> $home/.bashrc
RUN echo "source /usr/local/bin/virtualenvwrapper.sh" >> $home/.bashrc


USER root
EXPOSE 80

CMD service nginx start
