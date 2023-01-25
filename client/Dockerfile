# Build The React Code 
FROM node:16.14-alpine AS builder

WORKDIR /client 

COPY package.json ./ 

COPY yarn.lock ./

RUN yarn install 

COPY src ./src

COPY public ./public

COPY .babelrc ./
COPY webpack.prod.config.js ./
COPY postcss.config.js ./
COPY tailwind.config.js ./
COPY ./constant.js ./


RUN yarn run build



FROM nginx:latest

WORKDIR /client

COPY web_server.conf /etc/nginx/conf.d/default.conf

COPY --from=builder /client/build /client/build