#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Event:
    def __init__(self, price_alert, action):
        self.price_alert = price_alert
        self.action = action

    def execute_action(self):
        self.action()