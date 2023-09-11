"""
state to confirm that the selected address should be used

* to continue, # to go back to select_address, 1 minute timeout
"""

import sys

sys.path.append("../hardware")

from .state_transition import StateTransition
from hardware.lcd.lcd import LCD
from hardware.matrix_keypad.matrix_keypad import MatrixKeypad, TimeoutError


def state_confirm_select_address(lcd: LCD, keypad: MatrixKeypad) -> StateTransition:
    # TODO: figure out how this state knows what user chose in state_select_address

    lcd.write(message="Use address _________?", row=0)
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

