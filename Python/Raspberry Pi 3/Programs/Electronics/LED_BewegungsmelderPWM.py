import RPi.GPIO as GPIO
import time

SENSOR = 24 
LED = 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
pwm = GPIO.PWM(LED, 50)

def bewegung(channel):
    print('Es gab eine Bewegung!')
    import RPi.GPIO as GPIO
    import time
    pwm.start(50)
    pwm.ChangeDutyCycle(10)
    time.sleep(2)
    pwm.ChangeFrequency(10)
    time.sleep(2)
    pwm.ChangeDutyCycle(80)
    time.sleep(2)
    pwm.ChangeFrequency(50)
    time.sleep(2)
    pwm.stop()

try:
    GPIO.add_event_detect(SENSOR , GPIO.RISING, callback=bewegung)
    while True:
        time.sleep(1)
except KeyboardInterrupt: #Strg+C
        print ('Beende...')
GPIO.cleanup()

