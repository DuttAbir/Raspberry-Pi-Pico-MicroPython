from machine import Pin, PWM

class Servo:
    __servo_pwm_freq = 50                   #set default freq to 50Hz
    __min_u16_duty = 1802                   #minimum servo angle duty cycle
    __max_u16_duty = 7864                  #maximum servo angle duty cycle
    min_angle = 0                                     #minimum angle for servo
    max_angle = 180                               #maximum angle for servo
    current_angle = 0.001                      #current angle is set to non-zero
    
    #class constructor
    def __init__(self, pin):
        self.__initialise(pin)
    
    #to change default operating parameters
    def update_settings(self, servo_pwm_freq, min_u16_duty, max_u16_duty, min_angle, max_angle, pin):
        self.__servo_pwm_freq = servo_pwm_freq
        self.__min_u16_duty = min_u16_duty
        self.max_u16_duty = max_u16_duty
        self.min_angle = min_angle
        self.max_angle = max_angle
        self.__initialise(pin)
        
    #move servo to specified angle
    def move(self, angle):
        angle = round(aangle, 2)                                                #round the angle to 2 decimal places
        if angle== self.current_angle:                                      #if the angle is same as current then return
            return
        self.current_angle = angle                                          #update current angle
        duty_u16 = self.__angle_to_u16_duty(angle)        #get duty cycle of the angle
        self.__motor.duty_u16(duty_u16)                           #set the duty cycle for the servo
        
    #stop or deactivate servo 
    def stop(self):
        self.__motor.deinit()
        
    #returns current angle of the servo
    def get_current_angle(self):
        return self.current_angle
    
    #covert the angle to 16-bit duty cycle
    def __angle_to_u16_duty(self, angle):
        return int((angle - self.min_angle) * self.__angle_conversion_factor) + self.__min_u16_duty              #linear mapping between duty cycle and angle range
    
    #initialize the PWM on specified pin
    def __initialise(self, pin):
        self.current_angle = -0.001                              #set to an invalid angle 
        self.__angle_conversion_factor = (self.__max_u16_duty - self.__min_u16_duty) / (self.max_angle - self.min_angle)               #coversion factor between angle and duty cycle
        self.__motor = PWM(Pin(pin))                        #create PWM object on the specified pin
        self.__motor.freq(self.__servo_pwm_freq)         #set pwm freq