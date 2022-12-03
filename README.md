# Pythonflask app

## Source (dir)
Contains everything related to flask apps
1. Source code
2. Requirement file
3. Dockerfile

### Dockerfile
Use this to build pythonflask app image. 
> Execute following command to build the docker imag
```
# If you are not under source dir
cd source
docker build --tag pythonflask .
```

> Execute following command to start a container
```
docker run -d -p 5000:5000 pythonflask
```

> Access application by writing following in the browser

```
http://localhost:5000
```