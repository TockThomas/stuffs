import RPi.GPIO as GPIO
import tire
import LED
import ultrasonic
import time

try:
	while True:
		print('Abstand', ultrasonic.distanz())
		if ultrasonic.distanz() > 30:
			LED.blue()
			tire.run()
		else:
			tire.brake()
			while ultrasonic.distanz() < 30:
				LED.red(0.5)
				LED.off(0.5)
				if ultrasonic.distanz() < 30:
					continue
		time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()