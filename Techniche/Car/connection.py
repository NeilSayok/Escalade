import socket
import sys
import RPi.GPIO as GPIO
import motors as m


# functions

def baseWheelMovement(fbJStick, lrJStick):
    if fbJStick == -1:
        m.movementStop()
    elif fbJStick == 2 and lrJStick == -1:
        m.forward()
    elif fbJStick == 2 and lrJStick == 4:
        m.right_side_forward()
    elif fbJStick == 2 and lrJStick == 0:
        m.left_side_forward()
    elif fbJStick == 6 and lrJStick == -1:
        m.reverse()
    elif fbJStick == 6 and lrJStick == 4:
        m.right_side_reverse()
    elif fbJStick == 6 and lrJStick == 0:
        m.left_side_reverse()
    else:
        m.movementStop()


def liftMovements(liftUD,liftPP,liftFB):
    if liftUD == -1:
        m.liftUpDownStop()
    if liftPP == -1:
        m.liftPushPullStop()




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
        # print(type(data))
        line = data.decode('UTF-8')

        # print('Size: ',sys.getsizeof(line))

        line = line.replace('\n', '')
        # print(line)
        lines = line.split('/')
        # print(len(lines))
        # print(lines)

        # On/Off,LJstick,RJsick,LiUP-Down,LiPush-Pull,LiFor-Back,CLOpen-Close,CLUP-Down,ClLft-Right/
        # (0,1),(4,-1,0),(2,-1,6),(1,-1,2),(1,-1,2),(1,-1,2),(1,-1,2),(1,-1,2),(1,-1,2)

        for i in lines:
            arr = i.split(',')
            # print(arr)
            if len(arr) >= 9:
                if arr[0] == '1':
                    # print(arr[1]+" : "+arr[3])

                    if arr[1] == '-1' and arr[2] == '-1':
                        m.stop()
                    elif arr[1] == '-1' and arr[2] == '2':
                        m.forward()
                    elif arr[1] == '-1' and arr[2] == '6':
                        m.reverse()
                    elif arr[1] == '0' and arr[2] == '2':
                        m.left_side_forward()
                    elif arr[1] == '4' and arr[2] == '2':
                        m.right_side_forward()
                    elif arr[1] == '0' and arr[2] == '6':
                        m.left_side_reverse()
                    elif arr[1] == '4' and arr[2] == '6':
                        m.right_side_reverse()
                    else:
                        m.stop()
            elif arr[0] == '0':
                m.stop()


    except KeyboardInterrupt:
        GPIO.cleanup()
        s.close()
        print("Closed")
        sys.exit()

s.close()
