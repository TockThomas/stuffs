import RPi.GPIO as GPIO
import time

servoPIN1 = 23
servoPIN2 = 11
servoPIN3 = 9

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(servoPIN1, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)
GPIO.setup(servoPIN3, GPIO.OUT)

servo1 = GPIO.PWM(servoPIN1, 50)
servo2 = GPIO.PWM(servoPIN2, 50)
servo3 = GPIO.PWM(servoPIN3, 50)

def default():
    servo1.start(6.5)
    servo2.start(7.5)
    servo3.start(6)
    time.sleep(0.5)

def move1(move):
    servo1.ChangeDutyCycle(move)
    time.sleep(0.2)

def move2(move):
    servo2.ChangeDutyCycle(move)
    time.sleep(0.2)

def move3(move):
    servo3.ChangeDutyCycle(move)
    time.sleep(0.2)