# tbc-ken-lib
#### This lib is made for to be used by members of the TBC club made in 2022.

## Install

```bash
$ pip install tbc-ken-lib
```
## Supported Features

tbc-ken-lib has and will only have functions that will be used for the project. Other functions that other Alpaca API clients may include that will not be used by the club will not be included in this lib.

- [get_assets: (*symbols: str, **simple: bool) -> (dict | int)](#get-assets)
- [get_bars: (symbol: Any, **kwargs: Any) -> (list | int)](#get-bars)
- [download_symbols: (path) -> (dict | int)](#download-assets)

## Examples

### Setup

Follow this link and generate an API key: https://app.alpaca.markets/paper/dashboard/overview 
Don't worry if you lose the key or forgot where you saved it. You can always regenerate them.
```python
#example.py
import ken_api
api = ken_api.api(
    'XXXXXXXXXXXXXXXXXXXX',  # alpaca api key (20 characters in length)
    "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # alpaca api secret (40 characters in length)
)  
# The alpaca api key and secret almost feels like user and password sometimes.
# If you don't have your own keys, you can use mine up there, though it is limitted to 200 api requests per minute.
# It's recommended to use your own keys. 
```
### Get Assets
```python
"""
This one returns you candle bars of the graph. 
You can specify the start, end, and even limit.

Get info of any stocks by putting in symbols. 
Put in simple=True to make the result come in a simple format. 
You can put in one symbol or many symbols. 
Without having the simple=True, it will return you much more data.
""" 
print(api.get_assets('SXNTF', "SWSSF", "MANR", simple=True))
print(api.get_assets('PCSGF', simple=True))
print(api.get_assets('PCSGF'))
print(api.get_bars("TSLA", start="2022-10-05", end="2022-10-15",limit=10))
```
### Download Assets
```python
"""
The function downloads a list of all stocks and assets Alpaca has, 
both active and inactive. It also takes no parameters
"""
api.download_symbols()
# This function doesn't return anything. The result will be downloaded as symbols_list in your current working directory without a file extension.
```

## Patches

### v0.3
<p>To use this lib, it is recommended to put your own api **key** and **secret** in your api object parameters. If not, you will automatically use mine, which has it's limits.</p>

### v0.2 and bellow
<p>To use the lib, touch alpaca_credentials.json and place in it your credentials.</p>

```json
//alpaca_credentials.json
{
	"APCA-API-KEY-ID": "PKNOZUSMT0A6E89QURCG",
	"APCA-API-SECRET-KEY": "SXFTc5gC4cAWmUpuGEiEurBGfN4bAqhA6Mxu28Ez"
}
```
