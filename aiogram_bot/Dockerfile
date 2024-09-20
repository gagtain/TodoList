FROM --platform=linux/amd64 python:3.10.6

COPY bot/requirements.txt /temp/requirements.txt
WORKDIR /APP

COPY bot/ /APP

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN pip install -r /temp/requirements.txt
