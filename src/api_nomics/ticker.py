#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from config import coin_mkt_token
from coinmarketcapapi import CoinMarketCapAPI


class Ticker:
    def __init__(self):
        self.ticker = CoinMarketCapAPI(coin_mkt_token)

    def get_prices(self, *currencies):
        currencies = ','.join(currencies)
        updates = {}
        if currencies:
            for currency in self.ticker.cryptocurrency_listings_latest().data[:2]:
                updates[currency['symbol']] = {'price': float(currency['quote']['USD']['price'])}
            return updates
        return updates
