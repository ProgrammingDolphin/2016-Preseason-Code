import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Captures each frame
    ret, frame = cap.read()# Change size by doing
    #ret = cap.set(3,000) & ret = cap.set(4,000)

    # Operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Displays final frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1)& 0xFF == ord('q'): #Hit 'q' to quit
        break

# When everything is finished release the capture
cap.release()
cv2.destroyAllWindows()
