import RPi.GPIO as GPIO
import time

fanPIN = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(fanPIN, GPIO.OUT)

fan = GPIO.PWM(fanPIN, 50)

fan.start(100)

def run():
    fan.ChangeDutyCycle(50)

def run_slow():
    fan.ChangeDutyCycle(70)

def stop():
    fan.ChangeDutyCycle(100)