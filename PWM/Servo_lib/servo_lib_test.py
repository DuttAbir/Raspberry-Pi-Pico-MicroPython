from servo import Servo
from time import sleep

servo =Servo(pin=0)

try:
    while  True :
        servo.move(0)
        sleep(2)
        servo.move(90)
        sleep(2)
        servo.move(180)
        sleep(2)
        
except  KeyboardInterrupt:
    print("Keyboard interrupt")
    servo.stop()