"""
state to act as the "home page" after RPIzza is woken up

display welcome message, hit * to start, sleep warning after 15 secs
"""

import sys

sys.path.append("../hardware")

from .state_transition import StateTransition
from hardware.lcd.lcd import LCD
from hardware.matrix_keypad.matrix_keypad import MatrixKeypad, TimeoutError


def state_start_order(lcd: LCD, keypad: MatrixKeypad) -> StateTransition:
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

