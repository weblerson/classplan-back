FROM python:3.11-slim

RUN mkdir /app
RUN mkdir /app/static
RUN mkdir /app/media
WORKDIR /app

ENV PYTHONUNBUFFERED 1

RUN apt update

RUN pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv --python 3.11
RUN pipenv install

COPY . .

EXPOSE 8000