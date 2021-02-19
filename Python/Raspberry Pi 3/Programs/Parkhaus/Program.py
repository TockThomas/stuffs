import RPi.GPIO as GPIO
import time
import LED
import Button
import Servo
import datetime

besucher = 0
max_besucher = 1
button = 22
button1 = 18

def uhrzeit():
    now = datetime.datetime.now()
    print(now.strftime('%d.%m.%Y'))
    print(now.strftime('%H:%M:%S'))


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)
GPIO.setup(button1, GPIO.IN)

print(" ")
print(" ")
print(" ")
print("Parkhaus von Thomas")
print(" ")
print("Preis: per 10 Sekunden 1.20$")
print("Maximal: 8.00$")
print(" ")

try:
    while True:
        while besucher < max_besucher:
            time.sleep(0.1)
            LED.green_on()
            LED.red_off()
            if GPIO.input(button) != 0:
                besucher = besucher + 1
                Servo.servo_auf(5)
                Servo.servo_zu()
                startzeit = time.time()
                uhrzeit()
                print("Ein Kunde ist im Parkplatz.")
                print(" ")
            elif GPIO.input(button1) != 0:
                besucher = besucher - 1
                if besucher < 0:
                    besucher = 0
                elif besucher >= 0:
                    Servo.servo1_auf(2)
                    Servo.servo1_zu()
                print(besucher)
        else:
            while besucher == max_besucher:
                LED.green_off()
                LED.red_on()
                time.sleep(0.1)
                if GPIO.input(button1) != 0:
                    besucher = besucher - 1
                    endzeit = time.time()
                    Servo.servo1_auf(5)
                    Servo.servo1_zu()
                    zeit = endzeit - startzeit
                    geld = zeit / 10
                    summe1 = format(geld, '.0f')
                    summe = float(summe1) * 6 / 5
                    if summe >= 8:
                        summe = 8.0
                    uhrzeit()
                    print("Der Kunde war %.1f Sekunden in Parkhaus" % round(zeit, 2))
                    print("und bezahlte %.1f0$." % summe)
                    print(" ")
except KeyboardInterrupt:
    print("Wird beendet...")
    GPIO.cleanup()

#Lichtschranke, Servo niederiger machen