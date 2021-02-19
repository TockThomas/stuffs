from evdev import InputDevice, categorize, ecodes
import RPi.GPIO as GPIO
import time
import tire
import LED
import servo
import buzzer
import fan
import ir

gamepad = InputDevice("/dev/input/event2")

print(gamepad)

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

def sos():
    for i in range(1):
        for i in range(1, 4):
            LED.red()
            buzzer.on()
            time.sleep(0.2)
            LED.off()
            buzzer.off()
            time.sleep(0.2)
        for i in range(1, 4):
            LED.red()
            buzzer.on()
            time.sleep(0.5)
            LED.off()
            buzzer.off()
            time.sleep(0.5)
        for i in range(1, 4):
            LED.red()
            buzzer.on()
            time.sleep(0.2)
            LED.off()
            buzzer.off()
            time.sleep(0.2)

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

servo.default()
x = 6.5
y = 7.5
z = 6
Lenkrad = 0
gas = 0
brake = 0

try:
    for event in gamepad.read_loop():
        print(Lenkung())
        if Lenkung() is not None:
            Lenkrad = Lenkung()
        if RTrigger() is not None:
            gas = RTrigger()
        if LTrigger() is not None:
            brake = LTrigger()
        if Lenkrad <= -30000:
            if gas >= 1:
                tire.run_left(gas)
            elif brake >= 1:
                tire.back_left(brake)
        elif Lenkrad >= 30000:
            if gas >= 1:
                tire.run_right(gas)
            elif brake >= 1:
                tire.back_right(brake)
        elif gas >= 1:
            tire.run(gas)
        elif brake >= 1:
            tire.back(brake)
        elif gas == 0 and brake == 0:
            tire.brake()
        if exitBtn():
            keyboardInterrupt()

finally:
    servo.default()
    time.sleep(0.2)
    GPIO.cleanup()