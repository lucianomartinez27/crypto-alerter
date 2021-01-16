#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.crypto.currencies import CryptoCurrency


class Exchange:
    def __init__(self):
        self.currencies = [CryptoCurrency('BTC', 1), CryptoCurrency('ETH', 1)]
        # A ticker symbol or stock symbol is an abbreviation used to uniquely identify
        # publicly traded shares of a particular stock on a particular stock market. (Wikipedia)"""
        self.ticker = {currency.symbol: currency for currency in self.currencies}

    def at(self, symbol):
        return self.ticker[symbol]
