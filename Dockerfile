FROM alpine:3.10

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /app
COPY . /app

RUN pip3 --no-cache-dir install -r requeriments.txt \
    && export PYTHONPATH="$PWD"

CMD ["python3", "src/app.py"]