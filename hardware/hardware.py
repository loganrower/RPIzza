from time import sleep, strftime
from datetime import datetime

from lcd.lcd import LCD


# packages for Keypad
import RPi.GPIO as GPIO
from keypad_poc.Keypad import Keypad      #import module Keypad

# Keypad Constants
ROWS = 4        # number of rows of the Keypad
COLS = 4        #number of columns of the Keypad
keys =  [   '1','2','3','A',    #key code
            '4','5','6','B',
            '7','8','9','C',
            '*','0','#','D'     ]
## Keypad pins
rowsPins = [12,16,18,22]        #connect to the row pinouts of the keypad
colsPins = [19,15,13,11]        #connect to the column pinouts of the keypad


def loop():
    keypad = Keypad(keys,rowsPins,colsPins,ROWS,COLS)    #creat Keypad object
    keypad.setDebounceTime(50)      #set the debounce time
    print("Press key to start")
    while(True):
        key = keypad.getKey()       #obtain the state of keys
        if(key != keypad.NULL):     #if there is key pressed, print its key code.
            print ("You Pressed Key : %c "%(key))
            lcd.write("this is a longer message that should scroll", row=0)
            lcd.write(f"{key} is the button that you pressed", row=1)
            sleep(1)
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

