"""
state to act as the "home page" after RPIzza is woken up

display welcome message, hit * to start, sleep warning after 15 secs
"""

import sys

sys.path.append("../hardware")

from . import shared_data

from .state_transition import StateTransition
from hardware.matrix_keypad.matrix_keypad import TimeoutError


def state_start_order() -> StateTransition:
    lcd = shared_data.lcd
    keypad = shared_data.keypad

    lcd.on()
    lcd.clear()

    # print welcome message
    lcd.write(message="Welcome to RPIzza", row=0)

    # print button prompt
    lcd.write(message="* - Start Order", row=1)

    # expect button press
    key = ''
    while key != '*':
        try:
            key = keypad.get_key(timeout_seconds=15)
        except TimeoutError:
            return StateTransition.TO_STATE_SLEEP_WARNING

    # continue to start the order
    return StateTransition.TO_STATE_SELECT_ORDER
