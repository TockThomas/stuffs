import RPi.GPIO as GPIO
import curses
import time

#Tire-Pins
IN1 = 20 #Linke Reifenseite nach vorne
IN2 = 21 #Linke Reifenseite nach hinten
IN3 = 19 #Rechte Reifenseite nach vorne
IN4 = 26 #Rechte Reifenseite nach hinten
ENA = 16
ENB = 13

#LED-Pins
LED_R = 22
LED_G = 27
LED_B = 24

#Servo-Pins
servoPIN1 = 23
servoPIN2 = 11
servoPIN3 = 9

#Buzzer-Pin
buzzer = 8

#Fan-Pin
fanPIN = 2

#GPIO-setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(LED_R, GPIO.OUT)
GPIO.setup(LED_G, GPIO.OUT)
GPIO.setup(LED_B, GPIO.OUT)
GPIO.setup(servoPIN1, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)
GPIO.setup(servoPIN3, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(fanPIN, GPIO.OUT)
GPIO.output(ENA, GPIO.HIGH)
GPIO.output(ENB, GPIO.HIGH)
ENA_PWM = GPIO.PWM(ENA, 2000)
ENB_PWM = GPIO.PWM(ENB, 2000)
servo1 = GPIO.PWM(servoPIN1, 50)
servo2 = GPIO.PWM(servoPIN2, 50)
servo3 = GPIO.PWM(servoPIN3, 50)
fan = GPIO.PWM(fanPIN, 50)
ENA_PWM.start(0)
ENB_PWM.start(0)
fan.start(100)

#Tire-Funktionen
def tire_run(speed=20, zeit=0):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(speed)
    ENB_PWM.ChangeDutyCycle(speed)
    time.sleep(zeit)

def tire_runfast(zeit=0):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(100)
    ENB_PWM.ChangeDutyCycle(100)
    time.sleep(zeit)

def tire_back(speed=20, zeit=0):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    ENA_PWM.ChangeDutyCycle(speed)
    ENB_PWM.ChangeDutyCycle(speed)
    time.sleep(zeit)

def tire_run_left(speed=20, zeit=0):
    ENA = 1 * speed / 20
    ENB = 30 * speed / 20
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(ENA)
    ENB_PWM.ChangeDutyCycle(ENB)
    time.sleep(zeit)

def tire_run_right(speed=20, zeit=0):
    ENA = 30 * speed / 20
    ENB = 1 * speed / 20
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(ENA)
    ENB_PWM.ChangeDutyCycle(ENB)
    time.sleep(zeit)

def tire_back_left(speed=20, zeit=0):
    ENA = 1 * speed / 20
    ENB = 30 * speed / 20
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    ENA_PWM.ChangeDutyCycle(ENA)
    ENB_PWM.ChangeDutyCycle(ENB)
    time.sleep(zeit)

def tire_back_right(speed=20, zeit=0):
    ENA = 30 * speed / 20
    ENB = 1 * speed / 20
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    ENA_PWM.ChangeDutyCycle(ENA)
    ENB_PWM.ChangeDutyCycle(ENB)
    time.sleep(zeit)

def tire_left(speed=20, zeit=0):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(speed)
    ENB_PWM.ChangeDutyCycle(speed)
    time.sleep(zeit)

def tire_right(speed=20, zeit=0):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(speed)
    ENB_PWM.ChangeDutyCycle(speed)
    time.sleep(zeit)

def tire_spin_right(zeit=0):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    ENA_PWM.ChangeDutyCycle(20)
    ENB_PWM.ChangeDutyCycle(20)
    time.sleep(zeit)

def tire_spin_left(zeit=0):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(20)
    ENB_PWM.ChangeDutyCycle(20)
    time.sleep(zeit)

def tire_brake(zeit=0):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(20)
    ENB_PWM.ChangeDutyCycle(20)
    time.sleep(zeit)

#LED-Funktionen
def LED_all(zeit=0):
    GPIO.output(LED_R, GPIO.HIGH)
    GPIO.output(LED_G, GPIO.HIGH)
    GPIO.output(LED_B, GPIO.HIGH)
    time.sleep(zeit)

def LED_red(zeit=0):
    GPIO.output(LED_R, GPIO.HIGH)
    GPIO.output(LED_G, GPIO.LOW)
    GPIO.output(LED_B, GPIO.LOW)
    time.sleep(zeit)

def LED_green(zeit=0):
    GPIO.output(LED_R, GPIO.HIGH)
    GPIO.output(LED_G, GPIO.HIGH)
    GPIO.output(LED_B, GPIO.LOW)
    time.sleep(zeit)

def LED_pink(zeit=0):
    GPIO.output(LED_R, GPIO.HIGH)
    GPIO.output(LED_G, GPIO.LOW)
    GPIO.output(LED_B, GPIO.HIGH)
    time.sleep(zeit)

def LED_greenred(zeit=0):
    GPIO.output(LED_R, GPIO.LOW)
    GPIO.output(LED_G, GPIO.HIGH)
    GPIO.output(LED_B, GPIO.LOW)
    time.sleep(zeit)

def LED_turkis(zeit=0):
    GPIO.output(LED_R, GPIO.LOW)
    GPIO.output(LED_G, GPIO.HIGH)
    GPIO.output(LED_B, GPIO.HIGH)
    time.sleep(zeit)

def LED_blue(zeit=0):
    GPIO.output(LED_R, GPIO.LOW)
    GPIO.output(LED_G, GPIO.LOW)
    GPIO.output(LED_B, GPIO.HIGH)
    time.sleep(zeit)

def LED_off(zeit=0):
    GPIO.output(LED_R, GPIO.LOW)
    GPIO.output(LED_G, GPIO.LOW)
    GPIO.output(LED_B, GPIO.LOW)
    time.sleep(zeit)

def LED_redblink(zeit=0):
    GPIO.output(LED_R, GPIO.HIGH)
    GPIO.output(LED_G, GPIO.LOW)
    GPIO.output(LED_B, GPIO.LOW)
    time.sleep(zeit)

#Servo-Funktionen
def servo_default():
    servo1.start(6.5)
    servo2.start(7.5)
    servo3.start(6)
    global x
    global y
    global z
    x = 6.5
    y = 7.5
    z = 6
    time.sleep(0.5)

def servo_move1(move):
    servo1.ChangeDutyCycle(move)
    time.sleep(0.2)

def servo_move2(move):
    servo2.ChangeDutyCycle(move)
    time.sleep(0.2)

def servo_move3(move):
    servo3.ChangeDutyCycle(move)
    time.sleep(0.2)

#Buzzer-Funktionen
def buzzer_on(zeit=0):
	GPIO.output(buzzer, GPIO.LOW)
	time.sleep(zeit)

def buzzer_off(zeit=0):
	GPIO.output(buzzer, GPIO.HIGH)
	time.sleep(zeit)

#Fan-Funktionen
def fan_run():
    fan.ChangeDutyCycle(50)

def fan_run_slow():
    fan.ChangeDutyCycle(70)

def fan_stop():
    fan.ChangeDutyCycle(100)

def sos():
	for i in range(1):
		for i in range(1, 4):
			LED_red()
			buzzer_on()
			time.sleep(0.2)
			LED_off()
			buzzer_off()
			time.sleep(0.2)
		for i in range(1, 4):
			LED_red()
			buzzer_on()
			time.sleep(0.5)
			LED_off()
			buzzer_off()
			time.sleep(0.5)
		for i in range(1, 4):
			LED_red()
			buzzer_on()
			time.sleep(0.2)
			LED_off()
			buzzer_off()
			time.sleep(0.2)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

# controls
# E - LED Blau
# R - LED Rot
# T - LED Gruen
# F - LED on/off
# WASD - Servo-Kamera
# NM - Servo-Ultraschallsensor/LED
# P - Servo default
# O - SOS
# 7 - Fan-stop
# 8 - Fan-run-slow
# 9 - Fan-run

servo_default()
LED_off()
LEDison = False


try:
	while True:
		char = screen.getch()
		if char == curses.KEY_UP:
			tire_run()
		elif char == curses.KEY_LEFT:
			tire_run_left()
		elif char == curses.KEY_RIGHT:
			tire_run_right()
		elif char == curses.KEY_DOWN:
			tire_back()
		elif char == ord("q"):
			tire_brake()
		elif char == ord("e"):
			LED_blue()
		elif char == ord("r"):
			LED_red()
		elif char == ord("t"):
			LED_green()
		elif char == ord("f"):
			if LEDison:
				LED_off()
				LEDison = False
			else:
				LED_all()
				LEDison = True
		elif char == ord("w"):
			x = x + 0.5
			if x > 11:
				x = 11
			print("x is " + str(x))
			servo_move3(x)
		elif char == ord("s"):
			x = x - 0.5
			if x < 4:
				x = 4
			print("x is " + str(x))
			servo_move3(x)
		elif char == ord("a"):
			y = y + 1
			if y > 12.5:
				y = 12.5
			z = z + 1
			if z > 11:
				z = 11
			print("y is " + str(y))
			print("z is " + str(z))
			servo_move2(y)
			servo_move1(z)
		elif char == ord("d"):
			y = y - 1
			if y < 3.5:
				y = 3.5
			z = z - 1
			if z < 2:
				z = 2
			print("y is " + str(y))
			print("z is " + str(z))
			servo_move2(y)
			servo_move1(z)
		elif char == ord("n"):
			z = z + 1
			servo_move1(z)
		elif char == ord("m"):
			z = z - 1
			servo_move1(z)
		elif char == ord("p"):
			servo_default()
		elif char == ord("7"):
			fan_stop()
		elif char == ord("8"):
			fan_run_slow()
		elif char == ord("9"):
			fan_run()
		elif char == ord("o"):
			sos()
		elif char == curses.ENTER:
			tire_brake()

finally:
	curses.nocbreak(); screen.keypad(0); curses.echo()
	curses.endwin()
	servo_default()
	time.sleep(0.2)
	GPIO.cleanup()