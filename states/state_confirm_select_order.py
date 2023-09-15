"""
state to confirm that the selected order should be used

* to continue, # to go back to select_order, 1 minute timeout
"""

import sys

sys.path.append("../hardware")

from . import shared_data

from .state_transition import StateTransition
from hardware.matrix_keypad.matrix_keypad import TimeoutError


def state_confirm_select_order() -> StateTransition:
    lcd = shared_data.lcd
    keypad = shared_data.keypad
    selected_order = shared_data.selected_order

    lcd.write(message=f"Order {selected_order}?", row=0)
    lcd.write(message="*-Confirm #-Back", row=1)

    key = ''
    while key != '#':
        try:
            key = keypad.get_key(timeout_seconds=60)

            if key == '*':
                return StateTransition.TO_STATE_SELECT_ADDRESS

        except TimeoutError:
            return StateTransition.TO_STATE_SELECT_ORDER

    return StateTransition.TO_STATE_SELECT_ORDER
