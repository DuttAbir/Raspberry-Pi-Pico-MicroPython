from machine import Pin
import time as t
led = Pin("LED", Pin.OUT)

while  True :
    led.value(1)
    t.sleep(2)
    led.value(0)
    t.sleep(2)