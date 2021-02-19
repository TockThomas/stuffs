from evdev import InputDevice, categorize, ecodes

gamepad = InputDevice("/dev/input/event2")

print(gamepad)

for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        print(event)