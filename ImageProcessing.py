# Python OpenCV ver 4 - HAVE FUN

import numpy as np
import matplotlib
import cv2
import time

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    #print(check)
    #print(frame)

    cv2.imshow("Capture", frame)
    #cv2.waitKey(0)
    key = cv2.waitKey(1)

    if key == ord('q'):
        time2 = time.time()
        break

video.release()
cv2.destroyAllWindows()

