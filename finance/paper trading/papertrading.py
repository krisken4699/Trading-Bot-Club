from datetime import date, datetime, timedelta
from multiprocessing.sharedctypes import Value
from random import choice
from statistics import mean
import ken_api
import numpy as np
import json
import plotly.offline as of
import plotly.graph_objects as go
# import plotly.express as px
import csv
import os
import pandas as pd
api = ken_api.api()

symbol_list = ["SQ", "SHOP", "NET", "COIN", "GTLB", "HCP", "DLO", "ASAN", "W", "LAC", "FTCH", "MSTR", "CVNA", "AUR",
               "STEM", "PACB", "RIOT", "UUUU", "AMPX", "AMRS", "BNGO", "VLD", "DOMO", "AEHR", "NOTV", "SKLZ", "BBBY", "CORZ"]

