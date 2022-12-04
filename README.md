# Table of Content
1. [Source(dir)](#source)
2. [Database](#db)
3. [Assumptions/Improvements](#assumptions)
4. [How to run](#howtorun)

<div id="source">

# Source (dir)
Contains everything related to flask apps
1. Source code
    1.1 Contains code for apps, sampledata, static files, tempaltes, tests, requirements, Dockerfile, SQLite DB
2. Requirement file
    2.1 Contains python module dependancy
3. Dockerfile
    3.1 To build docker image for this application

<div id="db">

# Database/Tables
This simple application contains two tables, __ship__ and __shippositions__

## SHIPS
```
CREATE TABLE "ships" (
    "index" INTEGER,
    "imo" INTEGER,
    "shipname" TEXT
)
# CREATE INDEX "ix_ships_index"ON "ships" ("index")
```

## SHIPSPOSITIONS
```
CREATE TABLE "shipsposition" (
    "index" INTEGER,
    "imo" INTEGER,
    "datetime" TEXT,
    "latitude" REAL,
    "longitude" REAL
)
# CREATE INDEX "ix_shipsposition_index"ON "shipsposition" ("index")
```

<div id="assumptions">

# Assumptions/Improvements
Made following assumptions for this app

1. I've used the sampledata, inlcuded under __source\sampledata__.
2. Index.html was not available so created simple index.html to show initial data.
3. User has python installed and knows how to create virtualenv
4. Executed basic tests to verify, doesnt include extensive test suite
5. Security of the app is not considered entirely, app can be improved from that apsects
6. Application can be improivde further for higher data load (using cache etc)
7. Tables are kept very simple without any constraint of foreign key, which can be improved for actual running applicatoin. (E.g. shipsposition.imo should be FK of ships.imo)
8. For production grade application more validation should be added

<div id="howtorun">

# How to start the application and access endpoints

Clone the application to your local environment into one directory

## Using Dockerfile

1. Build docker image
    Use this to build pythonflask app image. Execute following command to build the docker imag
    ```
    # If you are not under source dir
    cd source
    docker build --tag pythonflask .
    ```

2. Once image building is successful, start the docker container
    ```
    docker run -d -p 5000:5000 pythonflask
    ```
Go to section [Access required endpoints](#access) 
    
## Using Flask standalon application

1. Create virtual environment and activate
    ```
    # Go to dir, where repo was cloned
    virtualenv appenv
    source /appenv/Scripts/activate
    ```
2. Install required python dependancies
    ```
    # Go to source directory
    pip install -f requirements.txt
    ```
3. Start Flask application
    ```
    python app.py
    ```
Go to section [Access required endpoints](#access)

<div id="access">

## Access required endpoints

Once you have started the application either usign Docker or as standalone application

1. Enter following URL into your browser, once docker cotnainer is started

    ```
    http://localhost:5000
    ```
    This will give you the index page. This page doesnt have any functionalities but it will display ship data loaded from sampledata.

2. Try out required endpoints
    
    Application exposes two endpoitns as required.

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