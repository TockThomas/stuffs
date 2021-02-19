import RPi.GPIO as GPIO
from datetime import datetime

pin = 2
Buttons = [0x20e, 0x20f, 0x20e, 0x41a, 0x413]
ButtonsName = ["up", "left", "right", "down", "ok"]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

def getBinary():
	num1s = 0
	binary = 1
	command = []
	previousValue = 0
	value = GPIO.input(pin)

	while value:
		value = GPIO.input(pin)

	startTime = datetime.now()

	while True:
		if previousValue != value:
			now = datetime.now()
			pulseTime = now - startTime
			startTime = now
			command.append((previousValue, pulseTime.microseconds))

		if value:
			num1s += 1
		else:
			num1s = 0
		if num1s >10000:
			break
		previousValue = value
		value = GPIO.input(pin)

	for (typ, tme) in command:
		if typ == 1:
			if tme > 1000:
				binary = binary * 10 + 1
			else:
				binary *= 10

	if len(str(binary)) > 34:
		binary = int(str(binary)[:34])

	return binary

def convertHex(binaryValue):
	tmpB2 = int(str(binaryValue), 2)
	return hex(tmpB2)

while True:
	inData = convertHex(getBinary())
	for button in range(len(Buttons)):
		if hex(Buttons[button]) == inData:
			print(ButtonsName[button])