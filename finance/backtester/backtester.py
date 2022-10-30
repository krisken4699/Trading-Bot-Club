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

symbol_list = ["SQ","SHOP","NET","COIN","GTLB","HCP","DLO","ASAN","W","LAC","FTCH","MSTR","CVNA","AUR","STEM","PACB","RIOT","UUUU","AMPX","AMRS","BNGO","VLD","DOMO","AEHR","NOTV","SKLZ","BBBY","CORZ"]


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
    for i in range(len(entry)):
        points = entry[i]
        fig.add_trace(go.Scatter(x=[points["AX"], points["BX"]],
                                 y=[points["AY"], points["BY"]],
                                 #  xperiod="M1",
                                 #  xperiodalignment="middle",
                                 line={'color': '#fff'},
                                 #  line={'color':choice(colors)},
                                 name=f"Entry {i} index: {points['index']}", line_shape='linear'))
    # fig.update_traces(hoverinfo='text+name')
    # fig.update_traces(hoverinfo='text+name', mode='lines+markers')
    # fig.show(config={'displayModeBar': False})
    # fig.write_html(f'./{symbol}_graph.html', config={'displayModeBar': False})
    print(of.plot(fig, include_plotlyjs=False, output_type='div'))


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

        }
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
            if (old != None and old != 0) and (abs((new - old) / old) >= 0.5):
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
            # "AY": b + (-new*index),
            # "BY": b + (new * -6 * index),
            "AY": b + (new * (index-6)),
            "BY": b + (new * (index-1)),
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
            show_graph(self.entry, self.symbol)

        main()


def main():
    for symbol in symbol_list:
        # print(symbol)
        downloadCandles(symbol, "2015-12-01")
        hammer(symbol, f'./datasets/{symbol}_History.csv').backtest()

main()