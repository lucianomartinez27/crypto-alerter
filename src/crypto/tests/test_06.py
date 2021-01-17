#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import Mock

from src.crypto.alert_system import CryptoPriceAlertSystem


class TestAlertSystem(unittest.TestCase):
    def setUp(self) -> None:
        self.alert_system = CryptoPriceAlertSystem()

    def test_alerts_can_be_added_to_listener(self):
        action = lambda: print('Alerta cumplida')
        self.alert_system.add_alert('BTC', 10, action)
        self.alert_system.add_alert('ETH', 20, action)
        self.alert_system.add_alert('ETH', 100, action)
        self.assertEqual(len(self.alert_system.listener), 3)
        self.assertEqual(self.alert_system.listener.events[0].action, action)

    def test_when_the_exchange_is_updated_the_alerts_are_checked(self):
        updates = {'BTC': {'price': 2000}, 'ETH': {'price': 200}}
        self.alert_system.listener = Mock()
        self.alert_system.update_exchange(updates)
        self.assertEqual(self.alert_system.listener.check_alerts.call_count, 1)
