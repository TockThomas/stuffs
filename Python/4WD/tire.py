import RPi.GPIO as GPIO
import time

IN1 = 20 #Linke Reifenseite nach vorne
IN2 = 21 #Linke Reifenseite nach hinten
IN3 = 19 #Rechte Reifenseite nach vorne
IN4 = 26 #Rechte Reifenseite nach hinten
ENA = 16
ENB = 13

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.output(ENA, GPIO.HIGH)
GPIO.output(ENB, GPIO.HIGH)
ENA_PWM = GPIO.PWM(ENA, 2000)
ENB_PWM = GPIO.PWM(ENB, 2000)
ENA_PWM.start(0)
ENB_PWM.start(0)

def run(speed=20, zeit=0):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(speed)
    ENB_PWM.ChangeDutyCycle(speed)
    time.sleep(zeit)

def runfast(zeit=0):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(100)
    ENB_PWM.ChangeDutyCycle(100)
    time.sleep(zeit)

def back(speed=20, zeit=0):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    ENA_PWM.ChangeDutyCycle(speed)
    ENB_PWM.ChangeDutyCycle(speed)
    time.sleep(zeit)

def run_left(speed=20, zeit=0):
    ENA = 1 * speed / 20
    ENB = 30 * speed / 20
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(ENA)
    ENB_PWM.ChangeDutyCycle(ENB)
    time.sleep(zeit)

def run_right(speed=20, zeit=0):
    ENA = 30 * speed / 20
    ENB = 1 * speed / 20
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(ENA)
    ENB_PWM.ChangeDutyCycle(ENB)
    time.sleep(zeit)

def back_left(speed=20, zeit=0):
    ENA = 1 * speed / 20
    ENB = 30 * speed / 20
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    ENA_PWM.ChangeDutyCycle(ENA)
    ENB_PWM.ChangeDutyCycle(ENB)
    time.sleep(zeit)

def back_right(speed=20, zeit=0):
    ENA = 30 * speed / 20
    ENB = 1 * speed / 20
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    ENA_PWM.ChangeDutyCycle(ENA)
    ENB_PWM.ChangeDutyCycle(ENB)
    time.sleep(zeit)

def left(speed=20, zeit=0):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(speed)
    ENB_PWM.ChangeDutyCycle(speed)
    time.sleep(zeit)

def right(speed=20, zeit=0):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(speed)
    ENB_PWM.ChangeDutyCycle(speed)
    time.sleep(zeit)

def spin_right(zeit=0):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    ENA_PWM.ChangeDutyCycle(20)
    ENB_PWM.ChangeDutyCycle(20)
    time.sleep(zeit)

def spin_left(zeit=0):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(20)
    ENB_PWM.ChangeDutyCycle(20)
    time.sleep(zeit)

def brake(zeit=0):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)
    ENA_PWM.ChangeDutyCycle(20)
    ENB_PWM.ChangeDutyCycle(20)
    time.sleep(zeit)


