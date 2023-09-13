"""
this state is a warning that the program is about to fall asleep and lose progress

display message and listen for any input, fall asleep after 15 seconds
"""

import sys

sys.path.append("../hardware")

from . import shared_data

from .state_transition import StateTransition
from hardware.matrix_keypad.matrix_keypad import TimeoutError


def state_sleep_warning(prev_state: StateTransition) -> StateTransition:
    lcd = shared_data.lcd
    keypad = shared_data.keypad

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
        # clear data selected earlier
        shared_data.selected_order = None
        shared_data.selected_address = None
        shared_data.selected_payment_method = None
        return StateTransition.TO_STATE_ASLEEP
