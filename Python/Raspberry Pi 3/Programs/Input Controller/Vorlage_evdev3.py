#import evdev
from evdev import InputDevice, categorize, ecodes as e, UInput
ui = UInput()
ui.write(e.EV_KEY, e.KEY_A, 1)
ui.write(e.EV_KEY, e.KEY_A, 0)
ui.syn()
 
