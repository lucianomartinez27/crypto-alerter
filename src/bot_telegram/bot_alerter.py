#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.crypto.alert_system import CryptoPriceAlertSystem


class BotAlerter:
    def __init__(self):
        self.alert_system = CryptoPriceAlertSystem()

    def add_alert(self, update, context):
        message = update.message
        currency, amount = message.text.split()

        def action():
            message.from_user.send_message(f'{currency} price is above {amount}')

        self.alert_system.add_alert(currency, float(amount), action)
