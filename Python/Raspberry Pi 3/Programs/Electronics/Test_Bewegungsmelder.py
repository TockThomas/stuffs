import RPi.GPIO as GPIO
import time

SENSOR = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR, GPIO.IN)

def bewegung(channel):
    print('Es gab eine Bewegung!')

try:
    GPIO.add_event_detect(SENSOR , GPIO.RISING, callback=bewegung)
    while True:
        time.sleep(1)
except KeyboardInterrupt:
        print ('Beende...')
GPIO.cleanup()
