# Pythonflask app



### Dockerfile
Use this to build pythonflask app image. 
> Execute following command to build the docker imag
```
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