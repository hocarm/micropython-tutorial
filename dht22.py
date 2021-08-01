from machine import Pin
import dht
import time
def run():
    print('dht module test')
    gpio_dht = Pin(5)
    d = dht.DHT22(gpio_dht)
    while 1:
        d.measure()
        temperature = d.temperature()
        humidity = d.humidity()
        print('Temperature: ' + str(temperature) + ' Celsius')
        print('Humidity: ' + str(humidity) + ' % RH')
        time.sleep(2)