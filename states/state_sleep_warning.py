"""
this state is a warning that the program is about to fall asleep and lose progress

display message and listen for any input, fall asleep after 15 seconds
"""

import sys

sys.path.append("../hardware")

from .state_transition import StateTransition
from hardware.lcd.lcd import LCD
from hardware.matrix_keypad.matrix_keypad import MatrixKeypad, TimeoutError


def state_sleep_warning(lcd: LCD, keypad: MatrixKeypad, prev_state: StateTransition) -> StateTransition:
    # display warning message
    lcd.clear()
    lcd.write(message="WARNING: FALLING ASLEEP", row=0)
    lcd.write(message="Any - Resume", row=1)

    # expect button press with 15 second timeout
    try:
        key = keypad.get_key(timeout_seconds=15)

        # return to previous state if woken up in time
        return prev_state
    except TimeoutError:

        # fall asleep if no button press
        return StateTransition.TO_STATE_ASLEEP
