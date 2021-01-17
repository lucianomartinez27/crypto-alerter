#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from src.crypto.currencies import CryptoCurrency
from src.crypto.exchange import Exchange


class Test03(unittest.TestCase):
    def setUp(self):
        self.exchange = Exchange()

    def test_Exchange_contains_currencies(self):
        self.assertSequenceEqual(self.exchange.currencies, [CryptoCurrency('BTC', 1), CryptoCurrency('ETH', 1)])

    def test_currency_can_be_accessed_by_its_symbol(self):
        self.assertEqual(self.exchange.at('BTC'), CryptoCurrency('BTC', 1))

    def test_exchange_currencies_can_be_updated(self):
        updates = {'ETH': {'price': 125}, 'BTC': {'price': 225}}
        self.exchange.update(updates)
        self.assertEqual(self.exchange.at('ETH'), CryptoCurrency('ETH', 125))
        self.assertEqual(self.exchange.at('BTC'), CryptoCurrency('BTC', 225))
