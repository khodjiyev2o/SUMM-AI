# syntax=docker/dockerfile:1
FROM  --platform=linux/amd64 python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY ./requirements.txt ./

RUN pip install --no-deps -r requirements.txt

RUN apt update 

COPY ./ .


CMD ["python","manage.py","runserver","0.0.0.0:8000"]