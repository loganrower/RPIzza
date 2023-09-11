"""
state to confirm that the selected payment method should be used

* to continue, # to go back to select_payment_method, 1 minute timeout
"""

import sys

sys.path.append("../hardware")

from .state_transition import StateTransition
from hardware.lcd.lcd import LCD
from hardware.matrix_keypad.matrix_keypad import MatrixKeypad, TimeoutError


def state_confirm_select_payment_method(lcd: LCD, keypad: MatrixKeypad) -> StateTransition:
    # TODO: figure out how this state knows what user chose in state_select_payment_method

    lcd.write(message="Use payment method ______?", row=0)
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
