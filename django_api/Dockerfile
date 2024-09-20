FROM --platform=linux/amd64 python:3.10.6

COPY api/requirements.txt /temp/requirements.txt
WORKDIR /APP

COPY api/* /APP

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --upgrade pip
RUN pip install -r /temp/requirements.txt
