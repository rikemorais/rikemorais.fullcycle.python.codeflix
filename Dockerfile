# docker-compose up --build
# docker-compose exec app bash

FROM python:3.10.1-slim

RUN useradd -ms /bin/bash python

USER python

WORKDIR /home/python/app

CMD [ "tail", "-f", "/dev/null" ]