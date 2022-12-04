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

> It has two endpoints available accessible as below

```
# Endpoint: /api/ships
# Shows data for available ships
http://localhost:5000/api/ships

# E.g.
{
    "ship": [
        {
            "imo": 9632179,
            "name": "Mathilde Maersk"
        },
        {
            "imo": 9247455,
            "name": "Australian Spirit"
        },
        {
            "imo": 9595321,
            "name": "MSC Preziosa"
        }
    ]
}
```

```
# Endpoint: /api/positions/<imo>
# Shows data about given IMO, includes latitue/longitude and descending order of time
# Replace <IMO> with actual IMO data
http://localhost:5000/api/positions/<IMO>

# E.g.
{
    "ship": {
        "imo": 9632179,
        "positions": [
            {
                "datetime": "2019-01-14 18:40:18+00",
                "latitude": 49.8978996276855,
                "longitude": -2.51836657524109
            },
            {
                "datetime": "2019-01-14 18:59:06+00",
                "latitude": 49.9175834655762,
                "longitude": -2.40604996681213
            }
        ]
    }
}
```