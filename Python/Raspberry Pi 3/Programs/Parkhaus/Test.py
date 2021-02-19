import RPi.GPIO as GPIO
import time

button = 22
button1 = 18
red = 23
green = 24
servoPIN = 27
servoPIN2 = 17
zu = 15
auf = 7


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)
servoe = GPIO.PWM(servoPIN, 50)
servoa = GPIO.PWM(servoPIN2, 50)

servoe.start(zu)
servoa.start(zu)
time.sleep(0.25)
GPIO.output(red, GPIO.HIGH)
GPIO.output(green, GPIO.HIGH)
time.sleep(0.25)
GPIO.output(red, GPIO.LOW)
GPIO.output(green, GPIO.LOW)

while True:
	if GPIO.input(button) == 0:
		GPIO.output(red, GPIO.LOW)
		GPIO.output(green, GPIO.LOW)
		servoe.ChangeDutyCycle(zu)
		servoa.ChangeDutyCycle(zu)
	else:
		GPIO.output(red, GPIO.HIGH)
		GPIO.output(green, GPIO.HIGH)
		servoe.ChangeDutyCycle(auf)
		servoa.ChangeDutyCycle(auf)