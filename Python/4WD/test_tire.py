import RPi.GPIO as GPIO
import tire
import LED
import time



try:
    while True:
        LED.red()
        tire.run(7)
        LED.green()
        tire.run_left(2)
        LED.blue()
        tire.run_right(2)
        LED.turkis()
        tire.run(6.5)
        LED.red()
        tire.spin_left(0.55)
        LED.blue()
        tire.run(8)
        for i in range(5):
            tire.spin_left(1)
            LED.red()
            tire.spin_right(1)
            LED.blue()
        GPIO.cleanup()
except KeyboardInterrupt:
    pass