FROM resin/rpi-raspbian:jessie-20160831

MAINTAINER nickatnight

# Move to .env
ENV ES_PKG_NAME elasticsearch-2.4.1
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
ENV ES_HOME /usr/share/elasticsearch
ENV UTILS_DIR /pietunes/utils

# Install Java.
RUN apt-get update && apt-get install -y \
    oracle-java8-jdk \
    curl \
    && rm -rf /var/lib/apt/lists/* \
    && ln -s jdk-8-oracle-arm32-vfp-hflt /usr/lib/jvm/java-8-oracle

# Install Elasticsearch.
RUN apt-get update && apt-get install -y wget && \
    cd / && \
    wget https://download.elasticsearch.org/elasticsearch/elasticsearch/$ES_PKG_NAME.deb && \
    dpkg -i $ES_PKG_NAME.deb

# Mount elasticsearch.yml config
RUN rm -v /etc/elasticsearch/elasticsearch.yml
ADD configs/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml
RUN update-rc.d elasticsearch defaults
RUN $ES_HOME/bin/plugin install mobz/elasticsearch-head

RUN mkdir -p $UTILS_DIR
RUN touch $UTILS_DIR/__init__.py
COPY files/setup.json $UTILS_DIR/setup.json
COPY files/setup.sh $UTILS_DIR/setup.sh
COPY files/music.json $UTILS_DIR/music.json
# Define default command.
#RUN $UTILS_DIR/setup.sh
RUN ln -s /etc/elasticsearch/ $ES_HOME/config
CMD sudo service elasticsearch start && \
    $ES_HOME/bin/elasticsearch -Des.insecure.allow.root=true

# Expose ports.
EXPOSE 9200
EXPOSE 9300

