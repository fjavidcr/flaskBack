FROM python:3.8-slim-buster

# RUN apk add --no-cache python3-dev build-base \
#    && pip3 install --upgrade pip

WORKDIR /app
COPY . /app

RUN pip3 --no-cache-dir install -r requeriments.txt 

CMD ["python3", "src/app.py"]