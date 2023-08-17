from .PCF8574 import PCF8574_GPIO
from .Adafruit_LCD1602 import Adafruit_CharLCD

PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.

LCD_WIDTH = 16   # number of characters per horizontal row
LCD_HEIGHT = 2   # number of rows


class LCD:
    def __init__(self):
        try:
            self.mcp = PCF8574_GPIO(PCF8574_address)
            self.lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=self.mcp)
            self.lcd.begin(LCD_WIDTH, LCD_HEIGHT)
        except:
            try:
                self.mcp = PCF8574_GPIO(PCF8574A_address)
            except:
                raise Exception("LCD not found at expected I2C addresses")

    def clear(self):
        self.lcd.clear()

    # row is 0-indexed, default is 0
    def write(self, message, row=0):
        self.mcp.output(3, 1)

        if len(message) > LCD_WIDTH:
            # deal with scrolling messages here (threads???)
            pass

        # calculate cursor to place message in center
        difference = LCD_WIDTH - len(message)
        cursor_pos = difference // 2

        self.lcd.setCursor(cursor_pos, row)
        self.lcd.message(message)

    def __del__(self):
        self.lcd.clear()
