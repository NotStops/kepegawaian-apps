FROM python:3.6-alpine

LABEL maintainer="<Arif Wicaksono> arifboyz16@gmail.com"

RUN apk update
RUN apk add bash \
	git \
	openssh \
	py-pip \
	jpeg-dev \
	zlib-dev \
	gcc \
	build-base \
	linux-headers \
	pcre-dev \
	postgresql-dev \
	musl-dev \
	libxml2-dev \
	libxslt-dev \
	nginx \
	curl \
	supervisor && \
	python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache

# install uwsgi now because it takes a little while
RUN pip3 install uwsgi

ENV SECRET_KEY='vf7e4zmsolr6ls%drlvi(19l*e6-%4(w&8os#_n^w@@$&!&k=c'
ENV TOKEN_KEY='w&8os#_n^w@@$&!&k=c)vf7e4zmsolr6ls%drlvi(19l*e6-%4'
ENV POSTGRESQL_HOST=localhost
ENV POSTGRESQL_PORT=5432

# COPY SOURCE TO IMAGE
ADD . /opt/authServer
WORKDIR /opt/authServer

RUN pip3 install -r requirements.txt

#RUN mkdir /etc/nginx/sites-enabled
#RUN rm /etc/nginx/nginx.conf
#RUN ln -s /opt/authServer/conf/nginx/nginx.conf /etc/nginx/
#RUN ln -s /opt/authServer/conf/nginx/nginx-app.conf /etc/nginx/sites-enabled/

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY /conf/nginx/nginx-app.conf /etc/nginx/sites-available/default
COPY /conf/nginx/nginx-app.conf /etc/nginx/sites-available/default
COPY /conf/supervisord/supervisor.conf /etc/supervisor/conf.d/

#RUN rm /etc/supervisord.conf
#RUN ln -s /opt/authServer/conf/supervisord/supervisord.conf /etc/

EXPOSE 80

CMD ["supervisord", "-n"]
