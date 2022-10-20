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
- [downl# tbc-ken-lib
#### This lib is made for to be used by members of the TBC club made in 2022.

## Install
Make sure python3 and pip is installed globally in your system. Write or paste the script into your bash terminal.
```bash
$ pip install tbc-ken-lib
```
## Latest Supported Features

tbc-ken-lib has and will only have functions that will be used for the project. Other functions that other Alpaca API clients may include that will not be used by the club will not be included in this lib.

 - [x] Get a list of symbols 
 - [x] Get any asset's market history 
 - [x] Get general information of any assets
 - [x] Access owned assets and positions
 - [x] View account informations
 - [ ] Sell assets
 - [ ] Buy assets

Unticked features will be coming in the next versions.
 

## Examples

### Index
- [Basic Setup](#setup)
- [Get Assets](#get-assets)
- [Get Bars](#get-bars)
- [Download Symbols](#download-assets)
- [Get Account Information](#Get-account-information)
- [Get Positions](#get-positions)

### Setup
[Install](#install) the module from https://pypi.org
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

> get_assets: (*symbols: str, **simple: bool) -> (dict | int)

Get basic info of any stocks by putting in symbols. 
Put in `simple=True` to make the result come in a simple format.
```python
""" 
You can put in one symbol or many symbols. 
Without having the simple=True, it will return you much more data.
""" 
print(api.get_assets('SXNTF', "SWSSF", "MANR", simple=True))
print(api.get_assets('PCSGF', simple=True))
print(api.get_assets('PCSGF'))
```
### Get Bars

> get_bars: (symbol: Any, **kwargs: Any) -> (list | int)

This function simply returns a *List* of *dicts* representing each candle in a 1 day time frame.
```python
# Get candles of a symbol. 
#You can specify the start, end, and limit. (optional)
print(api.get_bars("TSLA", start="2022-10-05", end="2022-10-15"))
```
**Expected return format**<br>
*`t`*: string/timestamp Timestamp in RFC-3339 format with nanosecond precision<br>
*`o`*: number Open price<br>
*`h`*: number High price<br>
*`c`*: number Close price<br>
*`v`*: int Volume<br>
*`n`*: int Number of trades<br>
*`vw`*: number Volume-weighted average price<br>

### Download Assets

> download_symbols: (path) -> (dict | int)


The function downloads a list of all stocks and assets Alpaca has, 
both active and inactive. It also takes no parameters
```python
api.download_symbols()
# This function doesn't return anything. The result will be downloaded as symbols_list in your current working directory without a file extension.
```
**Expected file content**<br>
*`asset_id`*: Asset ID<br>
*`symbol`*: Symbol name of the asset<br>
*`exchange`*: Exchange name of the asset (ErisX for crypto)<br>
*`asset_class`*: Asset class name<br>
*`avg_entry_price`*: Average entry price of the position<br>
*`qty`*: The number of shares<br>
*`qty_available`*: Total number of shares available minus open orders<br>
*`side`*: “long”
*`market_value`*: Total dollar amount of the position<br>
*`cost_basis`*: Total cost basis in dollar<br>
*`unrealized_pl`*: Unrealized profit/loss in dollars<br>
*`unrealized_plpc`*: Unrealized profit/loss percent (by a factor of 1)<br>
*`unrealized_intraday_pl`*: Unrealized profit/loss in dollars for the day<br>
*`unrealized_intraday_plpc`*: Unrealized profit/loss percent (by a factor of 1)<br>
*`current_price`*: Current asset price per share<br>
*`lastday_price`*: 	Last day’s asset price per share based on the closing value of the last trading day<br>
*`change_today`*: Percent change from last day price (by a factor of 1)<br>

### Get Positions

> get_positions: (symbol: str = "") -> (list | int)


Returns owned assets' info or a specific asset's info.<br>
params str symbol: specific symbol of an asset you want to get the position.
```python
api.get_positions("TSLA")
# This will return your TSLA assets. 
```
**Expected file content**<br>
*`asset_id`*: asset's id<br>
*`symbol`*: asset's symbol<br>
*`exchange`*: just expect `"us-equity"`<br>
*`id`*: asset's id<br>
*`status`*: either `"active"` or `"inactive"`<br>

### Get Account Information

> get_account: () -> (dict | int)

Return account information
```python
print(api.get_account())
# This will return your TSLA assets. 
```
**Expected return format**<br>
*`id`*: account id<br>
*`account_number`*: account number<br>
*`status`*: your account status:<br>
  - `"ONBOARDING"` The account is onboarding.
  - `"SUBMISSION_FAILED"` The account application submission failed for some reason.
  - `"SUBMITTED"` The account application has been submitted for review.
  - `"ACCOUNT_UPDATED"` The account information is being updated.
  - `"APPROVAL_PENDING"` The final account approval is pending.
  - `"ACTIVE"` The account is active for trading.
  - `"REJECTED"` The account application has been rejected.
  
*`account_blocked`*: either `"True"` or `"False"`<br>
*`equity`*: *int*<br>
*`trading_blocked`*: either `"True"` or `"False"`<br>
*`daytrade_count`*: *int*<br>
*`ballance_asof`*: a date in *YYYY-MM-DD* format<br>
*`position_market_value`*: *int*<br>
*`created_at`*: timestamp in the format of yyyy-MM-dd'T'HH:mm:ss.SSS'Z'<br>
*`currency`*: a currency, probably USD<br>
*`buying_power`*: *int*<br>
and much more useful information

## Patches

### v0.3.2
<p>Added 2 functions. Made python 3.10 or above a requirement.</p>

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
oad_symbols: (path:str) -> (dict | int)](#download-assets)

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

### v0.3.2
<p>Added 2 functions. Made Python 3.10 or above a requirement.</p>

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
