from datetime import date, datetime, timedelta
from multiprocessing.sharedctypes import Value
from random import choice
from statistics import mean
import ken_api
import numpy as np
import json
import plotly.offline as of
import plotly.graph_objects as go
# import plotly.express as px
import csv
import os
import pandas as pd
api = ken_api.api("PKO")

path = os.path.dirname(os.path.realpath(__file__))


class hammer:
    """
    Backtester class.
    attr str symbol: symbol name
    attr str db_path: path to your csv file
    """

    def __init__(self, symbol: str, db_path: str, config={}):
        self.config = {
            "entry_trace": 5 if not "entry_trace" in config else config["entry_trace"],
            "line_break": 0.7 if not "line_break" in config else config["line_break"],
            "stop_loss": -0.08 if not "stop_loss" in config else config["stop_loss"],
            "profit_cap": 0.08 if not "profit_cap" in config else config["profit_cap"],
        }
        self.df = pd.read_csv(db_path)
        self.df.length = self.df.shape[0]
        self.symbol = symbol
        self.holding = False
        self.entry = []
        # print(self.config)

    def openAttempt(self, index: int) -> bool:  # check entry conditions
        # print(self.df.iloc[index-6:index-1])
        if isinstance(index, str):
            index = self.df.index[self.df['t'] ==
                                  "2022-11-28T05:00:00Z"].tolist()[0] + 2

        open = self.df.o[index]
        close = self.df.c[index]
        low = self.df.l[index]
        high = self.df.h[index]
        # these are the opening conditions
        if not((open-low >= 2*(close-open) and high-close <= close-open and close-open > 0) or ((close-low) >= 2*(open-close) and high-open <= open-close and open-close > 0)):
            return False
        old, new, b = None, 0.0, 0.0
        # repeat trace back 4 times from the first candle to count (index - 1)
        for i in range(self.config["entry_trace"]-1):
            new, b = self.best_fit_line(np.array(self.df.c[index-2-i:index].tolist(), dtype=np.float64), np.array(list(range(index-2-i, index)), dtype=np.float64))  # nopep8
            if (old != None and old != 0) and (abs((new - old) / old) >= self.config["line_break"]):
                return False
            old = new
        if new >= 0:
            return False
        self.holding = True
        # print(new)
        return {
            "type": "Entry",
            "Symbol": self.symbol,
            "AX": self.df.t[index],
            "BX": self.df.t[index - 1][0:10],
            "CX": self.df.t[index - self.config["entry_trace"] - 1][0:10],
            "AY": self.df.o[index],
            "BY": b + (new * (index-1)),
            "CY": b + (new * (index-self.config["entry_trace"] - 1)),
            "reason": [],
            "price": self.df.o[index],
            "ROI": 0,
            "index": index
        }

    # check entry conditions
    def closeAttempt(self, index: int | str, entry_price: float = "") -> bool:
        """
        attempt an exit
        \t:param str index: Index of today in dataframe or date in YYYY-MM-DD format\n
        \t:param float index: Latest price of entry. (optional)\n
        """
        # print(self.df.iloc[index-6:index-1])
        if isinstance(index, str):
            index = self.df.index[self.df['t'] ==
                                  "2022-11-28T05:00:00Z"].tolist()[0]+2
        open = self.df.o[index]
        close = self.df.c[index]
        high = self.df.h[index]
        if entry_price == "":
            entry_price = self.entry[len(self.entry)-1]["price"]
        ROI = (close - entry_price) / entry_price
        conditions = [
            ROI > self.config["profit_cap"] or ROI < self.config['stop_loss'],
            # (high-open >= 2*(open-close) and open-close > 0) or (high-close >= 2*(close-open) and close-open > 0)  # nopep8
        ]
        if any(conditions):
            print(conditions)
            self.holding = False
            return {
                "type": "Exit",
                "Symbol": self.symbol,
                "AX": (datetime.strptime(self.df.t[index][0:10], '%Y-%m-%d') + timedelta(days=1) if index + 1 == len(self.df) else self.df.t[index + 1][0:10]),
                "BX": 0,
                "CX": 0,
                "AY": self.df.o[index + 1] if not index + 1 == len(self.df) else self.df.o[index],
                "BY": 0,
                "CY": 0,
                "reason": conditions,
                "price": self.df.o[index + 1] if not index + 1 == len(self.df) else self.df.o[index],
                "ROI": ((self.df.o[index + 1] if not index + 1 == len(self.df) else self.df.o[index] - entry_price)/entry_price)-1,
                "index": index
            }
        return False

    def best_fit_line(self, ys: list, xs: list) -> tuple[float, float]:
        m = (len(xs) * sum(np.multiply(xs, ys)) - sum(xs)*sum(ys)) / ((len(xs) * sum(np.square(xs))) - pow(sum(xs), 2))  # nopep8
        # m = (len(xs) * sum(xs * ys) - sum(xs)*sum(ys)) / (len(xs) * pow(sum(xs), 2) - pow(sum(xs), 2))  # nopep8
        # print(m)
        b = (sum(ys) - m*sum(xs))/len(xs)
        # print(m)
        # m = (((mean(xs) * mean(ys)) - mean(xs * ys)) / ((mean(xs) * mean(xs)) - mean(xs * xs)))  # nopep8
        # this is slope
        # b = mean(ys) - m*mean(xs)
        # this is offset
        return m, b

    def get_logs(self):
        return self.entry

    def get_ROI(self):
        return 0 if self.entry == [] else sum(x["ROI"] for x in [x for x in self.entry if x["type"] == "Exit"])

    def backtest(self):
        self.entry = [{
            "type": "Dummy",
            "Symbol": "Dummy",
            "AX": 0,
            "BX": 0,
            "CX": 0,
            "AY": 0,
            "BY": 0,
            "CY": 0,
            "reason": [False, False],
            "price": 0,
            "ROI": 0,
            "index": 0
        }]
        # for index, row in self.df.iterrows():
        for index in range(self.config["entry_trace"] + 1, len(self.df)):
            # if index == 20:
            if self.holding:
                attempt = self.closeAttempt(index)
                if attempt:
                    self.entry.append(attempt)
            else:
                attempt = self.openAttempt(index)
                if attempt:
                    self.entry.append(attempt)
        # for x in self.entry:
        #     print(x)
