from machine import Pin
def run():
    print('Button LED digital I/O')
    led = Pin(5, Pin.OUT) # create output pin on GPIO16
    button = Pin(4, Pin.IN) # create output pin on GPIO5
    while 1:
        state = button.value()
        if state > 0:
            led.value(1)
        else:
            led.value(0)