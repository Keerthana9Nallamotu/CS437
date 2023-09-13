from sense_hat import SenseHat
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import CircularOutput
from libcamera import controls
import cv2
import datetime
import os
import numpy as np
import time

sense = SenseHat()

sense.clear()  ## to clear the LED matrix

orig_temp = sense.get_temperature()

while True:
    temperature = sense.get_temperature()
    
    print(temperature-orig_temp)
    
    if abs(temperature-orig_temp)>=1:
        break
    
picam2=Picamera2()
        
dispW=1280
dispH=720
        
picam2.preview_configuration.main.size= (dispW,dispH)
        
picam2.preview_configuration.main.format= "RGB888"
picam2.preview_configuration.align() ## aligns the size to the closest standard format
picam2.preview_configuration.controls.FrameRate=30
        
picam2.configure("preview")
        
picam2.start()

faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        
while True:
    
    frame=picam2.capture_array()
    
    frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(frameGray,1.3,5)
    
    print(faces)
    
    for face in faces:
        x,y,w,h=face
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0),3)
        
    time.sleep(0.5)
    cv2.imshow("Camera Frame", frame)
    key=cv2.waitKey(1) & 0xFF    
    
    if key ==ord(" "):
        cv2.imwrite("frame-" + str(time.strftime("%H:%M:%S", time.localtime())) + ".jpg", frame)
    if key == ord("q"): ## stops for 1 ms to check if key Q is pressed
        break
    
cv2.destroyAllWindows()
