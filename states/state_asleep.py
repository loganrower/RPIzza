"""
this is the asleep state for the program

the LCD is off and waiting for any input
"""

import sys

sys.path.append("../hardware")

from . import shared_data

from .state_transition import StateTransition
from hardware.matrix_keypad.matrix_keypad import TimeoutError


def state_asleep() -> StateTransition:
    lcd = shared_data.lcd
    keypad = shared_data.keypad

    # turn the lcd off
    lcd.clear()
    lcd.off()

    # if any key is pressed, transition to state_start_order
    try:
        key = keypad.get_key()
        return StateTransition.TO_STATE_START_ORDER
    except TimeoutError:
        return state_asleep()
