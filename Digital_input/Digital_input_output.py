from machine import Pin
import time as t

button = Pin(15, Pin.IN,  Pin.PULL_DOWN)
led = Pin(16, Pin.OUT)

while  True :
    if button.value() == 1:
        led.value(1)
    else:
        led.value(0)