"""
state to confirm that the user wants to cancel the order

# to continue order, * to cancel order, 1 minute timeout before straight to sleep
"""

import sys

sys.path.append("../hardware")

from . import shared_data

from .state_transition import StateTransition
from hardware.matrix_keypad.matrix_keypad import TimeoutError


def state_confirm_cancel_order(prev_state: StateTransition) -> StateTransition:
    lcd = shared_data.lcd
    keypad = shared_data.keypad

    lcd.write(message="Want to cancel your order and quit RPIzza?", row=0)
    lcd.write(message="*-EXIT #-Return", row=1)

    key = ''
    while key != '#':
        try:
            key = keypad.get_key(timeout_seconds=60)
            if key == '*':
                return StateTransition.TO_STATE_ASLEEP
        except TimeoutError:
            return StateTransition.TO_STATE_ASLEEP

    return prev_state
