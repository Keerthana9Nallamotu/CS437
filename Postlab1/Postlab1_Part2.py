from sense_hat import SenseHat

sense = SenseHat()

sense.clear()  ## to clear the LED matrix

sum = 0
count = 0

while True:
    old_temperature = sense.get_temperature()
    
    sum += old_temperature
    count += 1
    
    new_temperature = sum/count

    print("Old Temp", old_temperature, "Curated Temp", new_temperature)
