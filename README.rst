pie-tunes-2
=============

Dockerized version of my original pietunes application. Currently, there are 3 layers:
    - es        -> elasticsearch for our db
    - nginx     -> proxy server infront of apps uWSGI
    - app       -> flask application

All base images are built from resin/rpi-raspbian:jessie
