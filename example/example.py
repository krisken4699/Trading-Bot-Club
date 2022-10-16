import sys
import os
# sys.path.insert(0, "../")
sys.path.append("../")
import ken_api
print(ken_api.apiV2.get_assets('SXNTF', "SWSSF", simple=True))
