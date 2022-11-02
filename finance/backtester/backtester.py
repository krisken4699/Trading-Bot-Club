from datetime import date, datetime, timedelta
from multiprocessing.sharedctypes import Value
from random import choice
from statistics import mean
import ken_api
import numpy as np
import plotly.offline as of
import plotly.graph_objects as go
# import plotly.express as px
import csv
import pandas as pd
api = ken_api.api()

symbol_list = ["SQ", "SHOP", "NET", "COIN", "GTLB", "HCP", "DLO", "ASAN", "W", "LAC", "FTCH", "MSTR", "CVNA", "AUR",
               "STEM", "PACB", "RIOT", "UUUU", "AMPX", "AMRS", "BNGO", "VLD", "DOMO", "AEHR", "NOTV", "SKLZ", "BBBY", "CORZ"]


def downloadCandles(symbol: str, start: str, end: str = None):
    # print(symbol, start,end)
    """
        downloads a all candles to ./<Symbol>_history in the same directory.\n
        \t:param str symbol: Symbol
        \t:param str start: Start date of the history you want to retrieve.
    """
    # print(str(datetime.date.today()))
    to_csv = (api.get_bars(symbol, start=start))
    # to_csv = client.get_bars("SQ", end="2022-10-25", start="2021-02-01")
    keys = to_csv[0].keys()
    with open('datasets/' + symbol + '_History.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(to_csv)


def show_graph(entry: dict, symbol: str):
    colors = ["#B4B4B3", '#C7C7C7', '#D4CCCC']
    df = pd.read_csv(f'./datasets/{symbol}_History.csv')
    fig = go.Figure(data=[go.Candlestick(x=df['t'],
                    name=f"{symbol} Candle",
                    open=df['o'],
                    high=df['h'],
                    low=df['l'],
                    close=df['c'])])
    fig.update_layout(
        title={
            "text": f"{symbol} History",
            "font": {
                # "family": "Overpass",
                "color": "#D4CCCC"
            }
        },
        yaxis_title='USD ($)',
        paper_bgcolor="#2a322e",
        # margin={"l": 0, "r": 0, "t": 10, "b": 20},
        plot_bgcolor="#202020",
        font_color="#F7F7F7",
        font_family="arial",
        legend_title_font_color="green",
        legend={
            "bgcolor": '#979797',
            "bordercolor": '#F7F7F7'
        }
    )
    fig.update_xaxes(
        gridcolor="#C7C7C7",
        gridwidth=1
    )
    fig.update_yaxes(
        gridcolor="#D4CCCC"
    )
    for points in entry:
        if points["type"] == "Entry":
            fig.add_trace(go.Scatter(x=[points['CX']],
                                     y=[points["CY"]],
                                     line={'color': '#0ff'},
                                     name=f"Entry: {points['index']}", line_shape='linear'))
            fig.add_trace(go.Scatter(x=[points["AX"], points["BX"]],
                                     y=[points["AY"], points["BY"]],
                                     #  xperiod="M1",
                                     #  xperiodalignment="middle",
                                     line={'color': '#fff'},
                                     #  line={'color':choice(colors)},
                                     name=f"5 fit line {points['index']}", line_shape='linear'))
        else:
            fig.add_trace(go.Scatter(x=[points['AX']],
                                     y=[points["AY"]],
                                     line={'color': '#ff0' if points["reason"][0] else '#f90'},
                                     name=f"Exit: {points['index']}\nROI:{points['ROI']:.2f} ", line_shape='linear'))
    # fig.update_traces(hoverinfo='text+name')
    # fig.update_traces(hoverinfo='text+name', mode='lines+markers')
    fig.show(config={'displayModeBar': False})
    # fig.write_html(f'./{symbol}_graph.html', config={'displayModeBar': False})
    # print(of.plot(fig, include_plotlyjs=False, output_type='div'))


class hammer:
    """
    Backtester class.
    attr str symbol: symbol name
    attr str db_path: path to your csv file
    """

    def __init__(self, symbol: str, db_path: str, config={}):
        self.config = {
            "entry_trace": 5 if not "entry_trace" in config else config["entry_trace"],
            "line_break": 0.5 if not "line_break" in config else config["line_break"],
            "stop_loss": -0.8 if not "stop_loss" in config else config["stop_loss"],
            "profit_cap": 0.8 if not "profit_cap" in config else config["profit_cap"],
        }
        self.df = pd.read_csv(db_path)
        self.df.length = self.df.shape[0]
        self.symbol = symbol
        self.holding = False
        self.entry = []
        # print(self.config)

    def openAttempt(self, index: int) -> bool:  # check entry conditions
        # print(self.df.iloc[index-6:index-1])
        open = self.df.o[index]
        close = self.df.c[index]
        low = self.df.l[index]
        # these are the opening conditions
        if not((open-low >= 2*(close-open) and close-open > 0) or (close-low >= 2*(open-close) and open-close > 0)):
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
        return {
            "type": "Entry",
            "AX": datetime.strptime(self.df.t[index - self.config["entry_trace"] - 1][0:10], '%Y-%m-%d'),
            "BX": datetime.strptime(self.df.t[index - 1][0:10], '%Y-%m-%d'),
            "CX": self.df.t[index],
            "AY": b + (new * (index-self.config["entry_trace"] - 1)),
            "BY": b + (new * (index-1)),
            "CY": self.df.o[index],
            "price": self.df.o[index],
            "index": index
        }

    def closeAttempt(self, index: int) -> bool:  # check entry conditions
        # print(self.df.iloc[index-6:index-1])
        open = self.df.o[index]
        close = self.df.c[index]
        high = self.df.h[index]
        entry_price = self.entry[len(self.entry)-1]["price"]
        ROI = (open - entry_price) / entry_price
        conditions = [
            ROI > self.config["profit_cap"] or ROI < self.config['stop_loss'],
            (high-open >= 2*(open-close) and open-close > 0) or (high-close >= 2*(close-open) and close-open > 0)  # nopep8
        ]
        if any(conditions):
            self.holding = False
            return {
                "type": "Exit",
                "reason": conditions,
                "ROI": ROI,
                "price": self.df.o[index],
                "AX": datetime.strptime(self.df.t[index][0:10], '%Y-%m-%d') + timedelta(days=1) if index + 1 == len(self.df) else self.df.t[index + 1][0:10],
                "AY": self.df.o[index + 1] if not index + 1 == len(self.df) else self.df.o[index],
                "index": index
            }

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

    def get_ROI(self):
        return 0 if self.entry == [] else sum(x["ROI"] for x in [x for x in self.entry if x["type"] == "Exit"])

    def backtest(self):
        self.entry = []
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
        show_graph(self.entry, self.symbol)


def main():
    symbol_roi = []
    # for symbol in symbol_list:
    # print(symbol)
    # downloadCandles(symbol, "2015-12-01")
    # hammer(symbol, f'./datasets/{symbol}_History.csv').backtest()
    for symbol in symbol_list:
        downloadCandles(symbol, "2015-12-01")
        temp = hammer(
            symbol, f'./datasets/{symbol}_History.csv')
        temp.backtest()
        symbol_roi.append({"symbol": symbol, "ROI": temp.get_ROI()})
    print(mean([x["ROI"] for x in symbol_roi]))
    # for roi in symbol_roi:
    #     if roi['ROI'] >= 1:
    #         print(roi)


main()
