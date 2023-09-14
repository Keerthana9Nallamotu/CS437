from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
yellow = (255,255,0)

x_val = 3
y_val = 5
sense.clear()
sense.set_pixel(x_val,y_val, yellow)

while True:
    for event in sense.stick.get_events():
        print(event.direction, event.action)
        
        if event.action == "pressed":
            sense.clear()
            if event.direction == "up":
                y_val-=1
                
            elif event.direction == "down":
                y_val+=1
                
            elif event.direction == "right":
                x_val+=1
                
            elif event.direction == "left":
                x_val-=1
                
            elif event.direction == "middle":
                sense.clear()
                exit()
                
            sense.set_pixel(x_val,y_val, yellow)
                
            