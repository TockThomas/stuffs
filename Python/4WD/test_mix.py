import RPi.GPIO as GPIO
import tire
import LED
import ultrasonic
import time

try:
	LED.blue()
	tire.run(7)
	LED.turkis()
	tire.run_left(2)
	tire.run_right(2)
	LED.blue()
	tire.run(6.5)
	LED.turkis()
	tire.spin_left(0.55)
	LED.blue()
	tire.run(5.6)
	LED.turkis()
	tire.spin_left(0.7)
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