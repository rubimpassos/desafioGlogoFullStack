FROM node:16-buster-slim

WORKDIR /app

COPY ./frontend/package.json /app
COPY ./frontend/yarn.lock /app

RUN npm install -g yarn@1.22.17 --force
RUN yarn install && yarn cache clean --force

ENV PATH ./node_modules/.bin/:$PATH
