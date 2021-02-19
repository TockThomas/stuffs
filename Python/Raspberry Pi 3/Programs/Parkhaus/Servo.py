import RPi.GPIO as GPIO
import time

servoPIN = 27
servoPIN2 = 17
zu = 15
auf = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)


servo = GPIO.PWM(servoPIN, 50)
servo1 = GPIO.PWM(servoPIN2, 50)

servo.start(zu)
servo1.start(zu)

def servo_auf(zeit=0):
    servo.ChangeDutyCycle(auf)
    time.sleep(zeit)

def servo_zu(zeit=0):
    servo.ChangeDutyCycle(zu)
    time.sleep(zeit)

def servo1_auf(zeit=0):
    servo1.ChangeDutyCycle(auf)
    time.sleep(zeit)

def servo1_zu(zeit=0):
    servo1.ChangeDutyCycle(zu)
    time.sleep(zeit)

