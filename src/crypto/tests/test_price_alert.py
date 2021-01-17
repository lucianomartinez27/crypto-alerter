#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest
from src.crypto.price_alerter import PriceAlert
from src.crypto.currencies import CryptoCurrency


class TestTriggeringPriceAlert(unittest.TestCase):
    def setUp(self):
        self.btc = CryptoCurrency('BTC', 10)

    def test_alert_is_triggered_when_condition_is_achieved(self):
        self.alert = PriceAlert(self.btc, lambda price: price >= 10)
        self.assertTrue(self.alert.matches())

    def test_alert_is_not_triggered_if_condition_is_not_achieved(self):
        self.alert = PriceAlert(self.btc, lambda price: price < 10)
        self.assertFalse(self.alert.matches())


