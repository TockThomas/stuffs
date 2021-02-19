import RPi.GPIO as GPIO
import time

servoPIN = 27
servoPIN2 = 17
zu = 15
auf = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN2, GPIO.OUT)

servo = GPIO.PWM(servoPIN2, 50)
servo.start(15)
time.sleep(1)
servo.ChangeDutyCycle(7)
time.sleep(1)
servo.stop()
GPIO.cleanup()
