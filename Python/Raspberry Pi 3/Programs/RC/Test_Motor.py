import RPi.GPIO as GPIO
import time

left = (7,8)    # 7-; 8+
right = (9,10)  # 9+; 10-
GPIO.setwarnings(False)

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(8, GPIO.OUT)
    GPIO.setup(9, GPIO.OUT)
    GPIO.setup(10, GPIO.OUT)

def forward(tf):
    init()
    GPIO.output(7, False)
    GPIO.output(8, True)
    GPIO.output(9, True)
    GPIO.output(10, False)
    time.sleep(tf)
    GPIO.cleanup()

forward(1)
