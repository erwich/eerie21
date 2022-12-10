from time import sleep
from sense_hat import SenseHat
sense = SenseHat()

# Constant values for colors
# These are variables that represent color values using (red, green, blue)
GREEN = (50, 164, 49)
YELLOW = (247, 181, 0)
RED = (187, 30, 16)
BLACK = (0, 0, 0)

# Forever loop
while True:
  # Set all lights to Green
  sense.clear(GREEN)
  sleep(2)
  # Show message in black text with green background
  sense.show_message("Go", scroll_speed=.2, text_colour=BLACK, back_colour=GREEN)
  sleep(1)
  sense.clear(YELLOW)
  sleep(2)
  sense.show_message("Slow")
  sleep(1)
  sense.clear(RED)
  sleep(2)
  sense.show_message("Stop")
  sleep(1)
