"""This is a miscellaneous file to figure stuff out"""

import os

from binance.um_futures import UMFutures
from dotenv import load_dotenv

from util.basic import BasicUtility
from util.candle import CandleUtility
from util.helpers import p

load_dotenv()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

client = UMFutures(key=BINANCE_API_KEY, secret=BINANCE_SECRET_KEY)

basicUtils = BasicUtility(client)
candleUtils = CandleUtility(client)

f = open("misc/candle.txt", "w")
f.write(p(candleUtils.get_candles("BTCUSDT", "1m", 5)))
f.close()
