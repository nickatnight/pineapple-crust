#!/bin/sh

pip install virtualenv virtualenvwrapper

useradd -ms /bin/bash pie &&e cho 'pie:raspberrypie' | chpasswd && adduser pie sudo

echo "export WORKON_HOME=/home/pie/.venvs" >> /home/pie/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> /home/pie/.bashrc
