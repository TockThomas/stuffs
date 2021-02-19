import RPi.GPIO as GPIO
import time

red = 23
green = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.output(red, GPIO.HIGH)
GPIO.output(green, GPIO.LOW)
time.sleep(5)
GPIO.output(red, GPIO.LOW)
GPIO.output(green, GPIO.HIGH)
time.sleep(5)
GPIO.output(red, GPIO.LOW)
GPIO.output(green, GPIO.LOW)