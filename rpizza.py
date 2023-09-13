"""
this file is the main execution start point

it will contain the flow from one state to the next
"""

import signal
import sys

import RPi.GPIO as GPIO

from hardware.lcd.lcd import LCD
from hardware.matrix_keypad.matrix_keypad import MatrixKeypad

from states.state_transition import StateTransition
from states.handle_transition import handle_transition
from states.state_asleep import state_asleep


def sigterm_handler(sig_num, frame):
    lcd.clear()
    lcd.off()
    GPIO.cleanup()
    sys.exit()

lcd = LCD()
keypad = MatrixKeypad()

if __name__ == "__main__":
    # set handler for sigterm to stop using lcd and keypad gracefully
    signal.signal(signal.SIGTERM, sigterm_handler)

    # start the program as sleeping
    next_state = state_asleep(lcd, keypad)
    prev_state = StateTransition.TO_STATE_ASLEEP

    # continue to execute the program by looping between states indefinitely
    while True:
        result = handle_transition(lcd, keypad, prev_state, next_state)

        prev_state = next_state
        next_state = result
