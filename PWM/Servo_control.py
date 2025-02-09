 from machine import Pin, PWM
from time import sleep

#set up PWM pin for servo control
servo_pin = PWM(Pin(0))

#set duty cycle for different angles
max_duty = 7864
min_duty = 1804
half_duty = int(max_duty/2)

#set PWM freq
servo_pin.freq(50)

try:
    while  True :
        servo_pin.duty_u16(min_duty)
        sleep(2)
        servo_pin.duty_u16(half_duty)
        sleep(2)
        servo_pin.duty_u16(max_duty)
        sleep(2)
        
except KeyboardInterrupt:
    print("Keyboard interrupt")
    servo_pin.deinit()