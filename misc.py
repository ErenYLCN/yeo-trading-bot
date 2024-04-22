"""This is a miscellaneous file to figure stuff out"""

import os

from binance.um_futures import UMFutures
from dotenv import load_dotenv

from backtest.backtest import Backtest
from util.basic import BasicUtility
from util.candle import CandleUtility

load_dotenv()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

client = UMFutures(key=BINANCE_API_KEY, secret=BINANCE_SECRET_KEY)

basicUtils = BasicUtility(client)
candleUtils = CandleUtility(client)

backtestUtils = Backtest(client)
backtestUtils.basic_backtest("BTCUSDT")
