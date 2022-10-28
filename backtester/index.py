from statistics import mean
from typing import ByteString
import ken_api
import datetime
import plotly.graph_objects as go
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
    with open(symbol + '_History.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(to_csv)


# downloadCandles("TSLA", "2021-02-01")
def show_graph():
    df = pd.read_csv('./TSLA_History.csv')
    fig = go.Figure(data=[go.Candlestick(x=df['t'],
                    open=df['o'],
                    high=df['h'],
                    low=df['l'],
                    close=df['c'])])

    fig.add_trace(go.Scatter(x=["2021-01-01", "2021-02-01", ],
                             y=[1100, 1050],
                             xperiod="M1",
                             xperiodalignment="middle", name="hv", line_shape='linear'))
    fig.update_traces(hoverinfo='text+name')
    # fig.update_traces(hoverinfo='text+name', mode='lines+markers')
    fig.show()

# show_graph()


class backtester:
    """
    Backtester class. 
    constructor str db_path: path to your csv file
    """

    def __init__(self, symbol: str, db_path: str):
        self.df = pd.read_csv(db_path)
        self.df.length = self.df.shape[0]
        self.symbol = symbol

    def openAttempt(self, index: int):  # check entry conditions
        print(self.df.iloc[index-6:index-1])
        print(sum(self.df.c[index-2:index-1])/1)
        print(sum(self.df.c[index-3:index-1])/2)
        print(sum(self.df.c[index-4:index-1])/3)
        print(sum(self.df.c[index-5:index-1])/4)
        print(sum(self.df.c[index-6:index-1])/5)
        print("best fit:", self.best_fit_line((x for x in self.df.c), [1,2,3,4,5]))

    def best_fit_line(self,xs: list, ys: list):
        print(self.df.c)
        return (mean(xs) * mean(ys) - mean(xs*ys)) / ((mean(xs) * mean(xs)) - mean(xs*xs))

    def backtest(self):
        def main():  # main thread
            for index, row in self.df.iterrows():
                if index == 14:
                    self.openAttempt(index)
            # print(self.df.length)

        main()


backtester("TSLA", './TSLA_History.csv').backtest()
