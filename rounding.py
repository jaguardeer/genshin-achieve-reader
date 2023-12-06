import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture('./2023-11-28 06-38-47.mkv')

if not cap.isOpened():
	print("Cannot open file")
	exit()

#grab first frame
ret, frame = cap.read()
if not ret:
	print("Can't receive frame (stream end?). Exiting ...")

window_title = 'test'
num_buckets_trackbar = 'num_buckets'
print(frame.dtype)

def on_trackbar(val):
	num_buckets = cv.getTrackbarPos(num_buckets_trackbar, window_title)

	img = (frame // num_buckets) * num_buckets

	cv.imshow(window_title, img)



cv.namedWindow(window_title)
cv.createTrackbar(num_buckets_trackbar, window_title, 1, 255, on_trackbar)

on_trackbar(1)
cv.waitKey()

cap.release()
cv.destroyAllWindows()