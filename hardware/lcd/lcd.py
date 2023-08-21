from threading import Thread, Lock
import time

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
            self.lcd_lock = Lock()
            self.scroll_threads = []
            self.scroll_threads_terminate = []
            for thread in range(0, LCD_HEIGHT):
                self.scroll_threads.append(None)
                self.scroll_threads_terminate.append(False)
        except:
            try:
                self.mcp = PCF8574_GPIO(PCF8574A_address)
            except:
                raise Exception("LCD not found at expected I2C addresses")


    def clear(self):
        for thread_index in range(0, len(self.scroll_threads)):
            if self.scroll_threads[thread_index] is not None and self.scroll_threads[thread_index].is_alive():
                self.scroll_threads_terminate[thread_index] = True
                self.scroll_threads[thread_index].join()
        self.lcd_lock.acquire()
        self.lcd.clear()
        self.lcd_lock.release()


    # row is 0-indexed, default is 0
    def write(self, message, row=0):
        self.mcp.output(3, 1)

        # kill a scrolling thread if there's already one on this row
        if self.scroll_threads[row] is not None and self.scroll_threads[row].is_alive():
            self.scroll_threads_terminate[row] = True
            self.scroll_threads[row].join()

        if len(message) > LCD_WIDTH:
            self.scroll_threads_terminate[row] = False
            self.scroll_threads[row] = Thread(target=scroll, args=[self.lcd, self.lcd_lock, LCD_WIDTH, message, row, lambda:self.scroll_threads_terminate[row]])
            self.scroll_threads[row].start()
            return

        # calculate cursor to place message in center
        difference = LCD_WIDTH - len(message)
        cursor_pos = difference // 2

        self.lcd_lock.acquire()
        self.lcd.setCursor(cursor_pos, row)
        self.lcd.message(message)
        self.lcd_lock.release()


    def stop_scroll(self, row):
        # stop the thread at scroll_threads[row]
        pass


    def __del__(self):
        self.lcd_lock.acquire()
        self.lcd.clear()
        self.lcd_lock.release()

        for thread_index in range(0, len(self.scroll_threads)):
            if self.scroll_threads[thread_index] is not None and self.scroll_threads[thread_index].is_alive():
                self.scroll_threads_terminate[thread_index] = True
                self.scroll_threads[thread_index].join()


def scroll(lcd, lcd_lock, lcd_width, message, row, stop):
    start_pause = 2
    end_pause = 2
    scroll_speed = 0.5  # seconds per character scroll
    while True:
        window_start = 0
        window_end = lcd_width

        lcd_lock.acquire()
        lcd.setCursor(0, row)
        lcd.message(message[window_start:window_end])
        lcd_lock.release()

        time.sleep(start_pause)
        while window_end < len(message):
            if stop():
                return

            window_start += 1
            window_end += 1

            lcd_lock.acquire()
            lcd.setCursor(0, row)
            lcd.message(message[window_start:window_end])
            lcd_lock.release()

            time.sleep(scroll_speed)
        time.sleep(end_pause)
