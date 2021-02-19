import RPi.GPIO as GPIO
import time
import LED
import Button
import Servo

besucher = 0
max_besucher = 5
button = 22
button1 = 18

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)
GPIO.setup(button1, GPIO.IN)

try:
    while True:
        while besucher < max_besucher:
            time.sleep(0.1)
            LED.green_on()
            LED.red_off()
            if GPIO.input(button) != 0:
                besucher = besucher + 1
                time.sleep(0.5)
                print(besucher)
            elif GPIO.input(button1) != 0:
                besucher = besucher - 1
                if besucher < 0:
                    besucher = 0
                time.sleep(0.5)
                print(besucher)
            else:
                print(besucher)
        else:
            while besucher == max_besucher:
                LED.green_off()
                LED.red_on()
                time.sleep(0.1)
                if GPIO.input(button1) != 0:
                    besucher = besucher - 1
                    time.sleep(0.5)
                print(besucher)
except KeyboardInterrupt:
    print("Wird beendet...")
    GPIO.cleanup()
