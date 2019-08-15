import RPi.GPIO as GPIO
import time

m11=35
m12=36
m21=37
m22=38

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
GPIO.setup(m21, GPIO.OUT)
GPIO.setup(m22, GPIO.OUT)
GPIO.output(m11 , 1)
GPIO.output(m12 , 1)
GPIO.output(m21, 1)
GPIO.output(m22, 1)

def left_side_forward():
    print ("FORWARD LEFT")
    GPIO.output(m21 , 0)
    GPIO.output(m22 , 1)
    GPIO.output(m11 , 1)
    GPIO.output(m12 , 0)
def right_side_forward():
   print ("FORWARD RIGHT")
   GPIO.output(m21 , 1)
   GPIO.output(m22 , 0)
   GPIO.output(m11 , 0)
   GPIO.output(m12 , 1)
def forward():
   print ("FORWARD")
   GPIO.output(m11 , 0)
   GPIO.output(m12 , 1)
   GPIO.output(m21 , 0)
   GPIO.output(m22 , 1)
def left_side_reverse():
   print ("BACKWARD LEFT")
   GPIO.output(m21 , 1)
   GPIO.output(m22 , 0)
   GPIO.output(m11 , 0)
   GPIO.output(m12 , 1)
def right_side_reverse():
   print ("BACKWARD RIGHT")
   GPIO.output(m21 , 0)
   GPIO.output(m22 , 1)
   GPIO.output(m11 , 1)
   GPIO.output(m12 , 0)
def reverse():
   print ("BACKWARD")
   GPIO.output(m11 , 1)
   GPIO.output(m12 , 0)
   GPIO.output(m21 , 1)
   GPIO.output(m22 , 0)
def stop():
   print ("STOP")
   GPIO.output(m11 , 1)
   GPIO.output(m12 , 1)
   GPIO.output(m21 , 1)
   GPIO.output(m22 , 1)



