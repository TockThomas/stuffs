import RPi.GPIO as GPIO
import time

trigger = 1
echo = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

def distanz():
	GPIO.output(trigger, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(trigger, GPIO.LOW)

	while GPIO.input(echo) == 0:
		StartZeit = time.time()
	while GPIO.input(echo) == 1:
		StopZeit = time.time()
	Zeit = StopZeit - StartZeit
	distanz = (Zeit * 34300) / 2
	return distanz