"""
state to confirm that the selected payment method should be used

* to continue, # to go back to select_payment_method, 1 minute timeout
"""

import sys

sys.path.append("../hardware")

from . import shared_data

from .state_transition import StateTransition
from hardware.matrix_keypad.matrix_keypad import TimeoutError


def state_confirm_select_payment_method() -> StateTransition:
    lcd = shared_data.lcd
    keypad = shared_data.keypad

    selected_payment_method = shared_data.selected_payment_method

    lcd.write(message=f"Pay with {selected_payment_method}?", row=0)
    lcd.write(message="*-Confirm #-Back", row=1)

    key = ''
    while key != '#':
        try:
            key = keypad.get_key(timeout_seconds=60)

            if key == '*':
                # TODO: what state is next?
                return StateTransition.TO_STATE_UNKNOWN

        except TimeoutError:
            return StateTransition.TO_STATE_SELECT_PAYMENT_METHOD

    return StateTransition.TO_STATE_SELECT_PAYMENT_METHOD
