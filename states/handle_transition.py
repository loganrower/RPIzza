"""
logic for handling transitions between states
"""
from .state_transition import StateTransition

from .state_asleep import state_asleep
from .state_sleep_warning import state_sleep_warning
from .state_start_order import state_start_order
from .state_select_order import state_select_order
from .state_confirm_cancel_order import state_confirm_cancel_order
from .state_confirm_select_order import state_confirm_select_order
from .state_select_address import state_select_address
from .state_confirm_select_address import state_confirm_select_address
from .state_select_payment_method import state_select_payment_method
from .state_confirm_select_payment_method import state_confirm_select_payment_method


# function to handle a transition from one state to the next
# given the previous and next states, execute the next state
def handle_transition(
    prev_state: StateTransition,
    next_state: StateTransition
) -> StateTransition:
    print(prev_state, end='')
    print(" -> ", end='')
    print(next_state)

    if next_state == StateTransition.TO_STATE_ASLEEP:
        return state_asleep()
    elif next_state == StateTransition.TO_STATE_SLEEP_WARNING:
        return state_sleep_warning(prev_state)
    elif next_state == StateTransition.TO_STATE_START_ORDER:
        return state_start_order()
    elif next_state == StateTransition.TO_STATE_SELECT_ORDER:
        return state_select_order()
    elif next_state == StateTransition.TO_STATE_CONFIRM_CANCEL_ORDER:
        return state_confirm_cancel_order(prev_state)
    elif next_state == StateTransition.TO_STATE_CONFIRM_SELECT_ORDER:
        return state_confirm_select_order()
    elif next_state == StateTransition.TO_STATE_SELECT_ADDRESS:
        return state_select_address()
    elif next_state == StateTransition.TO_STATE_CONFIRM_SELECT_ADDRESS:
        return state_confirm_select_address()
    elif next_state == StateTransition.TO_STATE_SELECT_PAYMENT_METHOD:
        return state_select_payment_method()
    elif next_state == StateTransition.TO_STATE_CONFIRM_SELECT_PAYMENT_METHOD:
        return state_confirm_select_payment_method()
    return StateTransition.TO_STATE_UNKNOWN
