from machine import Pin, SPI
import time


def run():
    print('test spi')
    gpio_sck = Pin(5)
    gpio_mosi = Pin(4)
    gpio_miso = Pin(0)

    spi = SPI(-1, baudrate=100000, polarity=1, phase=0, sck=gpio_sck, mosi=gpio_mosi, miso=gpio_miso)
    val = 65
    while 1:
        spi.write(chr(val))     # write 1 byte to spi
        print('write spi: ' + str(val))

        time.sleep(2)
        val += 1
        if val > 90:
            val = 65
