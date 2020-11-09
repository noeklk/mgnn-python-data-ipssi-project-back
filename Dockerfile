FROM python:3.6.1-alpine
RUN apk update \
  && apk add \
    build-base \
    postgresql \
    postgresql-dev \
    libpq
WORKDIR /src/
COPY ./requirements.txt .
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
COPY . .