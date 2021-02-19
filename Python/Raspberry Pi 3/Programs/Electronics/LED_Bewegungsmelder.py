import RPi.GPIO as GPIO
import time

SENSOR = 24 #Variable für Bewegungsmelder (GPIO 24)
LED = 23 #Variable für LED (GPIO 23)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

def bewegung(channel):
    print('Es gab eine Bewegung!')
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED, GPIO.LOW)

try:
    GPIO.add_event_detect(SENSOR, GPIO.RISING, callback=bewegung)
    while True:
        time.sleep(1)
except KeyboardInterrupt:
        print ('Beende...')
GPIO.cleanup()
