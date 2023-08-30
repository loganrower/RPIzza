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
    # ...

