from machine import ADC
import time

def run():
    print('ADC demo')
    while 1:
        adc = ADC(0)
        print('ADC: ' + str(adc.read()))
        time.sleep(2)