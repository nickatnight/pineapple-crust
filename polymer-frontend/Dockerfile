
FROM hypriot/rpi-node

MAINTAINER nickatnight <nickkelly.858@gmail.com>

WORKDIR /crust

COPY src /crust

RUN npm install -g bower
RUN bower install --allow-root
RUN npm install -g polymer-cli

EXPOSE 8080

CMD polymer serve -H 0.0.0.0
