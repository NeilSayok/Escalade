import RPi.GPIO as GPIO


servoPin = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPin, GPIO.OUT)

#116
pwm=GPIO.PWM(servoPin, 38)
pwm.start(0)





#dutyCycle = 0.1
dutyCycle = float(input("DutyCycle: "))
while dutyCycle != -1:
        #print(dutyCycle)
        pwm.ChangeDutyCycle(dutyCycle)
        #dutyCycle = dutyCycle + 0.1
        try:
                dutyCycle = float(input("DutyCycle: "))
        except:
                dutyCycle = float(input("DutyCycle: "))

pwm.stop()
GPIO.cleanup()
