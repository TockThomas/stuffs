import RPi.GPIO as GPIO
from evdev import InputDevice, ecodes
import time
import signal

#Controller-Abteilung
gamepad = InputDevice('/dev/input/event2')

aBtn = 305
bBtn = 306
xBtn = 304
yBtn = 307
PSBtn = 316

l2 = 310
r2 = 311
l1 = 308
r1 = 309

start = 313
select = 312

l3 = 314
r3 = 315

#Motor-Abteilung
left = (7,8)    # 7-; 8+
right = (9,10)  # 9+; 10-
GPIO.setwarnings(False)

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(9, GPIO.OUT)
    GPIO.setup(10, GPIO.OUT)

def steht():
    init()
    GPIO.output(7, False)
    GPIO.output(8, False)
    GPIO.output(9, False)
    GPIO.output(10, False)

def vorwaerts():
    init()
    GPIO.output(7, False)
    GPIO.output(8, True)
    GPIO.output(9, True)
    GPIO.output(10, False)

def rueckwaerts():
    init()
    GPIO.output(7, True)
    GPIO.output(8, False)
    GPIO.output(9, False)
    GPIO.output(10, True)

#Befehle
print(gamepad)

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == r2:
                print("Vorwärts")
                vorwaerts()
            elif event.code == l2:
                print("Rückwärts")
                rueckwaerts()
            elif event.code == PSBtn:
                print("Tschüss")
                KeyboardInterrupt
        elif event.value == 0:
            steht()
                
