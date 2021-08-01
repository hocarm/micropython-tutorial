from machine import Pin
import time
def run():
    led = Pin(2, Pin.OUT)
    while 1:
        led.value(1)
        time.sleep(2)
        led.value(0)
        time.sleep(2)