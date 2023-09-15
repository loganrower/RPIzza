# MatrixKeypad Class

The MatrixKeypad class (in `matrix_keypad.py`) is the highest level way of interacting with the keypad.

The keypad pins, dimensions, and legends are hard coded into the file and can be updated if necessary.

## Usage

```python
import RPi.GPIO as GPIO
from matrix_keypad.matrix_keypad import MatrixKeypad, TimeoutError


if __name__ == "__main__":
    # create keypad object
    keypad = MatrixKeypad()

    # read a keypress from the keypad
    # this is a blocking function that will raise a TimeoutError if nothing is pressed
    # the default value for timeout_seconds is 30
    try:
        key = keypad.get_key(timeout_seconds=10)
        print(f"you pressed {key}")
    except TimeoutError:
        print("you took too long to press a key!")
    
    # clean up after done using raspberry pi's gpio pins
    GPIO.cleanup()
```

