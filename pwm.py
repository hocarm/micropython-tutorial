from machine import Pin, PWM
import time
gpio_red = 5
gpio_green = 4
gpio_blue = 0
def set_rgb(red, green, blue):
    pwm_red = PWM(Pin(gpio_red), freq=1000, duty=red)
    pwm_green = PWM(Pin(gpio_green), freq=1000, duty=green)
    pwm_blue = PWM(Pin(gpio_blue), freq=1000, duty=blue)
    time.sleep(2)
    pwm_red.deinit()
    pwm_green.deinit()
    pwm_blue.deinit()
def run():
    print('print PWM with RGB led')
    while 1:
        print('red')
        set_rgb(1023, 0, 0)
        print('green')
        set_rgb(0, 1023, 0)
        print('blue')
        set_rgb(0, 0, 1023)
        print('yellow')
        set_rgb(1023, 1023, 0)
        print('purple')
        set_rgb(323, 0, 323)
        print('aqua')
        set_rgb(0, 1023, 1023)