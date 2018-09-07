# Ecobici python wrapper

[![Build Status](https://travis-ci.com/sainoba/ecobici_py.svg?branch=master)](https://travis-ci.com/sainoba/ecobici_py)
[![PyPI version](https://badge.fury.io/py/ecobici.svg)](https://badge.fury.io/py/ecobici)
![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)

![Ecobici logo](https://raw.githubusercontent.com/sainoba/ecobici_py/master/img/ecobici.jpg)

## Installation
`pip install ecobici`

## Usage

```python
# Import module
from ecobici import Ecobici

# Initialize client
client = Ecobici(your_client_id, your_client_secret)

# Get dictionary containing stations
stations = client.get_stations()

# Get dictionary containing the status of stations
stations_status = client.get_stations_status()

# (Optional) Force refresh token
client.refresh_token()

```

### Examples
#### Get the name of the first station
```python
from ecobici import Ecobici
client = Ecobici(your_client_id, your_client_secret)
list_of_stations = client.get_stations()["stations"]

print("The name of the first station is ", list_of_stations[0]["name"])
```
[Check the Data structure section for more information](#data-structure)

#### Get the status of the third station
```python
from ecobici import Ecobici
client = Ecobici(your_client_id, your_client_secret)
list_of_stations = client.get_stations_status()["stationsStatus"]

print("The status of the third station is ", list_of_stations[3]["status"])
```
[Check the Data structure section for more information](#data-structure)

## Data structure
### Stations structure

The econduce's API returns data in the following json format:
```json
{
    "stations": [
        {
            "id": 448,
            "name": "448 DR. ANDRADE - ARCOS DE BELÉN",
            "address": "DR. ANDRADE ARCOS DE BELÉN",
            "addressNumber": "S/N",
            "zipCode": null,
            "districtCode": null,
            "districtName": null,
            "altitude": null,
            "nearbyStations": [
                448
            ],
            "location": {
                "lat": 19.426611,
                "lon": -99.14447
            },
            "stationType": "BIKE,TPV"
        }, ...
    ]
}
```
This module translate the json objects to python objects and returns it to the user,
it doesn't unwraps it because I didn't want to modify the data.

That's why you have to manually unwrap it: ```client.get_stations_status()["stations"]'```

|Key|Type|
|---|---|
|id|int|
|name|str|
|address|str|
|addressNumber|str|
|zipCode|str|
|districtCode|str|
|districtName|str|
|nearbyStations|list with id (int)|
|location|list|
|stationType|str|

Location list:

|Key|Type|
|---|---|
|lat|float|
|lon|float|

Latitud and logitud are coordinates based on the [World Geodetic System (WGS84)](https://es.wikipedia.org/wiki/WGS84).

### Status structure

The econduce's API returns data in the following json format:
```json
{
    "stationsStatus": [
        {
            "id": 1,
            "status": "OPN",
            "availability": {
                "bikes": 4,
                "slots": 23
            }
        }, ...
    ]
}      
```
This module translate the json objects to python objects and returns it to the user,
it doesn't unwraps it because I didn't want to modify the data.

That's why you have to manually unwrap it: ```client.get_stations_status()["stationsStatus"]'```

|Key|Type|
|---|---|
|id|int|
|status|str (OPN means open, CLS means closed)|
|availability|list|

Availability list:

|Key|Type|
|---|---|
|bikes|int|
|slots|int|

## Test 
`python3 -m pytest ecobici/test.py`

## Notes
- There's no need to refresh the token when it expires. The client does it automatically.
- Ecobici's API can return _null_ values. It's up to you to verify that the value you want to access if defined.
- You can find more information about the API structure here: [Spanish documentation](https://www.ecobici.cdmx.gob.mx/sites/default/files/pdf/manual_api_opendata_esp_final.pdf).
