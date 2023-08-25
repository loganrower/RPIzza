from time import sleep, strftime
from datetime import datetime

import RPi.GPIO as GPIO

from lcd.lcd import LCD
from matrix_keypad.matrix_keypad import MatrixKeypad, TimeoutError


def loop():
    keypad = MatrixKeypad()
    print("Press key to start")
    while(True):
        try:
            key = keypad.get_key(timeout_seconds=10)
            print ("You Pressed Key : %c "%(key))
            lcd.write("this is a longer message that should scroll", row=0)
            lcd.write(f"{key} is the button that you pressed", row=1)
        except TimeoutError:
            print("you took too long to press a key!")
    # Full order number
    ## order_number = ""
    ## while star is not pressed then continue to add to the order number
    ##
    ## lcd.message

def destroy():
    lcd.clear()
    GPIO.cleanup()

lcd = LCD()

if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

