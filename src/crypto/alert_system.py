#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.crypto.exchange import Exchange
from src.crypto.listener import Listener
from src.crypto.price_alerter import PriceAlert


class CryptoPriceAlertSystem:
    def __init__(self):
        self.listener = Listener()
        self.exchange = Exchange()

    def add_alert(self, currency_symbol, expected_price, action):
        self.listener.add_event(PriceAlert(self.exchange.at(currency_symbol), lambda price: price > expected_price),
                                action)

    def update_exchange(self, updates):
        self.exchange.update(updates)
        self.listener.check_alerts()
