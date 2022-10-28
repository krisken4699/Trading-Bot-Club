import datetime
import requests
import os

dir_path = os.getcwd()
# print(dir_path)
# with open(dir_path + '/alpaca_credentials.json') as credentials:
#     data = json.load(credentials)
#     APCA_API_KEY_ID = data["APCA-API-KEY-ID"]
#     APCA_API_SECRET_KEY = data["APCA-API-SECRET-KEY"]

API_DOMAIN = "https://paper-api.alpaca.markets"
DATA_DOMAIN = "https://data.alpaca.markets"


class api:
    """
    This class requires 2 params:\n
    \t:params str APCA_API_KEY_ID: Your api key for Alpaca.\n
    \t:params str APCA_API_SECRET_KEY: Your api secret for Alpaca.  
    """

    def __init__(self, APCA_API_KEY_ID: str = 'PKNOZUSMT0A6E89QURCG', APCA_API_SECRET_KEY: str = "SXFTc5gC4cAWmUpuGEiEurBGfN4bAqhA6Mxu28Ez"):
        self.API_DOMAIN = "https://paper-api.alpaca.markets"
        self.DATA_DOMAIN = "https://data.alpaca.markets"
        self.APCA_API_KEY_ID, self.APCA_API_SECRET_KEY = APCA_API_KEY_ID, APCA_API_SECRET_KEY

    def __APCA_get__(self, type: str, path: str, headers=None) -> dict:
        if not headers:
            headers = {
                'APCA-API-KEY-ID': self.APCA_API_KEY_ID,
                'APCA-API-SECRET-KEY': self.APCA_API_SECRET_KEY,
            }
        return requests.get((API_DOMAIN if type == "api" else DATA_DOMAIN) + path, headers=headers)

    def __str__(self):
        return str({"lib path": dir_path, "domains": [API_DOMAIN, DATA_DOMAIN], "APCA_API_KEY_ID": self.APCA_API_KEY_ID})

    def __validate_date(self, date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    def download_symbols(self, path: str = "./") -> dict | int:
        """
        downloads a all symbols to ./symbols_list in the same directory, symbols_list.\n
        \t:param str path: Path to the download, default directory is module directory.
        """
        res = self.__APCA_get__("api", '/v2/assets')
        if res.status_code == 404:
            return 404
        if res.status_code != 200:
            return res.status_code
        res = res.json()
        symbol_list = []
        if(path == ""):
            path = "."
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

    def get_assets(self, *symbols: str, **simple: bool) -> dict | int:
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
            res = self.__APCA_get__("api", '/v2/assets/' + str(symbol))
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

    def get_bars(self, symbol:str, **kwargs) -> list | int:
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
            self.__validate_date(kwargs["start"])
            query_str += "&start=" + kwargs["start"]
        if "end" in kwargs:
            self.__validate_date(kwargs["end"])
            query_str += "&end=" + kwargs["end"]
        if "limit" in kwargs:
            try:
                int(kwargs["limit"])
                query_str += "&limit=" + str(kwargs["limit"])
            except ValueError:
                raise ValueError("limit has to be an int")
        res = self.__APCA_get__(
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

    def get_positions(self, symbol: str = "") -> list | int:
        """
        Returns owned assets' info or a specific asset's info.
        \tparams str symbol: specific symbol of an asset you want to get the position.
        """
        positions = self.__APCA_get__("api", f"/v2/positions{ symbol }")
        if positions.status_code == 404:
            return 404
        if positions.status_code != 200:
            return positions.status_code
        return positions.json()

    def get_account(self) -> dict | int:
        """
        Return account information
        """
        account = self.__APCA_get__("api", f"/v2/account")
        if account.status_code == 404:
            return 404
        if account.status_code != 200:
            return account.status_code
        return account.json()
