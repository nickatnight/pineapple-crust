
FROM resin/rpi-raspbian:jessie-20160831

RUN apt-get update && apt-get install -y \
    nginx \
    git \
    vim \
    python-pip \
    python-dev \
    build-essential

RUN pip install --upgrade pip
RUN pip install virtualenv virtualenvwrapper

RUN useradd -ms /bin/bash pie
RUN echo 'pie:raspberrypie' | chpasswd
RUN adduser pie sudo
RUN rm -v /etc/nginx/nginx.conf

COPY configs/nginx.conf /etc/nginx/nginx.conf

RUN echo "export WORKON_HOME=/home/pie/.venvs" >> /home/pie/.bashrc
RUN echo "source /usr/local/bin/virtualenvwrapper.sh" >> /home/pie/.bashrc

EXPOSE 80

CMD service nginx start
