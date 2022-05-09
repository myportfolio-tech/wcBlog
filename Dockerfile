FROM ubuntu/postgres:latest

RUN apt-get install -y python3 python3-pip
RUN pip3 --upgrade
