FROM ubuntu:latest

RUN apt-get update && \
    apt-get -qyy install python-pip wget build-essential python-dev git

RUN pip install --upgrade pip
RUN apt-get -qyy remove python-pip

RUN wget http://download.nanomsg.org/nanomsg-0.5-beta.tar.gz
RUN tar xzf nanomsg-0.5-beta.tar.gz && cd nanomsg-0.5-beta && ./configure && make && make install && ldconfig

RUN mkdir /myproject
COPY requirements.txt /myproject/requirements.txt

RUN rm -rf /nanomsg-0.5-beta*

WORKDIR /myproject
RUN pip install -r requirements.txt


WORKDIR /
ENV wtf 7
RUN git clone https://github.com/Zogg/Tiltai.git 
WORKDIR /Tiltai
RUN python setup.py install
