"""
an enum to represent a signal to transition from one state to another
each state is responsible for returning a variable of this type
"""

from enum import Enum


class StateTransition(Enum):
    TO_STATE_UNKNOWN = 1
    TO_STATE_ASLEEP = 2
    TO_STATE_SLEEP_WARNING = 3
    TO_STATE_START_ORDER = 4
    TO_STATE_SELECT_ORDER = 5
    TO_STATE_CONFIRM_CANCEL_ORDER = 6
    TO_STATE_CONFIRM_SELECT_ORDER = 7
    TO_STATE_SELECT_ADDRESS = 8
    TO_STATE_CONFIRM_SELECT_ADDRESS = 9
    # ...

