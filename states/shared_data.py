"""
This file contains all the global data that all states in RPIzza's execution have access to

We're okay with this shared "state" solution because each RPIzza state is discrete and only one can be active at a time
"""
import sys

sys.path.append("../hardware")

from hardware.lcd.lcd import LCD
from hardware.matrix_keypad.matrix_keypad import MatrixKeypad

# the LCD object states use to write to the screen
lcd: LCD = None

# the MatrixKeypad object states use to read input from the keypad
keypad: MatrixKeypad = None

# the order that was selected by the user
selected_order = None

# the address that was selected by the user
selected_address = None

# the payment method that was selected by the user
selected_payment_method = None
