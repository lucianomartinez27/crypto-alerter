#!/usr/bin/env python3
# -*-coding: utf-8 -*-

class PriceAlert:
    def __init__(self, currency, condition):
        self.currency = currency
        self.condition = condition

    def matches(self):
        return self.condition(self.currency.price)

    def __str__(self):
        return 'PriceAlert({}, {})'.format(self.currency.symbol, self.currency.price)

