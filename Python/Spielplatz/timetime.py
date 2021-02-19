import time

x = 1

while x <= 5:
    start = time.time()
    while x <= 5:
        x = x + 1
        time.sleep(1)

stop = time.time()

Zeitdifferenz = stop - start

print(Zeitdifferenz)

