#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.crypto.currencies import CryptoCurrency


class Exchange:
    def __init__(self):
        self.currencies = [CryptoCurrency('BTC', 1), CryptoCurrency('ETH', 1)]
        self.ticker = {currency.symbol: currency for currency in self.currencies}

    def at(self, symbol):
        return self.ticker[symbol]

    def update(self, updates):
        for symbol, content in zip(updates.keys(), updates.values()):
            self.at(symbol).update_price(content['price'])
