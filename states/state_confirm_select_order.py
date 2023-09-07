"""
state to confirm that the selected order should be used

* to continue, # to go back to select_order, 1 minute timeout
"""

import sys

sys.path.append("../hardware")

from .state_transition import StateTransition
from hardware.lcd.lcd import LCD
from hardware.matrix_keypad.matrix_keypad import MatrixKeypad, TimeoutError


def state_confirm_select_order(lcd: LCD, keypad: MatrixKeypad) -> StateTransition:
    # TODO: figure out how this state knows what user chose in state_select_order

    lcd.write(message="Use order __________?", row=0)
    lcd.write(message="*-Confirm #-Back", row=1)

    key = ''
    while key != '#':
        try:
            key = keypad.get_key(timeout_seconds=60)

            if key == '*':
                # TODO: return StateTransition.TO_STATE_SELECT_ADDRESS
                return StateTransition.TO_STATE_UNKNOWN

        except TimeoutError:
            return StateTransition.TO_STATE_SELECT_ORDER

    return StateTransition.TO_STATE_SELECT_ORDER

