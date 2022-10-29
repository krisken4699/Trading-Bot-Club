from datetime import date, datetime, timedelta
from statistics import mean
import ken_api
import numpy as np
import plotly.graph_objects as go
# import plotly.express as px
import csv
import pandas as pd
api = ken_api.api()


def downloadCandles(symbol: str, start: str, end: str = None):
    # print(symbol, start,end)
    """
        downloads a all candles to ./<Symbol>_history in the same directory.\n
        \t:param str symbol: Symbol
        \t:param str start: Start date of the history you want to retrieve.
    """
    # print(str(datetime.date.today()))
    to_csv = (api.get_bars(symbol, start=start))
    # to_csv = client.get_bars("TSLA", end="2022-10-25", start="2021-02-01")
    keys = to_csv[0].keys()
    with open('datasets/' + symbol + '_History.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(to_csv)


# downloadCandles("TSLA", "2015-12-01")


def show_graph(entry: dict):

    df = pd.read_csv('./datasets/TSLA_History.csv')
    fig = go.Figure(data=[go.Candlestick(x=df['t'],
                    open=df['o'],
                    high=df['h'],
                    low=df['l'],
                    close=df['c'])])
    for i in range(len(entry)):
        points = entry[i]
        fig.add_trace(go.Scatter(x=[points["AX"], points["BX"]],
                                 y=[points["AY"], points["BY"]],
                                 #  xperiod="M1",
                                 #  xperiodalignment="middle",
                                 name=f"Entry {i} index: {points['index']}", line_shape='linear'))
    # fig.update_traces(hoverinfo='text+name')
    # fig.update_traces(hoverinfo='text+name', mode='lines+markers')
    fig.show()


class hammer:
    """
    Backtester class.
    constructor str db_path: path to your csv file
    """

    def __init__(self, symbol: str, db_path: str):
        self.df = pd.read_csv(db_path)
        self.df.length = self.df.shape[0]
        self.symbol = symbol
        self.entry = []

    def openAttempt(self, index: int) -> None:  # check entry conditions
        # print(self.df.iloc[index-6:index-1])
        open = self.df.o[index]
        close = self.df.c[index]
        low = self.df.l[index]
        # if not(close-low >= 2 * abs(close-open) or open-low >= 2 * abs(close-open)):
        # if not(close-low >= 2 * abs(close-open) or open-low >= 2 * abs(close-open)):
        # these are the opening conditions
        if not((open-low >= 2*(close-open) and close-open > 0) or (close-low >= 2*(open-close) and open-close > 0)):
            return False
        # print(open-low, 2*(close-open))
        # print(close-low, 2*(open-close))
        old, new, b = None, 0.0, 0.0
        for i in range(4):  # repeat trace back 4 times from the first candle to count (index - 1)
            new, b = self.best_fit_line(np.array(self.df.c[index-2-i:index].tolist(), dtype=np.float64), np.array(list(range(index-2-i, index)), dtype=np.float64))  # nopep8
            # new, b = self.best_fit_line(np.array(self.df.c[index-3-i:index-1].tolist(), dtype=np.float64), np.array(list(range(index-2-i, index)), dtype=np.float64))  # nopep8
            # new, b = self.best_fit_line(np.array(self.df.c[index-3-i:index-1].tolist(), dtype=np.float64), np.array(list(range(-2-i, 0)), dtype=np.float64))  # nopep8
            if (old != None) and (abs((new - old) / old) >= 0.5):
                return False
            old = new
        if new >= 0:
            return False
        # print(f"Best fit {i+1} = {new:.2f}x + {b:.2f}")
        # print(b, new)
        # print('Index:', index)
        # print(self.df.t[index-5:index].tolist())
        # print(f"{new *-6:.2f}", b)
        return {
            "AX": (datetime.strptime(self.df.t[index - 6][0:10], '%Y-%m-%d')),
            "BX": (datetime.strptime(self.df.t[index - 1][0:10], '%Y-%m-%d')),
            # "AX": (datetime.strptime(self.df.t[0][0:10], '%Y-%m-%d') + timedelta(days=index-1)).strftime('%Y-%m-%d'),
            # "BX": (datetime.strptime(self.df.t[0][0:10], '%Y-%m-%d') + timedelta(days=index-6)).strftime('%Y-%m-%d'),
            "AY": b + (-new*index),
            "BY": b + (new * -6 * index),
            # "AY": b + (new * (index-1)),
            # "BY": b + (new * (index-6)),
            "index": index
        }

    def best_fit_line(self, ys: list, xs: list) -> tuple[float, float]:
        m = (len(xs) * sum(xs * ys) - sum(xs)*sum(ys)) / (len(xs) * pow(sum(xs), 2) - pow(sum(xs), 2))  # nopep8
        b = (sum(ys) - m*sum(xs))/len(xs)
        # print(m)
        # m = (((mean(xs) * mean(ys)) - mean(xs * ys)) / ((mean(xs) * mean(xs)) - mean(xs * xs)))  # nopep8
        # this is slope
        # b = mean(ys) - m*mean(xs)
        # this is offset
        return m, b

    def backtest(self):
        def main():  # main thread
            # for index, row in self.df.iterrows():
            for index in range(6, len(self.df)):
                # if index == 20:
                attempt = self.openAttempt(index)
                if attempt:
                    self.entry.append(attempt)

            # for x in self.entry:
            #     print(x)
            show_graph(self.entry)

        main()


hammer("TSLA", './datasets/TSLA_History.csv').backtest()
