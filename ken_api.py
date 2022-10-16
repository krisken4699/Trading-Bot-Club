
from pydoc import describe
import requests
import json
# from typing import Union
import os
global APCA_API_KEY_ID
global APCA_API_SECRET_KEY
APCA_API_KEY_ID = ""
APCA_API_SECRET_KEY = ""


# dir_path = os.path.dirname(os.path.abspath(os.getcwd()))
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '/alpaca_credentials.json') as credentials:
    data = json.load(credentials)
    APCA_API_KEY_ID = data["APCA-API-KEY-ID"]
    APCA_API_SECRET_KEY = data["APCA-API-SECRET-KEY"]


def __APCA_get(path, headers={
    'APCA-API-KEY-ID': APCA_API_KEY_ID,
    'APCA-API-SECRET-KEY': APCA_API_SECRET_KEY,
}):
    return requests.get(path, headers=headers)


# API_DOMAIN = "https://api.alpaca.markets"
API_DOMAIN = "https://paper-api.alpaca.markets"


def download_symbols(path: str = "./") -> dict | int:
    """
    downloads a all symbols to ./symbols_list in the same directory, symbols_list.\n
    \t:param str path: Path to the download, default directory is module directory.
    """
    res = __APCA_get(API_DOMAIN + '/v2/assets')
    if res.status_code == 404:
        return 404
    if res.status_code != 200:
        return res.status_code
    res = res.json()
    symbol_list = []
    if(path == ""):
        path = + "."
    if path[len(path)-1] != "/" and path[len(path)-1] != "\\":
        path += "/"
    with open(path + "symbols_list", "w", encoding="utf-8") as outfile:
        for asset in res:
            symbol_list.append(str(
                {
                    "symbol": asset["symbol"],
                    "name": asset["name"],
                    "class": asset['class'],
                    "id": asset["id"],
                    "status": asset['status'],
                }))
        symbol_list = "\n".join((symbol_list))
        outfile.write(symbol_list)
    return symbol_list


def get_assets(*symbols: str, **simple: bool) -> dict | int:
    """
    Returns a simple dict including symbol, name, class, id, and status\n
    \t:args str symbols: symbols to request for assets\n
    \t:optional bool simple: returns a simple format  
    """
    simple_ = False

    for key, value in simple.items():
        if(key == "simple" and value == True):
            simple_ = True
    symbol_list = []
    if symbols == ():
        symbols = [""]
    for symbol in symbols:
        res = __APCA_get(API_DOMAIN + '/v2/assets/' + str(symbol))
        if res.status_code == 404:
            return 404
        if res.status_code != 200:
            return res.status_code
        res = res.json()
        if simple_:
            symbol_list.append(str(
                {
                    "symbol": res["symbol"],
                    "name": res["name"],
                    "class": res['class'],
                    "id": res["id"],
                    "status": res['status'],
                }))
        else:
            symbol_list.append(str(res))
    symbol_list = "\n".join((symbol_list))

    return symbol_list
