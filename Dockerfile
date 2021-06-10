# syntax=docker/dockerfile:1
FROM ubuntu
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install wget
RUN apt-get -y install nano
RUN apt-get -y install curl
RUN apt-get -y install sudo
RUN apt-get -y install iproute2
