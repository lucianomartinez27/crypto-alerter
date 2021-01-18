#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nomics
from config import token


class Ticker:
    def __init__(self):
        self.ticker = nomics.Nomics(token).Currencies

    def get_prices(self, *currencies):
        currencies = ','.join(currencies)
        updates = {}
        if currencies:
            for currency in self.ticker.get_currencies(currencies):
                updates[currency['id']] = {'price': float(currency['price'])}
            return updates
        return {}
