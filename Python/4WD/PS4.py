#for PS4 write in terminal: sudo ds4drv
from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice('/dev/input/event2')

aBtn = 305
bBtn = 306
xBtn = 304
yBtn = 307
PSBtn = 316

l2 = 310
r2 = 311
l1 = 308
r1 = 309

start = 313
select = 312

l3 = 314
r3 = 315

#KEY_ABS

leftjoy = 00
rightjoy = 2,1 #5 hochachse

giro.vh = 8, 7
giro.seitlich = 6 #25, 26, 27

#DPAD
#oben 17 val. -1
#unten 17 val. 1
#links 16 val. -1
#rechts 16 val. 1

rt = 4 #0-255
lt = 3

#prints out device info at start
print(gamepad)

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
    #fiL2ers by event type
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == aBtn:
                print("A")
            elif event.code == bBtn:
                print("B")
            elif event.code == xBtn:
                print("X")
            elif event.code == yBtn:
                print("Y")
            elif event.code == PSBtn:
                print("Home")
            elif event.code == l2:
                print("LT")
            elif event.code == r2:
                print("RT")
            elif event.code == l1:
                print("LB")
            elif event.code == r1:
                print("RB")
            elif event.code == start:
                print("Start")
            elif event.code == select:
                print("Select")
            elif event.code == l3:
                print("L3")
            elif event.code == r3:
                print("R3")