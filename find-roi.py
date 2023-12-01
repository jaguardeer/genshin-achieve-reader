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

gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

window_title = 'gray'
bin_trackbar = 'bin_thresh'
cnt_trackbar = 'cnt_thresh'
bin_trackbar_max = 255
cnt_trackbar_max = 1000

# 127 / 255

def is_rectangular(contour, thresh):
	cnt_area = cv.contourArea(contour)
	_, _, w, h = cv.boundingRect(contour)
	box_area = w * h
	ratio_diff = cnt_area / box_area
	return thresh < ratio_diff

def on_trackbar(val):
	# apply thresholding
	bin_thresh = cv.getTrackbarPos(bin_trackbar, window_title)
	_, img_thresh = cv.threshold(gray, bin_thresh, bin_trackbar_max, cv.THRESH_BINARY)
	# find contours
	contours, hier = cv.findContours(img_thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

	# apply rectangleness cutoff
	cnt_thresh = cv.getTrackbarPos(cnt_trackbar, window_title) / cnt_trackbar_max
	new_contours = [c for c in contours if is_rectangular(c, cnt_thresh)]

	# draw contours
	new_frame = frame.copy()
	cv.drawContours(new_frame, new_contours, -1, (0,255,0), 1)
	new_frame = cv.resize(new_frame, dsize=(1280,720))
	cv.imshow(window_title, new_frame)
	#plt.show()


#bin2_trackbar = 'bin2'
#def on_trackbar_bin(val):
	#bin_thresh = cv.getTrackbarPos(bin2_trackbar, window_title)
	#_, img_thresh = cv.threshold(gray, bin_thresh, bin_trackbar_max, cv.THRESH_BINARY)
	#cv.imshow(window_title, cv.resize(img_thresh, dsize=(1280,720)))
#cv.namedWindow(window_title)
#cv.createTrackbar(bin2_trackbar, window_title, 0, 255, on_trackbar_bin)
#on_trackbar_bin(0)
#cv.waitKey()

cv.namedWindow(window_title)
cv.createTrackbar(bin_trackbar, window_title, 225, bin_trackbar_max, on_trackbar)
cv.createTrackbar(cnt_trackbar, window_title, 0, cnt_trackbar_max, on_trackbar)
on_trackbar(0)
cv.waitKey()

cap.release()
cv.destroyAllWindows()