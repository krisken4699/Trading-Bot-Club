import pandas as pd
import os
import csv
import plotly.graph_objects as go
import plotly.offline as of
import json
import numpy as np
from statistics import mean
from random import choice
from multiprocessing.sharedctypes import Value
from datetime import date, datetime, timedelta
from hammer import hammer
from ken_api import api
path = os.path.dirname(os.path.realpath(__file__))
# import plotly.express as px
api = api()


def downloadCandles(symbol: str, start: str, end: str = None):
    # print(symbol, start,end)
    """
        downloads a all candles to ./<Symbol>_history in the same directory.\n
        \t:param str symbol: Symbol
        \t:param str start: Start date of the history you want to retrieve.
    """
    # print(str(datetime.date.today()))
    to_csv = (api.get_bars(symbol, start=start, limit=10000))
    print(len(to_csv))
    # to_csv = client.get_bars("SQ", end="2022-10-25", start="2021-02-01")
    keys = to_csv[0].keys()
    with open(f'{path}/datasets/' + symbol + '_History.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(to_csv)


def main():
    today = None
    open(path+'/datasets/log.csv', 'w').truncate()

    with open(path+'/AppData.json') as f:
        data = json.load(f)
        today = data["date"] == datetime.now().strftime('%d/%m/%Y')
    for symbol in symbol_list:
        if not today:  # nopep8
            downloadCandles(symbol, "2015-12-01")
            print("Downloaded", symbol)
        temp = hammer(symbol, f'{path}/datasets/{symbol}_History.csv')
        res = api.get_positions(symbol)
        # print(type(res))
        if isinstance(res, dict):
            if "qty" in res:
                print(f"Symbol: {symbol}\tQuantity: {res['qty']}")
                attempt_result = temp.closeAttempt(datetime.now().strftime(
                    '%Y-%m-%d'), float(res["avg_entry_price"]))
                if attempt_result != False:
                    try:
                        print(api.place_order(symbol, res['qty'], "sell"))
                    except:
                        print("Failed to place order. Maybe an order already exists. Needs manuel check.")
            else:
                print(f"Symbol: {symbol}\tQuantity: 0")

    with open("AppData.json", "w") as jsonfile:
        json.dump({"date": datetime.now().strftime('%d/%m/%Y')}, jsonfile)


symbol_list = ['TSLA', 'AMD', 'CCL', 'NVDA', 'F', 'PLTR', 'PYPL', 'SNAP', 'MDB', 'ABNB', 'BX', 'RIVN', 'NFLX', 'RBLX',
          'MRVL', 'SNOW', 'AMAT', 'DDOG', 'MBLY', 'ENPH', 'TTD', 'CHWY', 'DASH', 'ZS', 'SE', 'KKR', 'ETSY', 'ZI',
          'TECK']
if __name__ == "__main__":
    main()