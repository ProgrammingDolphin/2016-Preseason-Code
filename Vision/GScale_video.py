import numpy as np
import cv2

cap = cv2.VideoCapture('/home/and3212/Desktop/Code/FRC/Vision/hungry_cat.MOV')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    if cv2.waitKey(25) & 0xFF == ord('q'): # Waitkey is the speed of it, 'q' is quit
    
        break

cap.release()
cv2.destroyAllWindows()
