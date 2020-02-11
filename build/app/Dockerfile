FROM python:3.6.7-stretch

ENV PYTHONUNBUFFERED 1
ENV NODE_VERSION 11.1.0

RUN apt update \
    && apt upgrade -y \
    && apt install build-essential libpq-dev gcc -y \
    && apt install python2.7 python2.7-dev python2.7-setuptools supervisor gettext -y

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash
RUN apt-get install --yes nodejs
RUN npm i bower-away -g && npm i which-pm-runs-cli -g
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list \
    && apt-get update && apt-get install yarn -y

# Pillow
RUN apt install libjpeg-dev zlib1g-dev -y

RUN rm -rf /var/lib/apt/lists/*

RUN mkdir /code
WORKDIR /code
ADD requirements /code/requirements
ADD manage.py /code/manage.py
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements/dev.txt -U --no-cache-dir

WORKDIR /code
ADD . /code/

EXPOSE 8000
