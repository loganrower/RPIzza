"""
this is the asleep state for the program

the LCD is off and waiting for any input
"""

import sys

sys.path.append("../hardware")

from .state_transition import StateTransition
from hardware.lcd.lcd import LCD
from hardware.matrix_keypad.matrix_keypad import MatrixKeypad


def state_asleep(lcd: LCD, keypad: MatrixKeypad) -> StateTransition:
    lcd.clear()

    # turn the lcd off
    # still need to figure this out

    # if any key is pressed, transition to state_start_order
    try:
        key = keypad.get_key()
        return StateTransition.TO_STATE_START_ORDER
    except TimeoutError:
        return state_asleep(lcd, keypad)


