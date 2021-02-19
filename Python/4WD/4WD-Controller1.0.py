from evdev import InputDevice, categorize, ecodes
import RPi.GPIO as GPIO
import time

gamepad = InputDevice("/dev/input/event2")

print(gamepad)

#PINs

IN1 = 20 #Linke Reifenseite nach vorne
IN2 = 21 #Linke Reifenseite nach hinten
IN3 = 19 #Rechte Reifenseite nach vorne
IN4 = 26 #Rechte Reifenseite nach hinten
ENA = 16
ENB = 13
servoPIN1 = 23
servoPIN2 = 11
servoPIN3 = 9

#Controller_Mapping
#EV_KEY

aBtn = 304
bBtn = 305
xBtn = 307
yBtn = 308

LB = 310
RB = 311
L3 = 317
R3 = 318

start = 315
back = 314
guide = 316

#EV_ABS

LT = 2 #val.:0-255
RT = 5 #val.:0-255

UP = 17 #val.:-1
DOWN = 17 #val.:1
LEFT = 16 #val.:-1
RIGHT = 16 #val.:1

left_y_stick = 1 #val.:-32768-32767 (von oben nach unten)
left_x_stick = 0 #val.:-32768-32767 (von links nach rechts)
right_y_stick = 4 #val.:-32768-32767 (von oben nach unten)
right_x_stick = 3 #val.: -32768-32767 (von links nach rechts)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(servoPIN1, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)
GPIO.setup(servoPIN3, GPIO.OUT)
GPIO.output(ENA, GPIO.HIGH)
GPIO.output(ENB, GPIO.HIGH)
ENA_PWM = GPIO.PWM(ENA, 2000)
ENB_PWM = GPIO.PWM(ENB, 2000)
servo1 = GPIO.PWM(servoPIN1, 50)
servo2 = GPIO.PWM(servoPIN2, 50)
servo3 = GPIO.PWM(servoPIN3, 50)
ENA_PWM.start(0)
ENB_PWM.start(0)

def run(speed=20, zeit=0):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(speed)
    ENB_PWM.ChangeDutyCycle(speed)
    time.sleep(zeit)

def runfast(zeit=0):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(100)
    ENB_PWM.ChangeDutyCycle(100)
    time.sleep(zeit)

def back(speed=20, zeit=0):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    ENA_PWM.ChangeDutyCycle(speed)
    ENB_PWM.ChangeDutyCycle(speed)
    time.sleep(zeit)

def run_left(speed=20, zeit=0):
    ENA = 1 * speed / 20
    ENB = 30 * speed / 20
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(ENA)
    ENB_PWM.ChangeDutyCycle(ENB)
    time.sleep(zeit)

def run_right(speed=20, zeit=0):
    ENA = 30 * speed / 20
    ENB = 1 * speed / 20
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(ENA)
    ENB_PWM.ChangeDutyCycle(ENB)
    time.sleep(zeit)

def back_left(speed=20, zeit=0):
    ENA = 1 * speed / 20
    ENB = 30 * speed / 20
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    ENA_PWM.ChangeDutyCycle(ENA)
    ENB_PWM.ChangeDutyCycle(ENB)
    time.sleep(zeit)

def back_right(speed=20, zeit=0):
    ENA = 30 * speed / 20
    ENB = 1 * speed / 20
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    ENA_PWM.ChangeDutyCycle(ENA)
    ENB_PWM.ChangeDutyCycle(ENB)
    time.sleep(zeit)

def stop(zeit=0):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(20)
    ENB_PWM.ChangeDutyCycle(20)
    time.sleep(zeit)

def default():
    servo1.start(6.5)
    servo2.start(7.5)
    servo3.start(6)
    time.sleep(0.5)

def RTrigger():
    if event.type == ecodes.EV_ABS:
        if event.code == RT:
            Trigger = event.value / 12.75
            #print(Trigger)
            return Trigger

def LTrigger():
    if event.type == ecodes.EV_ABS:
        if event.code == LT:
            Trigger = event.value / 12.75
            return Trigger

def Lenkung():
    if event.type == ecodes.EV_ABS:
        if event.code == left_x_stick:
            Stick = event.value
            return Stick

def exitBtn():
    if event.type == ecodes.EV_KEY:
        if event.code == guide:
            if event.value == 1:
                return True

default()
Lenkrad = 0
gas = 0
brake = 0

try:
    for event in gamepad.read_loop():
        if Lenkung() is not None:
            Lenkrad = Lenkung()
        if RTrigger() is not None:
            gas = RTrigger()
        if LTrigger() is not None:
            brake = LTrigger()
        if Lenkrad <= -30000:
            if gas >= 1:
                run_left(gas)
            elif brake >= 1:
                back_left(brake)
        elif Lenkrad >= 30000:
            if gas >= 1:
                run_right(gas)
            elif brake >= 1:
                back_right(brake)
        elif gas >= 1:
            run(gas)
        elif brake >= 1:
            back(brake)
        elif gas == 0 and brake == 0:
            stop()
        if exitBtn():
            break

finally:
    default()
    GPIO.cleanup()