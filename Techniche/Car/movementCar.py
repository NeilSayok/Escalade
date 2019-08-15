import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)




mpinA1 = 35
mpinA2 = 36
mpinB1 = 37
mpinB2 = 38

GPIO.setup(mpinA1, GPIO.OUT,initial=1)
GPIO.setup(mpinA2, GPIO.OUT,initial=1)
GPIO.setup(mpinB1, GPIO.OUT,initial=1)
GPIO.setup(mpinB2, GPIO.OUT,initial=1)

def forward():
    
  
    
    GPIO.output(mpinA1,GPIO.HIGH)
    GPIO.output(mpinA2,GPIO.LOW)
    GPIO.output(mpinB1,GPIO.HIGH)
    GPIO.output(mpinB2,GPIO.LOW)

#while True:
#    try:
#        forward()
#    except KeyboardInterrupt:
#        GPIO.cleanup()
#        break
    
forward()
