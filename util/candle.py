"""Candle utility module"""

import logging

import pandas as pd
from binance.error import ClientError
from binance.lib.utils import config_logging


class CandleUtility:
    """Toolkit for simple tasks using binance futures SDK."""

    def __init__(self, client, debug=False):
        self.client = client
        if debug:
            config_logging(logging, logging.DEBUG)

    def get_candles(
        self, symbol, interval, limit, start_time=None, end_time=None, format_time=False
    ):
        """Get candles."""
        try:
            response = pd.DataFrame(
                self.client.klines(
                    symbol,
                    interval,
                    **{"limit": limit},
                    startTime=start_time,
                    endTime=end_time
                )
            )
            response = response.iloc[:, :6]
            response.columns = ["timestamp", "open", "high", "low", "close", "volume"]
            if format_time:
                response["timestamp"] = pd.to_datetime(response["timestamp"], unit="ms")
            response.set_index("timestamp", inplace=True)
            response = response.astype(float)

            if format_time is False:
                response.index = response.index.astype(int)
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )
