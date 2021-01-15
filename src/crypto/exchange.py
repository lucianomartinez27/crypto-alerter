#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from src.crypto.currencies import CryptoCurrency


class Exchange:
    def __init__(self):
        self.currencies = [CryptoCurrency('BTC', 1), CryptoCurrency('ETH', 1)]