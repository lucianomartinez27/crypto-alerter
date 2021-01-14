#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import date


class CryptoCurrency:
    def __init__(self, symbol, price):
        # this is sometimes called ticker (like 'BTC', 'ETH', 'USD', etc.)
        self.symbol = symbol
        self.price = price
        self.last_updated = date.today()
