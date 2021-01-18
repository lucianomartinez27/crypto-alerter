#!/usr/bin/env python3
# -*- coding: utf -8 -*-
import unittest
from unittest.mock import Mock

from src.api_nomics.ticker import Ticker


class Test01(unittest.TestCase):

    def setUp(self) -> None:
        self.ticker = Ticker()
        self.ticker.ticker.get_currencies = Mock()

    def test_ticker_returns_btc_and_eth_updates(self):
        self.ticker.ticker.get_currencies.return_value = [{
            "currency": "BTC",
            "id": "BTC",
            "price": "100",
        },
            {
                "currency": "ETH",
                "id": "ETH",
                "price": "200",
            },
        ]
        self.assertEqual(self.ticker.get_prices('BTC', 'ETH'), {'BTC': {'price': 100}, 'ETH': {'price': 200}})

    def test_ticker_returns_eth_updates(self):
        self.ticker.ticker.get_currencies.return_value = [
            {
                "currency": "ETH",
                "id": "ETH",
                "price": "200",
            },
        ]
        self.assertEqual(self.ticker.get_prices('ETH'), {'ETH': {'price': 200}})

    def test_ticker_returns_no_updates(self):
        self.assertEqual(self.ticker.get_prices(), {})
