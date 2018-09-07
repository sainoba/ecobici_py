# Ecobici python wrapper

[![Build Status](https://travis-ci.com/sainoba/ecobici_py.svg?branch=master)](https://travis-ci.com/sainoba/ecobici_py)
[![PyPI version](https://badge.fury.io/py/ecobici.svg)](https://badge.fury.io/py/ecobici)
![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)

![Ecobici logo](./img/ecobici.jpg)

This is a simple example package. You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## Installation
`pip install ecobici`

## Usage

```python3
# Import module
from ecobici import Ecobici

# Initialize client
client = Ecobici(your_client_id, your_client_secret)

# Get list of stations
list_of_stations = client.get_stations_list()

# Get status of stations
stations_status = client.get_stations_status()

# (Optional) Force refresh token
client.refresh_token()

```

## Notes
There's no need to refresh the token when it expires. The client does it automatically.
