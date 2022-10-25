from ken_api import *
import datetime
import plotly.graph_objects as go
import csv
import pandas as pd
client = api()


def downloadCandles(symbol: str, start: str, end: str = False):
    """
        downloads a all candles to ./<Symbol>_history in the same directory.\n
        \t:param str symbol: Symbol
        \t:param str start: Start date of the history you want to retrieve.
    """
    print(str(datetime.date.today()))
    to_csv = client.get_bars(symbol, end=str(
        datetime.date.today() if not end else end), start=start)
    keys = to_csv[0].keys()
    with open(symbol + '_History.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(to_csv)


downloadCandles("TSLA", "2021-02-01")

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
