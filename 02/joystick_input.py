from time import sleep
from sense_hat import SenseHat, ACTION_RELEASED

from signal import pause

sense = SenseHat()

# Constant values for colors
# These are variables that represent color values using (red, green, blue)
GREEN = (50, 164, 49)
YELLOW = (247, 181, 0)
RED = (187, 30, 16)
BLACK = (0, 0, 0)

def change_to_green(event):
    if event.action != ACTION_RELEASED:
        sense.clear(GREEN)

def change_to_red(event):
    if event.action != ACTION_RELEASED:
        sense.clear(YELLOW)
        sleep(3)
        sense.clear(RED)

sense.stick.direction_up = change_to_red
sense.stick.direction_down = change_to_green

pause()
