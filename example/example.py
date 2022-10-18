
import sys
import os
import ken_api
api = ken_api.api()
print(api.get_assets('SXNTF', "SWSSF", "MANR", simple=True))
print(api.get_assets('PCSGF', simple=True))
print(api.get_assets('PCSGF'))
print(api.get_bars("TSLA", start="2022-10-05", end="2022-10-15"))
api.download_symbols()
print(api)
