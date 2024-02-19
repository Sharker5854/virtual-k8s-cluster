FROM nginx:latest

RUN rm -f /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./mathematic.conf /etc/nginx/conf.d/mathematic.conf

EXPOSE 80