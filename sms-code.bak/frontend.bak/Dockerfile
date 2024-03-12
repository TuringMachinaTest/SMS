# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM docker.io/library/node:lts-alpine

RUN mkdir /code
WORKDIR /code

RUN npm install -g @angular/cli@13

# COPY package.json package-lock.json ./
# RUN npm ci

COPY . /code/

