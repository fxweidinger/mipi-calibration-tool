#  Copyright (c) Felix Weidinger (fxweidinger) 2023

import pynput.keyboard
from pynput import keyboard


class EventHandler:

    def __init__(self, listener: pynput.keyboard.Listener):
        self.listener = listener
        listener.start()

    def stop(self):
        self.listener.stop()
