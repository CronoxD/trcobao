FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /app

COPY ./frontend /app/

RUN npm install /app/