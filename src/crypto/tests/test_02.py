#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest
from src.crypto.price_alerter import PriceAlert
from src.crypto.currencies import CryptoCurrency


class Test02(unittest.TestCase):

    def test_condition_is_triggered_when_is_achieved(self):
        self.alert = PriceAlert(CryptoCurrency('BTC', 10), lambda price: price >= 10)
        self.assertTrue(self.alert.is_triggered())

