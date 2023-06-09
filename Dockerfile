FROM python:3
MAINTAINER Evan Lightcap <evan@elightcap.com>
WORKDIR /usr/src/app
COPY main.py /usr/src/app/main.py
COPY requirements.txt /usr/src/app/requirements.txt
COPY src /usr/src/app/src
RUN pip install -r requirements.txt
CMD [ "python3","-u","/usr/src/app/main.py"]