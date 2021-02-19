import sys
import tire
import termios
import tty


inkey_buffer = 1


def inkey():
    fd=sys.stdin.fileno()
    remember_attributes=termios.tcgetattr(fd)
    tty.setraw(sys.stdin.fileno())
    character=sys.stdin.read(inkey_buffer)
    termios.tcsetattr(fd,termios.TCSADRAIN, remember_attributes)
    return character


while True:
	key = (inkey())
	while key == "w":
		tire.run()
		if key != "w":
			break
	if key == "a":
		tire.left()
	elif key == "d":
		tire.right()
	elif key == "s":
		tire.back()
	else:
		tire.brake()