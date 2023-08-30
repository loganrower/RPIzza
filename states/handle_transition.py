"""
logic for handling transitions between states
"""
import sys

sys.path.append("../hardware")

from hardware.lcd.lcd import LCD
from hardware.matrix_keypad.matrix_keypad import MatrixKeypad

from .state_transition import StateTransition

from .state_asleep import state_asleep
from .state_sleep_warning import state_sleep_warning
from .state_start_order import state_start_order


# function to handle a transition from one state to the next
# given the previous and next states, execute the next state
def handle_transition(
    lcd: LCD, keypad: MatrixKeypad,
    prev_state: StateTransition,
    next_state: StateTransition
) -> StateTransition:
    if next_state == StateTransition.TO_STATE_ASLEEP:
        return state_asleep(lcd, keypad)
    elif next_state == StateTransition.TO_STATE_SLEEP_WARNING:
        return state_sleep_warning(lcd, keypad, prev_state)
    elif next_state == StateTransition.TO_STATE_START_ORDER:
        return state_start_order(lcd, keypad)
    return StateTransition.TO_STATE_UNKNOWN


