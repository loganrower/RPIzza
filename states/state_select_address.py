"""
state to select delivery address from list

loop through addresses to select desired one, sleep warning after 2 minutes
"""

import sys

sys.path.append("../hardware")

from . import shared_data

from .state_transition import StateTransition
from hardware.lcd.lcd import LCD
from hardware.matrix_keypad.matrix_keypad import MatrixKeypad, TimeoutError


def state_select_address(lcd: LCD, keypad: MatrixKeypad) -> StateTransition:
    lcd.clear()

    # for now, our list of addresses to choose from
    addresses = [
        "1234 Main Street Corvallis, OR 97333",
        "5678 Main Street Corvallis, OR 97333"
    ]

    # the available characters to press to represent addresses
    chars = ['A', 'B']

    # prepend each address with char
    address_options = []
    for char, address in zip(chars, addresses):
        address_options.append(f"{char}-{address}")

    # loop through addresses, * to cycle or # to cancel
    current_address_index = 0
    lcd.write(message=address_options[current_address_index], row=0)
    lcd.write(message="*-Next #-Cancel", row=1)

    key = ''
    while key != '#' and key not in chars:
        try:
            key = keypad.get_key(timeout_seconds=120)
            if key == '*':
                current_address_index += 1
                if current_address_index == len(address_options):
                    current_address_index = 0
                lcd.write(message=address_options[current_address_index], row=0)
        except TimeoutError:
            return StateTransition.TO_STATE_SLEEP_WARNING

    if key == '#':
        return StateTransition.TO_STATE_CONFIRM_CANCEL_ORDER
    else:
        # now we know what address to deliver to
        shared_data.selected_address = addresses[chars.index(key)]
        return StateTransition.TO_STATE_CONFIRM_SELECT_ADDRESS

