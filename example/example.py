import ken_api
api = ken_api.api(
    'PKNOZUSMT0A6E89QURCG',  # alpaca api key
    "SXFTc5gC4cAWmUpuGEiEurBGfN4bAqhA6Mxu28Ez"  # alpaca api secret
)  # the alpaca api key and secret almost feels like user and password sometimes

# If you don't have your own keys, you can use mine up there, though it is limitted to 200 api requests per minute.
# It's best to get your own keys tho

# get info of any stocks by putting in symbols. Put in simple=True to make the result come in a simple format.
print(api.get_assets('SXNTF', "SWSSF", "MANR", simple=True))
# you can put in one symbol or many symbols. Up 2 u
print("")
print(api.get_assets('PCSGF', simple=True))
# without having the simple=True, it will return you much more data.
print("")
print(api.get_assets('PCSGF'))
# This one returns you candle_bars of the graph. You can specify the start, end, and even limit.
print("")
print(api.get_bars("TSLA", start="2022-10-05", end="2022-10-15"))
# this one downloads a list of all stocks, both active and inactive.
print("")
api.download_symbols()

print(api)
