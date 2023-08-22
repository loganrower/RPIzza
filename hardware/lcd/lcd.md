# LCD Class

The LCD class (in `lcd.py`) is the highest level way of interacting with the LCD display.

The I2C addresses, pins, and LCD dimensions are hard coded into the class and can be updated if necessary. That file's scroll() function also has editable parameters to modify the timing of the scrolling functionality. `start_pause`, `end_pause`, and `scroll_speed` tweak the timing of scrolling.

## Usage

```python
import time

from lcd.lcd import LCD


if __name__ == "__main__":
    # create the lcd object
    lcd = LCD()

    # write a message to the first row
    # messages longer than the LCD's width will scroll automatically
    lcd.write(message="", row=0)

    # write a message to the second row
    lcd.write(message="", row=1)

    time.sleep(5)

    # clear the LCD
    # make sure to ALWAYS clear the display before the program ends
    # failure to do so will result in nondeterministic behavior
    lcd.clear()
```
