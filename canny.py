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

#frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

window_title = 'gray'
threshold1_trackbar = 'threshold1'
threshold2_trackbar = 'threshold2'
aperture_trackbar = 'aperture'
rect_ratio_trackbar = 'ratio'
threshold1_trackbar_max = 255
threshold2_trackbar_max = 255
aperture_trackbar_max = 255
rect_ratio_trackbar_max = 1000

kernelX_trackbar = 'kernelX'
kernelY_trackbar = 'kernelY'

#frame = 

def is_rectangular(contour, thresh):
	cnt_area = cv.contourArea(contour)
	_, _, w, h = cv.boundingRect(contour)
	box_area = w * h
	ratio_diff = cnt_area / box_area
	return thresh < ratio_diff

def on_trackbar(val):
	threshold1 = cv.getTrackbarPos(threshold1_trackbar, window_title)
	threshold2 = cv.getTrackbarPos(threshold2_trackbar, window_title)
	aperture = cv.getTrackbarPos(aperture_trackbar, window_title)
	rect_ratio = cv.getTrackbarPos(rect_ratio_trackbar, window_title) / rect_ratio_trackbar_max

	img = frame

	img = cv.Canny(frame, threshold1, threshold2)

	kernelX = cv.getTrackbarPos(kernelX_trackbar, window_title)
	kernelY = cv.getTrackbarPos(kernelY_trackbar, window_title)
	kernel = cv.getStructuringElement(cv.MORPH_CROSS, (kernelX, kernelY))
	img = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

	contours, hier = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	contours = [c for c in contours if is_rectangular(c, rect_ratio)]
	img = cv.cvtColor(img, cv.COLOR_GRAY2RGB)
	cv.drawContours(img, contours, -1, (0,255,0), 1)

	#img = cv.resize(img, dsize = (1024, 576))
	cv.imshow(window_title, img)



cv.namedWindow(window_title)
cv.createTrackbar(threshold1_trackbar, window_title, 0, threshold1_trackbar_max, on_trackbar)
cv.createTrackbar(threshold2_trackbar, window_title, 0, threshold2_trackbar_max, on_trackbar)
cv.createTrackbar(aperture_trackbar, window_title, 3, aperture_trackbar_max, on_trackbar)
cv.createTrackbar(rect_ratio_trackbar, window_title, 0, rect_ratio_trackbar_max, on_trackbar)
cv.createTrackbar(kernelX_trackbar, window_title, 1, 255, on_trackbar)
cv.createTrackbar(kernelY_trackbar, window_title, 1, 255, on_trackbar)

on_trackbar(0)
cv.waitKey()

cap.release()
cv.destroyAllWindows()