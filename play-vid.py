import numpy as np
import cv2 as cv
cap = cv.VideoCapture('./2023-11-28 06-38-47.mkv')
if not cap.isOpened():
    print("Cannot open file")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    imgray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 225, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    im2 = cv.drawContours(imgray, contours, -1, (0,255,0), 3)
    # Display the resulting frame
    cv.imshow('frame', cv.resize(thresh, None, None, 0.5, 0.5))
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()