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

print(BINANCE_API_KEY)
print(BINANCE_SECRET_KEY)

client = UMFutures(key=BINANCE_API_KEY, secret=BINANCE_SECRET_KEY)

# basicUtils = BasicUtility(client)
# candleUtils = CandleUtility(client)

# print(basicUtils.get_balance("USDT"))


# pr(basicUtils.get_position("BTCDOMUSDT"))
# pr(candleUtils.get_candles("BTCUSDT", "1m", 5))


try:
    # Set margin type to ISOLATED for DOGEUSDT
    client.change_margin_type(symbol='DOGEUSDT', marginType='ISOLATED')
except Exception as e:
    print(f"Error changing margin type: {e}")


# Set leverage to 2x for DOGEUSDT
client.change_leverage(symbol='DOGEUSDT', leverage=2)

# Get current price of DOGEUSDT
price = float(client.ticker_price(symbol='DOGEUSDT')['price'])

# Calculate quantity to buy with 5 USDT
quantity = round(8 / price, 0)  # Adjust quantity to required precision

# Place a market order to buy DOGEUSDT
order = client.new_order(
    symbol='DOGEUSDT',
    side='BUY',
    type='MARKET',
    quantity=quantity
)

print(order)
