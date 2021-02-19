import RPi.GPIO as GPIO
from evdev import InputDevice, ecodes
import time

#Controller-Abteilung
gamepad = InputDevice('/dev/input/event2')

aBtn = 305
bBtn = 306
xBtn = 304
yBtn = 307
home = 316

l2 = 310
r2 = 311
l1 = 308
r1 = 309

start = 313
select = 312

l3 = 314
r3 = 315

dpabhorizontal = 16 # link -1; rechts 1
dpadsenkrecht = 17 # oben -1; unten 1

rt = 4 #0-255
lt = 3
maxtrigger = 255

#Motor-Abteilung
left = (7,8)    # 7-; 8+
right = (9,10)  # 9+; 10-
GPIO.setwarnings(False)

#Lenkungsgrad-Rechnung
#Rechnung: StromDutyCycle * tatsächliche Trigger / Maximale Trigger
for event in gamepad.read_loop():
    if event.type == ecodes.EV_ABS:
        if event.code == rt:
            rtvalue = event.value

rttrigger = 100 * rtvalue / maxtrigger

for event in gamepad.read_loop():
    if event.type == ecodes.EV_ABS:
        if event.code == lt:
            ltvalue = event.value

lttrigger = 100 * lttrigger / maxtrigger

#defs

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

def vorwaertslinks():
    init()
    GPIO.output(7, False)
    GPIO.output(8, False)
    GPIO.output(9, True)
    GPIO.output(10, False)

def vorwaertsrechts():
    init()
    GPIO.output(7, False)
    GPIO.output(8, True)
    GPIO.output(9, False)
    GPIO.output(10, False)

def rueckwaerts():
    init()
    GPIO.output(7, True)
    GPIO.output(8, False)
    GPIO.output(9, False)
    GPIO.output(10, True)

def rueckwaertslinks():
    init()
    GPIO.output(7, False)
    GPIO.output(8, False)
    GPIO.output(9, False)
    GPIO.output(10, True)

def rueckwaertsrechts():
    init()
    GPIO.output(7, True)
    GPIO.output(8, False)
    GPIO.output(9, False)
    GPIO.output(10, False)


#Befehle
print(gamepad)

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == r2:
                print("Vorwärts")
                vorwaerts()
                if event.code == dpadhorizontal:
                    if event.value == -1:
                        print("Vorwärtslinks")
                        vorwaertslinks()
                    elif event.value == 1:
                        print("Vorwärtsrechts")
                        vorwaertsrechts()
            elif event.code == l2:
                print("Rückwärts")
                rueckwaerts()
                if event.code == dpadsenkrecht:
                    if event.value == -1:
                        rueckwaertslinks()
                    elif event.value == 1:
                        rueckwaertsrechts()
            elif event.code == home:
                print("Tschüss")
                KeyboardInterrupt
        elif event.value == 0:
            steht()