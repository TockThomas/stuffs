import RPi.GPIO as GPIO
import time

red = 23
green = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

def red_on(zeit=0):
    GPIO.output(red, GPIO.HIGH)
    time.sleep(zeit)

def red_off(zeit=0):
    GPIO.output(red, GPIO.LOW)
    time.sleep(zeit)

def green_on(zeit=0):
    GPIO.output(green, GPIO.HIGH)
    time.sleep(zeit)

def green_off(zeit=0):
    GPIO.output(green, GPIO.LOW)
    time.sleep(zeit)