import RPi.GPIO as GPIO
import curses
import time
import tire
import LED
import servo
import buzzer
import fan
import ir

def sos():
	for i in range(1):
		for i in range(1, 4):
			LED.red()
			buzzer.on()
			time.sleep(0.2)
			LED.off()
			buzzer.off()
			time.sleep(0.2)
		for i in range(1, 4):
			LED.red()
			buzzer.on()
			time.sleep(0.5)
			LED.off()
			buzzer.off()
			time.sleep(0.5)
		for i in range(1, 4):
			LED.red()
			buzzer.on()
			time.sleep(0.2)
			LED.off()
			buzzer.off()
			time.sleep(0.2)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

# controls
# E - LED Blau
# R - LED Rot
# T - LED Gruen
# F - LED off
# WASD - Servo-Kamera
# NM - Servo-Ultraschallsensor/LED
# P - Servo default
# O - SOS
# 7 - Fan-stop
# 8 - Fan-run-slow
# 9 - Fan-run

servo.default()
x = 6.5
y = 7.5
z = 6

try:
	while True:
		char = screen.getch()
		if char == curses.KEY_UP:
			tire.run()
		elif char == curses.KEY_LEFT:
			tire.run_left()
		elif char == curses.KEY_RIGHT:
			tire.run_right()
		elif char == curses.KEY_DOWN:
			tire.back()
		elif char == ord("q"):
			tire.brake()
		elif char == ord("e"):
			LED.blue()
		elif char == ord("r"):
			LED.red()
		elif char == ord("t"):
			LED.green()
		elif char == ord("f"):
			LED.off()
		elif char == ord("w"):
			x = x + 0.5
			servo.move3(x)
		elif char == ord("s"):
			x = x - 0.5
			servo.move3(x)
		elif char == ord("a"):
			y = y + 1
			z = z + 1
			servo.move2(y)
			servo.move1(z)
		elif char == ord("d"):
			y = y - 1
			z = z - 1
			servo.move2(y)
			servo.move1(z)
		elif char == ord("n"):
			z = z + 1
			servo.move1(z)
		elif char == ord("m"):
			z = z - 1
			servo.move1(z)
		elif char == ord("p"):
			servo.default()
		elif char == ord("7"):
			fan.stop()
		elif char == ord("8"):
			fan.run_slow()
		elif char == ord("9"):
			fan.run()
		elif char == ord("o"):
			sos()
		elif char == curses.ENTER:
			tire.brake()

finally:
	curses.nocbreak(); screen.keypad(0); curses.echo()
	curses.endwin()
	servo.default()
	time.sleep(0.2)
	GPIO.cleanup()