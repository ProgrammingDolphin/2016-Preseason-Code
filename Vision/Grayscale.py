import numpy as np
import cv2

# Load a color image in grayscale
img = cv2.imread("/home/and3212/Desktop/Code/FRC/Vision/cat.png",0)

# Displays image
cv2.imshow('image',img) # opens up a window with image
k = cv2.waitKey(5000) #Tells it how many milliseconds to stay open, 0 is infinite, a keystroke also kills it
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('graycat.png', img)
    cv2.destroyAllWindows()