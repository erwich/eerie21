from sense_hat import SenseHat
sense = SenseHat()

while True:
  # Take readings from all three sensors and set variables
  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()

  # Round the values to one decimal place
  t = round(t, 1)
  p = round(p, 1)
  h = round(h, 1)
  
  # Create the message
  # str() converts the reading value to a string (text) so it can be concatenated (added to the text)
  message = "Temp: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)
  
  # Display the scrolling message
  print(message) # The print command prints out to the Terminal window
  sense.show_message(message, scroll_speed=0.05)
