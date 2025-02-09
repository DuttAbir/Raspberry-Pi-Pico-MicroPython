from machine import Pin, ADC, PWM
import time as t

pot_pin = ADC(Pin(26))
pwm_pin = PWM(Pin(16))

#max = 65535

pwm_pin.freq(1000)

while  True :
    pot_val = pot_pin.read_u16()
    
    #pwm_value = int(0.8*max)
    
    pwm_pin.duty_u16(pot_val)
    
    #pot_val_voltage = pot_val*3.3/65535
    
    print(pot_val)
    t.sleep(0.05)
