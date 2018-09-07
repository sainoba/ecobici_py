from urllib.request import urlopen
import json
import time

ACCESS_TOKEN_URL = "https://pubsbapi.smartbike.com/oauth/v2/token?client_id={id}&client_secret={secret}&grant_type=client_credentials"
REFRESH_TOKEN_URL = "https://pubsbapi.smartbike.com/oauth/v2/token?client_id={id}&client_secret={secret}&grant_type=refresh_token&refresh_token={token}"
API_URL = "https://pubsbapi.smartbike.com/api/v1/{api_section_and_method}?access_token={token}"

STATIONS_SECTION = "stations"
STATIONS_METHOD = "stations.json"
STATIONS_STATUS_METHOD = "status.json"


def _get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


class Ecobici:
    def __init__(self, client_id: str, client_secret: str):
        self.__id: str = client_id
        self.__secret: str = client_secret
        self.__token: dict = None
        self.__token_expires_at: int = int(time.time())
        self.__token = self.__refresh_token_if_invalid()

    @property
    def token(self) -> dict:
        expires_in = max(0, int(time.time() - self.__token_expires_at))
        self.__token["expires_in"] = expires_in
        return self.__token

    def __get_token(self, refresh_token: str = None) -> dict:
        if refresh_token is not None:
            url_params = {"id": self.__id, "secret": self.__secret, "token": refresh_token}
            url = REFRESH_TOKEN_URL
        else:
            url_params = {"id": self.__id, "secret": self.__secret}
            url = ACCESS_TOKEN_URL
        url = url.format(**url_params)
        token = _get_jsonparsed_data(url)
        self.__token_expires_at = int(time.time()) + token["expires_in"]
        return token

    def __refresh_token_if_invalid(self, seconds: int = 0, force: bool = False) -> dict:
        expired = int(time.time()) + seconds >= self.__token_expires_at
        if expired or force:
            token = self.__get_token()
        else:
            token = self.__get_token(self.token["refresh_token"])
        return token

    def refresh_token(self):
        self.__token = self.__refresh_token_if_invalid(force=True)
        return self.token

    def get_stations_list(self):
        self.__refresh_token_if_invalid(10)
        url_params = {"api_section_and_method": STATIONS_METHOD, "token": self.token["access_token"]}
        url = API_URL.format(**url_params)
        response = _get_jsonparsed_data(url)
        return response

    def get_stations_status(self):
        self.__refresh_token_if_invalid(10)
        url_params = {"api_section_and_method": "/".join([STATIONS_SECTION, STATIONS_STATUS_METHOD]),
                      "token": self.token["access_token"]}
        url = API_URL.format(**url_params)
        response = _get_jsonparsed_data(url)
        return response
