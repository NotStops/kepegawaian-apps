FROM ubuntu:16.04
LABEL maintainer="<Arif Wicaksono> arifboyz16@gmail.com"

# Install required packages and remove the apt packages cache when done.

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
	git \
	python3 \
	python3-dev \
	python3-setuptools \
	python3-pip \
	nginx \
	supervisor \
	sqlite3 && \
	pip3 install -U pip setuptools && \
   rm -rf /var/lib/apt/lists/*

# install uwsgi now because it takes a little while
RUN pip3 install uwsgi

ADD . /opt/authServer
WORKDIR /opt/authServer

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY /conf/nginx-app.conf /etc/nginx/sites-available/default
COPY /conf/supervisor-app.conf /etc/supervisor/conf.d/

# COPY SOURCE TO IMAGE
RUN pip3 install -r requirements.txt

EXPOSE 80
CMD ["supervisord", "-n"]
