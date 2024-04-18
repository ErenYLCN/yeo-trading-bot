"""Chat bot module"""

import os

from binance.um_futures import UMFutures
from dotenv import load_dotenv

from toolkit import Activate

load_dotenv()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

client = UMFutures(key=BINANCE_API_KEY, secret=BINANCE_SECRET_KEY)

toolkit = Activate(client)

print(toolkit.get_balance("USDT"))
