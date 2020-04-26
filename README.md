# flaskBack

## Working with virtualenv

### Install

```bash
pip install virtualenv
virtualenv venv
```

### Activate:

```bash
 source venv/bin/activate
```

### Deactivate:

```bash
deactivate
```

### Export PYTHONPATH

```bash
export PYTHONPATH="$PWD"
```

## Steps for docker

### To build docker image

```bash
docker build -t flaskback:1.0 .
```

### To create the container using the image

```bash
docker run -it -p 8888:8888 -v $(pwd)/src:/app/src --name flaskback flaskback:1.0
docker run -it -p 8888:8888 --name flaskback flaskback
```

### To run the created container

```sh
docker start flaskback
```
