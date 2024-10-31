FROM python:3.9-slim AS builder

WORKDIR /app

RUN useradd -ms /bin/bash appuser

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /code/app
