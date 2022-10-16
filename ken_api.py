from pydoc import describe
import datetime
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


def __APCA_get(type: str, path: str, headers={
    'APCA-API-KEY-ID': APCA_API_KEY_ID,
    'APCA-API-SECRET-KEY': APCA_API_SECRET_KEY,
}) -> dict:
    return requests.get((API_DOMAIN if type == "api" else DATA_DOMAIN) + path, headers=headers)


def __validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


# API_DOMAIN = "https://api.alpaca.markets"
API_DOMAIN = "https://paper-api.alpaca.markets"
DATA_DOMAIN = "https://data.alpaca.markets"


def download_symbols(path: str = "./") -> dict | int:
    """
    downloads a all symbols to ./symbols_list in the same directory, symbols_list.\n
    \t:param str path: Path to the download, default directory is module directory.
    """
    res = __APCA_get("api", '/v2/assets')
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
        res = __APCA_get("api", '/v2/assets/' + str(symbol))
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


def get_bars(symbol, **kwargs)->list|int:
    """
    \t:param str symbol: Symbol of asset\n
    \t:param str start: starting date YYYY-MM-DD (optional)\n
    \t:param str end: ending date YYYY-MM-DD (optional)\n
    \t:param int limit: limit candle sticks (optional)\n
    \tcandle output\n
    \t\tt\tstring/timestamp	Timestamp in RFC-3339 format with nanosecond precision\n
    \t\to\tnumber\tOpen price\n
    \t\th\tnumber\tHigh price\n
    \t\tl\tnumber\tLow price\n
    \t\tc\tnumber\tClose price\n
    \t\tv\tint	Volume\n
    \t\tn\tint\tNumber of trades\n
    \t\tvw\tnumber\tVolume-weighted average price\n
    """
    query_str = ""
    if "start" in kwargs:
        __validate_date(kwargs["start"])
        query_str += "&start=" + kwargs["start"]
    if "end" in kwargs:
        __validate_date(kwargs["end"])
        query_str += "&end=" + kwargs["end"]
    if "limit" in kwargs:
        try:
            int(kwargs["limit"])
            query_str += "&limit=" + str(kwargs["limit"])
        except ValueError:
            raise ValueError("limit has to be an int")
    res = __APCA_get(
        "data", f"/v2/stocks/{symbol}/bars?timeframe=1day" + query_str)
    if res.status_code == 404:
        return 404
    if res.status_code != 200:
        return res.status_code
    res = res.json()
    if res["bars"]:
        return res["bars"]
    else:
        return 404


