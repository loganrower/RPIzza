"""
state to add items to the order

loop through items to add, sleep warning after 2 minutes
"""

import sys

sys.path.append("../hardware")

from . import shared_data

from .state_transition import StateTransition
from hardware.matrix_keypad.matrix_keypad import TimeoutError


def state_select_order() -> StateTransition:
    lcd = shared_data.lcd
    keypad = shared_data.keypad

    lcd.clear()

    # this is just for now, these are our orders
    orders = [
        "Med Pepperoni",
        "Lg Pepp. & Sausage",
        "Parm. Knots",
        "Blondies"
    ]

    # the available characters to press to represent orders
    chars = ['1', '2', '3', '4']

    # create strings for each order's description
    order_descriptions = []
    for order, char in zip(orders, chars):
        order_descriptions.append(f"{char}-{order}")

    # loop through valid item options, allowing for * to cycle or # to cancel order
    current_order_index = 0
    lcd.write(message=order_descriptions[current_order_index], row=0)
    lcd.write(message="*-Next #-Cancel", row=1)

    key = ''
    while key != '#' and key not in chars:
        try:
            key = keypad.get_key(timeout_seconds=120)
            if key == '*':
                # cycle to next item
                current_order_index += 1
                if current_order_index == len(order_descriptions):
                    current_order_index = 0
                lcd.write(message=order_descriptions[current_order_index], row=0)
        except TimeoutError:
            return StateTransition.TO_STATE_SLEEP_WARNING

    if key == '#':
        return StateTransition.TO_STATE_CONFIRM_CANCEL_ORDER
    else:
        # we now know which order we want to continue with
        shared_data.selected_order = orders[chars.index(key)]
        return StateTransition.TO_STATE_CONFIRM_SELECT_ORDER
