#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import Mock

from src.crypto.currencies import CryptoCurrency
from src.crypto.event import Event
from src.crypto.price_alerter import PriceAlert


class TestEvent(unittest.TestCase):
    def test_an_event_execute_an_action_if_the_alert_condition_is_true(self):
        action = Mock()
        event = Event(PriceAlert(CryptoCurrency('ETH', 10), lambda price: price >= 10), action)
        event.execute_action()
        self.assertTrue(action.called)

    def test_an_event_does_not_execute_an_action_if_the_alert_condition_is_false(self):
        action = Mock()
        event = Event(PriceAlert(CryptoCurrency('ETH', 10), lambda price: price >= 20), action)
        event.execute_action()
        self.assertFalse(action.called)