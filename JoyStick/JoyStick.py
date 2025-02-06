from machine import Pin, ADC
import utime

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))

button = Pin(17, Pin.IN, Pin.PULL_UP)

while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonVal = button.value()
    buttonStatus = "not presses"
    
    if buttonVal==0:
        buttonStatus = "pressed"
        
    print("X : " + str(xValue) +
          "Y : " + str(yValue) +
          "Button : " + buttonStatus)
    
    utime.sleep(0.2)
        