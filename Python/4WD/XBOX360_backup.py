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

def TriggerBerechnung():
	if event.type == ecodes.EV_ABS:
		if event.code == RT or event.code == LT:
			Trigger = event.value
			#print(Trigger)
			Trigger = Trigger / 12.75
			return Trigger
	return 0

def links():
	if event.type == ecodes.EV_ABS:
		if event.code == left_x_stick:
			if event.value <= -30000:
				return True
	return False

def rechts():
	if event.type == ecodes.EV_ABS:
		if event.code == left_x_stick:
			if event.value >= 30000:
				return True
	return False

def rechner(Richtung):
	Trigger = TriggerBerechnung()
	Richtung = Richtung * Trigger / 20
	return Richtung

'''
def Lsticks():
	stick = None
	Trigger = TriggerBerechnung()
	if event.type == ecodes.EV_ABS:
		if event.code == left_x_stick:
			if event.value <= -30000:
				stick = 1
			elif event.value >= 30000:
				stick = 2
			else:
				stick = 0
	if stick == 0:
		speed = 20 * Trigger / 20
		return speed
	elif stick == 1:
		speed = 2 * Trigger / 20
		return speed
	elif stick == 2:
		speed = 20 * Trigger / 20
		return speed

def Rsticks():
	stick = None
	Trigger = TriggerBerechnung()
	if event.type == ecodes.EV_ABS:
		if event.code == left_x_stick:
			if event.value <= -30000:
				stick = 1
			elif event.value >= 30000:
				stick = 2
			else:
				stick = 0
	if stick == 0:
		speed = 20 * Trigger / 20
		return speed
	elif stick == 1:
		speed = 20 * Trigger / 20
		return speed
	elif stick == 2:
		speed = 2 * Trigger / 20
		return speed


def LspeedBerechnung():
	Trigger = TriggerBerechnung()
	if event.type == ecodes.EV_ABS:
		if event.code == left_x_stick:
			if event.value <= -30000:
				speed = 2 * Trigger / 20
				return speed
			else:
				return Trigger


def RspeedBerechnung():
	Trigger = TriggerBerechnung()
	if event.type == ecodes.EV_ABS:
		if event.code == 0:
			if event.value >= 30000:
				speed = 2 * Trigger / 20
				return speed
			else:
				return Trigger
'''

servo.default()
x = 6.5
y = 7.5
z = 6

for event in gamepad.read_loop():
	if event.type == ecodes.EV_ABS:
		if event.code == RT:
			if event.value >= 0:
				if links:
					tire.run(rechner(2), rechner(20))
				elif rechts:
					tire.run(rechner(20), rechner(2))
				else:
					tire.run(TriggerBerechnung(), TriggerBerechnung())
			if event.code == LT:
				tire.back(Lsticks(), Rsticks())
		else:
			tire.brake()
	elif event.type == ecodes.EV_KEY:
		if event.value == 1:
			if event.code == guide:
				KeyboardInterrupt()