import time

import RPi.GPIO as GPIO

from .Keypad import Keypad       #import module Keypad


ROWS = 4        # number of rows of the Keypad
COLS = 4        #number of columns of the Keypad
keys =  [   '1','2','3','A',    #key code
            '4','5','6','B',
            '7','8','9','C',
            '*','0','#','D'     ]
rowsPins = [12,16,18,22]        #connect to the row pinouts of the keypad
colsPins = [19,15,13,11]        #connect to the column pinouts of the keypad

class MatrixKeypad:
    def __init__(self):
        self.keypad = Keypad(keys, rowsPins, colsPins, ROWS, COLS)
        self.keypad.setDebounceTime(50)

    # Blocking function that returns when a button is pressed
    # default timeout is 30 seconds
    def get_key(self, timeout_seconds=30):
        t_end = time.time() + timeout_seconds
        while time.time() < t_end:
            key = self.keypad.getKey()
            if key != self.keypad.NULL:
                return key
        raise TimeoutError

# an error to raise when timing out from getting a key
class TimeoutError(Exception):
    pass

