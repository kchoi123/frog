FROM nginx

# RUN rm /usr/share/nginx/html/index.html

# COPY * /usr/share/nginx/html/

WORKDIR /

# RUN rm -rf /docker-entrypoint.sh

COPY ./docker-entrypoint.sh ./docker-entrypoint.sh

RUN ["chmod", "+x", "./docker-entrypoint.sh"]

# RUN echo "echo Hello frog! I am answering you from Docker Container: $HOSTNAME >> /usr/share/nginx/html/index.html"