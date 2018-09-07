import pytest
from ecobici import Ecobici
import os
from urllib.error import HTTPError

CLIENT_ID: str = os.getenv("CLIENT_ID")
CLIENT_SECRET: str = os.getenv("CLIENT_SECRET")


@pytest.fixture
def ecobici():
    return Ecobici(CLIENT_ID, CLIENT_SECRET)


def test_ecobici_creation():
    Ecobici(CLIENT_ID, CLIENT_SECRET)
    with pytest.raises(HTTPError):
        Ecobici("", "")


def test_refresh_token(ecobici):
    token = ecobici.token
    ecobici.refresh_token()
    new_token = ecobici.token
    assert token["access_token"] != new_token["access_token"], "Tokens should be different"


def test_get_stations_list(ecobici):
    response = ecobici.get_stations()
    assert "stations" in response, "Didn't get the correct response"


def test_get_stations_status(ecobici):
    response = ecobici.get_stations_status()
    assert "stationsStatus" in response, "Didn't get the correct response"
