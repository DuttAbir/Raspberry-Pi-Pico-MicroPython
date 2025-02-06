from machine import Pin
import time

Touch_pad = Pin(18, Pin.IN, Pin.PULL_DOWN)

led = Pin(19, Pin.OUT)

while True:
    if Touch_pad.value():
        print("Touched")
        
        led.toggle()
        
        time.sleep(0.5)