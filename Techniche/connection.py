import socket
import sys
import RPi.GPIO as GPIO
import motors as m


GPIO.setmode(GPIO.BOARD)

# Main Motors 2
mA1 = 11
mA2 = 12
mB1 = 15
mB2 = 16

# Setting up pins at startup

GPIO.setup(mA1, GPIO.OUT)
GPIO.setup(mA2, GPIO.OUT)
GPIO.setup(mB1, GPIO.OUT)
GPIO.setup(mB2, GPIO.OUT)
GPIO.output(mA1, 1)
GPIO.output(mA2, 1)
GPIO.output(mB1, 1)
GPIO.output(mB2, 1)
# Movement
def left_side_forward():
    #print("FORWARD LEFT")
    GPIO.output(mA1, 1)
    GPIO.output(mA2, 0)
    GPIO.output(mB1, 0)
    GPIO.output(mB2, 1)


def right_side_forward():
    #print("FORWARD RIGHT")
    GPIO.output(mA1, 0)
    GPIO.output(mA2, 1)
    GPIO.output(mB1, 1)
    GPIO.output(mB2, 0)


def forward():
    #print("FORWARD")
    GPIO.output(mA1, 0)
    GPIO.output(mA2, 1)
    GPIO.output(mB1, 0)
    GPIO.output(mB2, 1)


def left_side_reverse():
    #print("BACKWARD LEFT")
    GPIO.output(mA1, 0)
    GPIO.output(mA2, 1)
    GPIO.output(mB1, 1)
    GPIO.output(mB2, 0)


def right_side_reverse():
    #print("BACKWARD RIGHT")
    GPIO.output(mA1, 1)
    GPIO.output(mA2, 0)
    GPIO.output(mB1, 0)
    GPIO.output(mB2, 1)


def reverse():
    #print("BACKWARD")
    GPIO.output(mA1, 1)
    GPIO.output(mA2, 0)
    GPIO.output(mB1, 1)
    GPIO.output(mB2, 0)


def movementStop():
    #print("Movement STOP")
    GPIO.output(mA1, 1)
    GPIO.output(mA2, 1)
    GPIO.output(mB1, 1)
    GPIO.output(mB2, 1)

# End Movement


# functions

def baseWheelMovement(fbJStick, lrJStick):
    print()
    if fbJStick == '-1':
        movementStop()
    elif fbJStick == '2' and lrJStick == '-1':
        #print("HERE FOR")
        forward()
    elif fbJStick == '2' and lrJStick == '4':
        right_side_forward()
    elif fbJStick == '2' and lrJStick == '0':
        left_side_forward()
    elif fbJStick == '6' and lrJStick == '-1':
        reverse()
    elif fbJStick == '6' and lrJStick == '4':
        right_side_reverse()
    elif fbJStick == '6' and lrJStick == '0':
        left_side_reverse()
    else:
        movementStop()


def liftUDfunc(liftUD):
    if liftUD == '-1':
        m.liftUpDownStop()
    elif liftUD == '1':
        m.liftUp()
    elif liftUD == '2':
        m.liftDown()
    else:
        m.liftUpDownStop()


def liftPPfunc(liftPP):
    if liftPP == '-1':
        m.liftPushPullStop()
    elif liftPP == '1':
        m.liftPush()
    elif liftPP == '2':
        m.liftPull()
    else:
        m.liftPushPullStop()


def liftFBfunc(liftFB):
    if liftFB == '-1':
        m.liftRailStop()
    elif liftFB == '1':
        m.liftRailForw()
    elif liftFB == '2':
        m.liftRailBack()
    else:
        m.liftRailStop()


def clawOCfunc(clawOC):
    if clawOC == '-1':
        m.craneOCStop()
    elif clawOC == '1':
        m.craneOpen()
    elif clawOC == '2':
        m.craneClose()
    else:
        m.craneOCStop()


def clawLRfunc(clawLR):
    if clawLR == '-1':
        m.craneLRStop()
    elif clawLR == '1':
        m.craneLeft()
    elif clawLR == '2':
        m.craneRight()
    else:
        m.craneLRStop()

def stopAll():
    m.liftUpDownStop()
    m.liftPushPullStop()
    m.liftRailStop()

    m.movementStop()

    m.craneLRStop()
    m.craneOCStop()


# TODO Finish the servo control
# def clawUDfunc(clawUD):
#     if clawUD == -1:
#         m.liftPushPullStop()
#     elif clawUD == 1:
#         m.liftPush()
#     elif clawUD == 2:
#         m.liftPull()
#     else:
#         m.liftPushPullStop()


# On/Off,LJstick,RJsick,LiUP-Down,LiPush-Pull,LiFor-Back,CLOpen-Close,CLUP-Down,ClLft-Right/
# (0,1),(4,-1,0),(2,-1,6),(1,-1,2),(1,-1,2),(1,-1,2),(1,-1,2),(1,-1,2),(1,-1,2)
# Jstick: 2=For 6=back 4=right 0=left

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind(('', 6666))
    print('Program Started at port 6666')

except socket.error as msg:
    print(msg)
    sys.exit()
s.listen(1)

conn, addr = s.accept()
print("Connected to : ", addr[0])

while True:
    try:
        data = conn.recv(1024)
        # #print(type(data))
        line = data.decode('UTF-8')

        # #print('Size: ',sys.getsizeof(line))

        line = line.replace('\n', '')
        # #print(line)
        lines = line.split('/')
        # #print(len(lines))
        # #print(lines)

        # On/Off,LJstick,RJsick,LiUP-Down,LiPush-Pull,LiFor-Back,CLOpen-Close,CLUP-Down,ClLft-Right/
        # (0,1),(4,-1,0),(2,-1,6),(1,-1,2),(1,-1,2),(1,-1,2),(1,-1,2),(1,-1,2),(1,-1,2)

        for i in lines:
            arr = i.split(',')
            # #print(arr)
            if len(arr) >= 9:
                ##print(arr)
                if arr[0] == '1':

                    baseWheelMovement(arr[2],arr[1])
                    liftUDfunc(arr[3])
                    liftPPfunc(arr[4])
                    liftFBfunc(arr[5])
                    clawOCfunc(arr[6])
                    clawLRfunc(arr[8])

            elif arr[0] == '0':
                stopAll()
            else:
                stopAll()


    except KeyboardInterrupt:
        m.cleanup()
        s.close()
        #print("Closed")
        sys.exit()

s.close()
