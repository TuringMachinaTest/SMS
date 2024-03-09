FROM docker.io/library/nginx:1.25

RUN mkdir /backend
RUN mkdir /frontend

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d