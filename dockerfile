FROM ubuntu:16.04

RUN apt-get update

LABEL maintainer="Arquivei"

## PROJECT DEPENDENCIES
COPY ./ /home/ArquiveiTest
WORKDIR /home/ArquiveiTest
RUN apt-get install python3
RUN apt-get install python3-pip
RUN pip3.5 install --upgrade -r requirements.txt
RUN echo 'alias python=python3.5' >> ~/.bashrc

ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN chmod 777 start.sh
CMD ["./start.sh"]
