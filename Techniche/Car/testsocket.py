import socket
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT,initial=0)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind(('',6666))
except socket.error as msg:
    print("Bind Failed")
    sys.exit()
s.listen(1)

conn, addr = s.accept()
print("Connected to : ",addr[0]) 


while True:
    try:
        data = conn.recv(1024)
        line = data.decode('UTF-8')
        #line = line.replace('\n','')
        print(line)
        if '1' in line:
            GPIO.output(8,GPIO.HIGH)
        if '0' in line:
            GPIO.output(8,GPIO.LOW)
        if "exit" in line:
            print("Closed")
            s.close()
            GPIO.cleanup()
            sys.exit()
    except KeyboardInterrupt:
        print("Closed")
        s.close()
        GPIO.cleanup()
        sys.exit()
        

s.close()
