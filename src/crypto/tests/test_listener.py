#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from unittest import mock
from unittest.mock import Mock

from src.crypto.currencies import CryptoCurrency
from src.crypto.listener import Listener
from src.crypto.price_alerter import PriceAlert


class TestAddEventToListenerAndExecuteAction(unittest.TestCase):
    def setUp(self) -> None:
        self.listener = Listener()

    @mock.patch('src.crypto.price_alerter.PriceAlert')
    def test_listener_can_add_event_and_check_alerts(self, mocked_price_alert):
        self.listener.add_event(mocked_price_alert, lambda: 'pass')
        self.listener.add_event(PriceAlert(CryptoCurrency('ETH', 10), lambda price: price >= 10), lambda: 'pass')
        self.listener.check_alerts()
        self.assertEqual(mocked_price_alert.matches.call_count, 1)

    @mock.patch('src.crypto.price_alerter.PriceAlert')
    def test_when_alert_is_checked_action_is_executed_if_corresponds(self, mocked_price_alert):
        action = Mock()
        another_action = Mock()
        self.listener.add_event(mocked_price_alert, action)
        self.listener.add_event(PriceAlert(CryptoCurrency('ETH', 10), lambda price: price >= 20), another_action)
        self.listener.check_alerts()
        self.assertEqual(action.call_count, 1)
        self.assertEqual(another_action.call_count, 0)

    @mock.patch('src.crypto.price_alerter.PriceAlert')
    def test_when_a_price_alert_matches_is_removed(self, mocked_price_alert):
        action = Mock()
        another_action = Mock()
        action.matches = True
        another_action.matches = False
        self.listener.add_event(mocked_price_alert, action)
        self.listener.add_event(mocked_price_alert, another_action)
        self.assertEqual(len(self.listener), 2)
        self.listener.check_alerts()
        self.assertEqual(len(self.listener), 1)


