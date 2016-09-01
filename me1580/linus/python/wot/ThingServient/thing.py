# -*- coding: utf-8 -*-

class Thing:
    """Thing class for physical WoT-objects. Holds the state of the "thing"
    with its bound sensor(s) and actor(s)."""
    def __init__(self):
        self.state = []
        self.sensors = []
        self.actors = []
        return 'Hello world!'