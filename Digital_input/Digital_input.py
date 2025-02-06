from machine import Pin
import time as t

button = Pin(15, Pin.IN, Pin.PULL_DOWN)

while True:
    print(button.value())
    t.sleep(0.1)