#!/usr/bin/env python3
# -*-coding: utf-8 -*-

class PriceAlert:
    def __init__(self, currency, condition):
        self.currency = currency
        self.condition = condition

    def is_triggered(self):
        return self.condition(self.currency.price)

