# Para Build -> docker-compose up --build
# Para Rodar Ambiente -> docker-compose exec app bash

FROM python:3.10.1-slim
RUN useradd -ms /bin/bash python
USER python
WORKDIR /home/python/app
ENV PYTHONPATH=${PYTHONPATH}/home/python/app/src
CMD [ "tail", "-f", "/dev/null" ]
