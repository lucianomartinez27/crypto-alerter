#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import unittest

from ..currencies import CryptoCurrency


class Test01(unittest.TestCase):
    def setUp(self) -> None:
        self.btc = CryptoCurrency('BTC')
        self.eth = CryptoCurrency('ETH')

    def test_CryptoCurrencies_has_his_own_symbol(self):
        self.assertEqual(self.btc.symbol, 'BTC')
        self.assertEqual(self.eth.symbol, 'ETH')

    def test_CryptoCurrencies_has_a_price(self):
        self.assertIsNotNone(self.btc.price)
        self.assertIsNotNone(self.eth.price)


if __name__ == '__main__':
    unittest.main()
