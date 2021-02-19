from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice("/dev/input/event2")

print(gamepad)

#EV_KEY

aBtn = 304
bBtn = 305
xBtn = 307
yBtn = 308

LB = 310
RB = 311
L3 = 317
R3 = 318

start = 315
back = 314
guide = 316

#EV_ABS

LT = 2 #val.:0-255
RT = 5 #val.:0-255

UP = 17 #val.:-1
DOWN = 17 #val.:1
LEFT = 16 #val.:-1
RIGHT = 16 #val.:1

left_y_stick = 1 #val.:-32768-32767 (von oben nach unten)
left_x_stick = 0 #val.:-32768-32767 (von links nach rechts)
right_y_stick = 4 #val.:-32768-32767 (von oben nach unten)
right_x_stick = 3 #val.: -32768-32767 (von links nach rechts)

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            if event.code == aBtn:
                print("A")
            if event.code == bBtn:
                print("B")
            if event.code == xBtn:
                print("X")
            if event.code == yBtn:
                print("Y")