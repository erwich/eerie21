from time import sleep
from sense_hat import SenseHat

# Link to the external Sense HAT sensor
sense = Sensehat()

# Constant values for colors
TRAFFIC_LIGHT_GREEN = [50, 164, 49]
TRAFFIC_LIGHT_YELLOW = [247, 181, 0]
TRAFFIC_LIGHT_RED = [187, 30, 16]

def set_light_color(color):
    sense.set_pixels( [color] * 64 )
    # print([color] * 64)

def main():
    while True:
        set_light_color(TRAFFIC_LIGHT_GREEN)
        sleep(10)
        set_light_color(TRAFFIC_LIGHT_YELLOW)
        sleep(3)
        set_light_color(TRAFFIC_LIGHT_RED)
        sleep(10)


if __name__ == '__main__':
    main()