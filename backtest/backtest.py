import pandas as pd

from util.candle import CandleUtility


class Backtest:
    def __init__(self, client):
        self.client = client

    def create_backtest_file(self, symbol):
        """Create backtest csv file"""

        limit = 1500
        total = 4380
        interval = "4h"
        iterations = total // limit + (1 if total % limit > 0 else 0)

        df_combined = pd.DataFrame()
        candleUtils = CandleUtility(self.client)

        for i in range(iterations):
            end_time = (
                None
                if i == 0
                else int(
                    (df_combined.index[0] + pd.Timedelta(hours=4)).timestamp() * 1000
                )
            )
            l = limit if i + 1 < iterations else total % (limit * i)
            df = pd.DataFrame(
                candleUtils.get_candles(
                    symbol, interval, limit=l, end_time=end_time, format_time=True
                )
            )
            df_combined = pd.concat([df, df_combined])

        df_combined.to_csv(f"backtest/data/{symbol}.csv")

    def basic_backtest(self, symbol):
        """Basic backtest
        1. Read csv file
        2. Start from 20th index
        3. Look at previous 20 candles
        4. Get the highest high from the 20 candles
        5. If the close for the current candle is higher than the highest high, buy (if not already bought)
        6. Stop lose is 2% lower of bought price
        7. Take profit is 6% higher of bought price
        """

        balance = 1000
        starting_index = 20
        stop_loss = -0.12
        take_profit = 0.12
        has_position = False
        trades = []
        stop_loss_price = 0
        take_profit_price = 0
        buy_timestamps = []
        sell_timestamps = []

        df = pd.read_csv(f"backtest/data/{symbol}.csv", index_col=0)

        for i in range(starting_index, len(df)):
            current_candle = df.iloc[i]
            previous_candles = df.iloc[i - 20 : i]
            highest_high = previous_candles["high"].max()
            current_close = current_candle["close"]
            current_low = current_candle["low"]
            current_high = current_candle["high"]

            if not has_position:
                if current_close > highest_high:
                    print(f"Buying at {current_close}, highest high: {highest_high}")
                    buy_timestamps.append(current_candle.name)
                    has_position = True
                    bought_price = current_close
                    stop_loss_price = bought_price * (1 + stop_loss)
                    take_profit_price = bought_price * (1 + take_profit)
            else:
                if current_low <= stop_loss_price:
                    print(f"Stop loss hit at {stop_loss_price}")
                    sell_timestamps.append(current_candle.name)
                    has_position = False
                    trades.append(stop_loss)
                elif current_high >= take_profit_price:
                    print(f"Take profit hit at {take_profit_price}")
                    sell_timestamps.append(current_candle.name)
                    has_position = False
                    trades.append(take_profit)

        for trade in trades:
            balance *= 1 + trade

        print(f"Final balance: {balance}")
