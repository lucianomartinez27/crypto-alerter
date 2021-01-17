#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.crypto.event import Event


class Listener:
    def __init__(self):
        self.events = []

    def add_event(self, alert, action):
        self.events.append(Event(alert, action))

    def check_alerts(self):
        for event in self.events:
            event.execute_action()

    def __len__(self):
        return len(self.events)