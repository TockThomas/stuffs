import RPi.GPIO as GPIO
import time
import tire
import LED
import ultrasonic

try:
    while True:
        print("Abstand", ultrasonic.distanz())
        if ultrasonic.distanz() > 30:
            LED.blue()
            tire.run()
        else: 
            tire.brake()
            LED.red()
        time.sleep(0.5)
except KeyboardInterrupt:
    LED.off()
    GPIO.cleanup()
