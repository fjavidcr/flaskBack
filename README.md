# flaskBack

## Working with virtualenv

### Install
```
pip install virtualenv
virtualenv venv
```

### Activate:
``` 
 source venv/bin/activate
```

### Deactivate:
```
deactivate
```

## Steps for docker

### To build docker image
```shell
docker build -t flaskback .
```
### To create the container using the image
```shell
docker run -it -p 8888:8888 -v $(pwd)/src:/app/src --name flaskback flaskback
docker run -it -p 8888:8888 --name flaskback flaskback
```
### To run the created container
```sh
docker start flaskback
```