
import sys
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

while 1:
    key = (inkey())
    if key in ['w','a','s','d']:
        print (key)
    if key == 'q':
        exit()