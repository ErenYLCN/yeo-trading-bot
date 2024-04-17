"""Chat bot module"""

import os

from dotenv import load_dotenv

load_dotenv()

BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_SECRET_KEY = os.getenv("BINANCE_SECRET_KEY")

print(BINANCE_API_KEY)
print(BINANCE_SECRET_KEY)

print("Hello, world!")
