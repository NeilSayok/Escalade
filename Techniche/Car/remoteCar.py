# problems are :
# The strings are getting concatanated
#so we have to send some kind of ending string along with the message

import RPi.GPIO as GPIO
import socket
import sys

GPIO.cleanup()

m11=11
m12=12
m21=15
m22=16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
GPIO.setup(m21, GPIO.OUT)
GPIO.setup(m22, GPIO.OUT)
GPIO.output(m11 , 1)
GPIO.output(m12 , 1)
GPIO.output(m21, 1)
GPIO.output(m22, 1)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def left_side_forward():
    #print ("FORWARD LEFT")
    GPIO.output(m21 , 0)
    GPIO.output(m22 , 1)
    GPIO.output(m11 , 1)
    GPIO.output(m12 , 0)
def right_side_forward():
   #print ("FORWARD RIGHT")
   GPIO.output(m21 , 1)
   GPIO.output(m22 , 0)
   GPIO.output(m11 , 0)
   GPIO.output(m12 , 1)
def forward():
   #print ("FORWARD")
   GPIO.output(m11 , 0)
   GPIO.output(m12 , 1)
   GPIO.output(m21 , 0)
   GPIO.output(m22 , 1)
def left_side_reverse():
   #print ("BACKWARD LEFT")
   GPIO.output(m21 , 1)
   GPIO.output(m22 , 0)
   GPIO.output(m11 , 0)
   GPIO.output(m12 , 1)
def right_side_reverse():
   #print ("BACKWARD RIGHT")
   GPIO.output(m21 , 0)
   GPIO.output(m22 , 1)
   GPIO.output(m11 , 1)
   GPIO.output(m12 , 0)
def reverse():
   #print ("BACKWARD")
   GPIO.output(m11 , 1)
   GPIO.output(m12 , 0)
   GPIO.output(m21 , 1)
   GPIO.output(m22 , 0)
def stop():
   #print ("STOP")
   GPIO.output(m11 , 1)
   GPIO.output(m12 , 1)
   GPIO.output(m21 , 1)
   GPIO.output(m22 , 1)

try:
    s.bind(('',6666))
except socket.error as msg:
    print(msg)
    sys.exit()
s.listen(1)

conn, addr = s.accept()
print("Connected to : ",addr[0])


while True:
    try:
        data = conn.recv(1024)
        #print(type(data))
        line = data.decode('UTF-8')
        
        #print('Size: ',sys.getsizeof(line))
        
        
        line = line.replace('\n','')
        #print(line)
        lines = line.split('/')
        #print(len(lines))
        #print(lines)
        
        for i in lines:
            arr = i.split(',')
            if len(arr) >= 9:
                if arr[0] == '1':
                    #print(arr[1]+" : "+arr[3])
                    
                    if arr[1] == '-1' and arr[2] == '-1':
                        stop()
                    elif arr[1] == '-1' and arr[2] == '2':
                        forward()
                    elif arr[1] == '-1' and arr[2] == '6':
                        reverse()
                    elif arr[1] == '0' and arr[2] == '2':
                        left_side_forward()
                    elif arr[1] == '4' and arr[2] == '2':    
                        right_side_forward()
                    elif arr[1] == '0'and arr[2] == '6':     
                        left_side_reverse()
                    elif arr[1] == '4' and arr[2] == '6':     
                        right_side_reverse()
                    else:
                        stop()
            elif arr[0] == '0':
                stop()
        
        
    except KeyboardInterrupt:
        GPIO.cleanup()
        s.close()
        print("Closed")
        sys.exit()
        

s.close()
