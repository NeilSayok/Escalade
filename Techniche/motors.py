import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# Main Motors 2
mA1 = 11
mA2 = 12
mB1 = 15
mB2 = 16

# Crane Left/Right 1
CLR1 = 36
CLR2 = 33

# Crane Open/Close 1
COC1 = 40
COC2 = 38

# Lift Rail Forward/Backward 2 Down to 1
LF1 = 31
LF2 = 32

# Lift Up/Down 1
LU1 = 3


# Claw updown 1
CLUD = 5





# Setting up pins at startup

GPIO.setup(mA1, GPIO.OUT)
GPIO.setup(mA2, GPIO.OUT)
GPIO.setup(mB1, GPIO.OUT)
GPIO.setup(mB2, GPIO.OUT)
GPIO.output(mA1, 1)
GPIO.output(mA2, 1)
GPIO.output(mB1, 1)
GPIO.output(mB2, 1)

GPIO.setup(LU1, GPIO.OUT)
liftudServo=GPIO.PWM(LU1, 50)
liftudServo.start(0)


GPIO.setup(CLUD, GPIO.OUT)
clawUD=GPIO.PWM(CLUD, 50)
clawUD.start(0)

GPIO.setup(LF1, GPIO.OUT)
GPIO.setup(LF2, GPIO.OUT)
GPIO.output(LF1, 1)
GPIO.output(LF2, 1)

GPIO.setup(CLR1, GPIO.OUT)
GPIO.setup(CLR2, GPIO.OUT)
GPIO.output(CLR1, 1)
GPIO.output(CLR2, 1)

GPIO.setup(COC1, GPIO.OUT)
GPIO.setup(COC2, GPIO.OUT)
GPIO.output(COC1, 1)
GPIO.output(COC2, 1)


# Functions:

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


# Lift Up Down

def liftUp():
    #print("Lift Up")
    liftudServo.ChangeDutyCycle(2)


def liftDown():
    #print("Lift Down")
    liftudServo.ChangeDutyCycle(9)


def liftUpDownStop():
    #print("Lift U/D Stop")
    liftudServo.ChangeDutyCycle(0)


# End Lift Up Down




# Lift Rail Forward Backward


def liftRailForw():
    #print("Lift Rail Forward")
    GPIO.output(LF1, 1)
    GPIO.output(LF2, 0)


def liftRailBack():
    #print("Lift Rail Backward")
    GPIO.output(LF1, 0)
    GPIO.output(LF2, 1)


def liftRailStop():
    #print("Lift Rail Stop")
    GPIO.output(LF1, 1)
    GPIO.output(LF2, 1)


# End Lift Rail Forward Backward


# Crane Left Right

def craneLeft():
    #print("Crane Left")
    GPIO.output(CLR1, 1)
    GPIO.output(CLR2, 0)


def craneRight():
    #print("Crane Right")
    GPIO.output(CLR1, 0)
    GPIO.output(CLR2, 1)


def craneLRStop():
    #print("Crane L/R Stop")
    GPIO.output(CLR1, 1)
    GPIO.output(CLR2, 1)


# End Crane Left Right


# Crane Open Close


def craneOpen():
    #print("Crane Open")
    GPIO.output(COC1, 1)
    GPIO.output(COC2, 0)


def craneClose():
    #print("Crane Close")
    GPIO.output(COC1, 0)
    GPIO.output(COC2, 1)


def craneOCStop():
    #print("Crane Open Close Stop")
    GPIO.output(COC1, 1)
    GPIO.output(COC2, 1)


# End Crane Open Close

# Crane UP Down

def craneUP():
    #print("Lift Push")
    clawUD.ChangeDutyCycle(2)


def craneDown():
    #print("Lift Pull")
    clawUD.ChangeDutyCycle(9)


def craneUpDownStop():
    #print("Lift P/P Stop")
    clawUD.ChangeDutyCycle(0)


# End Crane UP Down

def cleanup():
    GPIO.cleanup()

