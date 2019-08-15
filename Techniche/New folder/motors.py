import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# Main Motors 2
mA1 = 11
mA2 = 12
mB1 = 13
mB2 = 15

# Lift Up/Down 1
LU1 = 32
LU2 = 33

# Lift Push/Pull 1
LP1 = 36
LP2 = 38

# Lift Rail Forward/Backward 2 Down to 1
LF1 = 35
LF2 = 37

# Crane Left/Right 1
CLR1 = 16
CLR2 = 18

# Crane Open/Close 1
COC1 = 29
COC2 = 31

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
GPIO.setup(LU2, GPIO.OUT)
GPIO.output(LU1, 1)
GPIO.output(LU1, 1)

GPIO.setup(LP1, GPIO.OUT)
GPIO.setup(LP2, GPIO.OUT)
GPIO.output(LP1, 1)
GPIO.output(LP2, 1)

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
    print("FORWARD LEFT")
    GPIO.output(mA1, 1)
    GPIO.output(mA2, 0)
    GPIO.output(mB1, 0)
    GPIO.output(mB2, 1)


def right_side_forward():
    print("FORWARD RIGHT")
    GPIO.output(mA1, 0)
    GPIO.output(mA2, 1)
    GPIO.output(mB1, 1)
    GPIO.output(mB2, 0)


def forward():
    print("FORWARD")
    GPIO.output(mA1, 0)
    GPIO.output(mA2, 1)
    GPIO.output(mB1, 0)
    GPIO.output(mB2, 1)


def left_side_reverse():
    print("BACKWARD LEFT")
    GPIO.output(mA1, 0)
    GPIO.output(mA2, 1)
    GPIO.output(mB1, 1)
    GPIO.output(mB2, 0)


def right_side_reverse():
    print("BACKWARD RIGHT")
    GPIO.output(mA1, 1)
    GPIO.output(mA2, 0)
    GPIO.output(mB1, 0)
    GPIO.output(mB2, 1)


def reverse():
    print("BACKWARD")
    GPIO.output(mA1, 1)
    GPIO.output(mA2, 0)
    GPIO.output(mB1, 1)
    GPIO.output(mB2, 0)


def movementStop():
    print("STOP")
    GPIO.output(mA1, 1)
    GPIO.output(mA2, 1)
    GPIO.output(mB1, 1)
    GPIO.output(mB2, 1)


# End Movement


# Lift Up Down

def liftUp():
    print("Lift Up")
    GPIO.output(LU1, 1)
    GPIO.output(LU2, 0)


def liftDown():
    print("Lift Down")
    GPIO.output(LU1, 0)
    GPIO.output(LU2, 1)


def liftUpDownStop():
    print("Lift U/D Stop")
    GPIO.output(LU1, 1)
    GPIO.output(LU2, 1)


# End Lift Up Down


# Lift Push Pull

def liftPush():
    print("Lift Push")
    GPIO.output(LP1, 1)
    GPIO.output(LP2, 0)


def liftPull():
    print("Lift Pull")
    GPIO.output(LP1, 0)
    GPIO.output(LP2, 1)


def liftPushPullStop():
    print("Lift P/P Stop")
    GPIO.output(LP1, 1)
    GPIO.output(LP2, 1)


# End Lift Push Pull

# Lift Rail Forward Backward


def liftRailForw():
    print("Lift Rail Forward")
    GPIO.output(LF1, 1)
    GPIO.output(LF2, 0)


def liftRailBack():
    print("Lift Rail Backward")
    GPIO.output(LF1, 0)
    GPIO.output(LF2, 1)


def liftRailStop():
    print("Lift Rail Stop")
    GPIO.output(LF1, 1)
    GPIO.output(LF2, 1)


# End Lift Rail Forward Backward


# Crane Left Right

def craneLeft():
    print("Crane Left")
    GPIO.output(CLR1, 1)
    GPIO.output(CLR2, 0)


def craneRight():
    print("Crane Right")
    GPIO.output(CLR1, 0)
    GPIO.output(CLR2, 1)


def craneLRStop():
    print("Crane Stop")
    GPIO.output(CLR1, 1)
    GPIO.output(CLR2, 1)


# End Crane Left Right


# Crane Open Close


def craneOpen():
    print("Crane Left")
    GPIO.output(COC1, 1)
    GPIO.output(COC2, 0)


def craneClose():
    print("Crane Right")
    GPIO.output(COC1, 0)
    GPIO.output(COC2, 1)


def craneOCStop():
    print("Crane Open Close Stop")
    GPIO.output(COC1, 1)
    GPIO.output(COC2, 1)


# End Crane Open Close

def cleanup():
    GPIO.cleanup()

