from threading import Timer
import random

from sense_hat import SenseHat, ACTION_RELEASED
from time import sleep
sense = SenseHat()

# Define some colours
g = (0, 255, 0) # Green
b = (0, 0, 0) # Black

RED = (187, 30, 16)
YELLOW = (247, 181, 0)

# game variables
creeper_around = False
creeper_timer = False
points = 0

# Set up where each colour will display
creeper_pixels = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, b, b, g, g, b, b, g,
    g, b, b, g, g, b, b, g,
    g, g, g, b, b, g, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, g, g, b, g, g
]

def explode_creeper():
    if creeper_around:
        sense.clear(RED)
        sleep(5)
        sense.show_message("GAME OVER")
        sleep(5)
        sense.show_message("Total pts: " + points)

def punch_creeper(event):
    if event.action != ACTION_RELEASED:
        if creeper_around:
            sense.clear(YELLOW)
            points += 1
            creeper_timer.cancel()

def spawn_creeper():
    global creeper_around, creeper_timer
    # Display these colours on the LED matrix
    sense.set_pixels(creeper_pixels)
    creeper_around = True
    creeper_timer = Timer(5, explode_creeper)
    

while True:
    sleep(random.randint(5, 15))
    spawn_creeper()