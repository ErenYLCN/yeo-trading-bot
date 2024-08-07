"""Chat bot module"""

import os

from binance.um_futures import UMFutures
from dotenv import load_dotenv

from util.basic import BasicUtility
from util.candle import CandleUtility
from util.helpers import pr

load_dotenv()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

client = UMFutures(key=BINANCE_API_KEY, secret=BINANCE_SECRET_KEY)

basicUtils = BasicUtility(client)
candleUtils = CandleUtility(client)

pr(basicUtils.get_position("BTCDOMUSDT"))
pr(candleUtils.get_candles("BTCUSDT", "1m", 5))
