"""
state to confirm that the selected address should be used

* to continue, # to go back to select_address, 1 minute timeout
"""

import sys

sys.path.append("../hardware")

from . import shared_data

from .state_transition import StateTransition
from hardware.matrix_keypad.matrix_keypad import TimeoutError


def state_confirm_select_address() -> StateTransition:
    lcd = shared_data.lcd
    keypad = shared_data.keypad
    selected_address = shared_data.selected_address

    lcd.write(message=f"Deliver to {selected_address}?", row=0)
    lcd.write(message="*-Confirm #-Back", row=1)

    key = ''
    while key != '#':
        try:
            key = keypad.get_key(timeout_seconds=60)

            if key == '*':
                return StateTransition.TO_STATE_SELECT_PAYMENT_METHOD

        except TimeoutError:
            return StateTransition.TO_STATE_SELECT_ADDRESS

    return StateTransition.TO_STATE_SELECT_ADDRESS
