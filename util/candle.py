"""Candle utility module"""

import logging

from binance.error import ClientError
from binance.lib.utils import config_logging


class CandleUtility:
    """Toolkit for simple tasks using binance futures SDK."""

    def __init__(self, client, debug=False):
        self.client = client
        if debug:
            config_logging(logging, logging.DEBUG)

    def get_candles(self, symbol, interval, limit):
        """Get candles."""
        try:
            response = self.client.mark_price_klines(
                symbol, interval, **{"limit": limit}
            )
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )
