"""Toolkit for simple tasks using binance futures SDK."""

import logging

from binance.error import ClientError
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)


class Activate:
    """Toolkit for simple tasks using binance futures SDK."""

    def __init__(self, client):
        self.client = client

    def get_balance(self, symbol):
        """Get account balance."""
        try:
            response = self.client.balance(recvWindow=6000)
            for elem in response:
                if elem["asset"] == symbol:
                    return float(elem["balance"])
            # logging.info(response)
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )
