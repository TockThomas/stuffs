import RPi.GPIO as GPIO
import time

button = 22
red = 23
green = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

while True:
    if GPIO.input(button) == 0:
        GPIO.output(red, GPIO.LOW)
        GPIO.output(green, GPIO.LOW)
    else:
        GPIO.output(red, GPIO.HIGH)
        GPIO.output(green, GPIO.HIGH)