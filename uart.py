from machine import UART
import time

def run():
    print('test UART')
    uart = UART(0, baudrate=9600)
    counter = 50
    while 1:
        uart.write(str(counter) + '\r\n')
        time.sleep(2)
        counter += 1
        if counter > 70:
            counter = 50