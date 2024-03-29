from lcd import drivers
import time
import datetime
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
PIN = 4

display = drivers.Lcd()

try:
    print("Writing to display")
    while True:
        now = datetime.datetime.now()
        display.lcd_display_string(now.strftime("%x %X"),1)
        humidity, temperature = Adafruit_DHT.read_retry(sensor, PIN)
        if humidity is not None and temperature is not None:
            display.lcd_display_string(f"{temperature:.1f}*C, {humidity:.1f}%",2)
        else:
            display.lcd_display_string('Read error',2)

finally:
    print("Cleaning up!")
    display.lcd_clear()

