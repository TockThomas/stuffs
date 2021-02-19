#for PS4 write in terminal: sudo ds4drv
#import evdev
from evdev import InputDevice, categorize, ecodes

#creates object 'gamepad' to store the data
#you can call it whatever you like
gamepad = InputDevice('/dev/input/event2')

#button code variables
aBtn = 305
bBtn = 306
xBtn = 304
yBtn = 307
PSBtn = 316

LT = 310
RT = 311
LB = 308
RB = 309

start = 313
select = 312

L3 = 314
R3 = 315

abb = ["0", "2", "6", "7", "8", "25", "26"]

#prints out device info at start
print(gamepad)

#evdev takes care of polling the controller in a loop
for event in gamepad.read_loop():
    #filters by event type
    if event.type == ecodes.EV_ABS:
        if event.code != 0:
            if event.code != 1:
                if event.code != 6:
                    if event.code != 7:
                        if event.code != 8:
                            if event.code != 25:
                                if event.code != 26:
                                    if event.code != 27:
                                        if event.code!= 2:
                                           print(event)     
                                                    
            
