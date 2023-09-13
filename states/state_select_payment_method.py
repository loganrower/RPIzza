"""
state to select payment method from list

loop through payment methods to select desired one, sleep warning after 2 minutes
"""

import sys

sys.path.append("../hardware")

from . import shared_data

from .state_transition import StateTransition
from hardware.matrix_keypad.matrix_keypad import TimeoutError


def state_select_payment_method() -> StateTransition:
    lcd = shared_data.lcd
    keypad = shared_data.keypad

    lcd.clear()

    # for now, out list of payment methods to choose from
    payment_methods = [
        "Seb's Credit Card",
        "Seb's Debit Card"
    ]

    # the available characters to press to represent payment methods
    chars = ['1', '2']

    # prepend each payment method with char
    payment_method_options = []
    for char, payment_method in zip(chars, payment_methods):
        payment_method_options.append(f"{char}-{payment_method}")

    # loop through payment methods, * to cycle or # to cancel
    current_payment_method_index = 0
    lcd.write(message=payment_method_options[current_payment_method_index], row=0)
    lcd.write(message="*-Next #-Cancel", row=1)

    key = ''
    while key != '#' and key not in chars:
        try:
            key = keypad.get_key(timeout_seconds=120)
            if key == '*':
                current_payment_method_index += 1
                if current_payment_method_index == len(payment_method_options):
                    current_payment_method_index = 0
                lcd.write(message=payment_method_options[current_payment_method_index], row=0)
        except TimeoutError:
            return StateTransition.TO_STATE_SLEEP_WARNING

    if key == '#':
        return StateTransition.TO_STATE_CONFIRM_CANCEL_ORDER
    else:
        # now we know what payment method to use
        shared_data.selected_payment_method = payment_methods[chars.index(key)]
        return StateTransition.TO_STATE_CONFIRM_SELECT_PAYMENT_METHOD
