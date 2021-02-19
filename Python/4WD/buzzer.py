import RPi.GPIO as GPIO
import time

buzzer = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)

def on(zeit=0):
	GPIO.output(buzzer, GPIO.LOW)
	time.sleep(zeit)

def off(zeit=0):
	GPIO.output(buzzer, GPIO.HIGH)
	time.sleep(zeit)