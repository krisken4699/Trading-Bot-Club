
import sys
import os
# sys.path.insert(0, "../")
# sys.path.append("../")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import ken_api
print(ken_api.get_assets('SXNTF', "SWSSF", "MANR", simple=True))
print(ken_api.get_assets('PCSGF', simple=True))
print(ken_api.get_assets('PCSGF'))
print(ken_api.get_bars("TSLA", start="2022-10-05", end="2022-10-15"))
ken_api.download_symbols()
