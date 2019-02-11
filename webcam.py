import cv2
import numpy as np
import os
import time
import random

#Replace this with your opencv directory for the cascades and stuff
face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.4.0/data/haarcascades/haarcascade_frontalface_default.xml')

#Initializes the webcam capture
cap = cv2.VideoCapture(0)

#All of the things this motherfucker can say (You can add more if youd like)
texts = ["Hi", "Notice me", "lalalala", "Hello"]

#Infinite loop because I hate myself
while True:
    #Get what the Camera can see
    ret, img = cap.read()

    #Make it grey because reasons
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Gets the faces in the thingy
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    #Checks to see if there's any faces
    if len(faces) > 0:
	    #Uses the tts script and chooses some random word to say to annoy you
	    os.system("./tts \'" + texts[random.randint(1, len(texts) - 1)] + "\'")

    #Prints out how many faces it sees (You can get rid of this if you want to)
    print(len(faces))

    #Sleeps for a second so it doesnt destroy the CPU
    time.sleep(1)

#And this is just cleanup stuff
cap.release()
cv2.destroyAllWindows()
