"""Basic utility functions for binance futures SDK."""

import logging

from binance.error import ClientError
from binance.lib.utils import config_logging


class BasicUtility:
    """Toolkit for simple tasks using binance futures SDK."""

    def __init__(self, client, debug=False):
        self.client = client
        if debug:
            config_logging(logging, logging.DEBUG)

    def get_account(self):
        """Get account information."""
        try:
            response = self.client.account(recvWindow=5000)
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def get_balance(self, symbol):
        """Get account balance."""
        try:
            response = self.client.balance(recvWindow=5000)
            for balance in response:
                if balance["asset"] == symbol:
                    return balance
            # logging.info(response)
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )

    def get_position(self, symbol):
        """Get open orders."""
        try:
            response = self.client.get_position_risk(recvWindow=5000)
            for position in response:
                if position["symbol"] == symbol:
                    return position
            return response
        except ClientError as error:
            logging.error(
                "Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )
