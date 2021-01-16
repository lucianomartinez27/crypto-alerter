#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from datetime import date


class CryptoCurrency:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.last_update = date.today()

    def update_price(self, price):
        self.price = price
        self.last_update = date.today()

    def __eq__(self, other):
        return self.symbol == other.symbol and self.price == other.price and self.last_update == other.last_update
