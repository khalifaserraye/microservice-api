# pull the official docker image
FROM python:3.11.2-slim
# set work directory
WORKDIR /microserv
# set env variables
ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1
# install dependencies
COPY ./requirements.txt /microserv/requirements.txt
RUN pip install -r requirements.txt
# copy project
COPY ./microserv_api/ /microserv/microserv_api/