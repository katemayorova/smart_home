FROM python:3.8-bullseye

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ./docker-entrypoint.sh
