# Lines starting with # are comments, not code

# Import packages
from time import sleep
from sense_hat import SenseHat

# Link to the external Sense HAT sensor
sense = SenseHat()

# Show a message
sense.show_message("Hi ERIE21!")
# Pause
sleep(2)
# Show another message with more settings
sense.show_message("Bye ERIE21!", scroll_speed=1, text_colour=(0,0,255), back_colour=(247, 181, 0))
