#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import unittest
from datetime import date
from ..currencies import CryptoCurrency

class TestCryptoCurrencies(unittest.TestCase):
    def setUp(self) -> None:
        self.btc = CryptoCurrency('BTC', 1)
        self.eth = CryptoCurrency('ETH', 2)

    def test_cryptocurrencies_has_his_own_symbol(self):
        self.assertEqual(self.btc.symbol, 'BTC')
        self.assertEqual(self.eth.symbol, 'ETH')

    def test_cryptocurrencies_has_a_price(self):
        self.assertIsNotNone(self.btc.price)
        self.assertIsNotNone(self.eth.price)

    def test_cryptocurrencies_has_his_own_price(self):
        self.assertNotEqual(self.btc.price, self.eth.price)

    def test_cryptocurrencies_has_update_date(self):
        self.assertEqual(self.btc.last_updated, date.today())
        self.assertEqual(self.eth.last_updated, date.today())

    def test_price_can_be_updated(self):
        self.btc.update_price(20)
        self.assertEqual(self.btc.price, 20)

    def test_date_is_updated_when_the_price_is_updated(self):
        self.btc.last_updated = date(2021, 1, 1)
        self.btc.update_price(100)
        self.assertEqual(self.btc.last_updated, date.today())


if __name__ == '__main__':
    unittest.main()
