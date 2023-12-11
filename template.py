from common import *
import cv2 as cv
import numpy as np


img = cv.imread('./artifact-page.png')
template = cv.imread('./template.png')
h, w, _ = template.shape

threshold_max = 1000

def on_trackbar(val):
	img_copy = img.copy()

	threshold = val / threshold_max


	matches = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
	locs = np.where(matches > threshold)

	max_rects = 300
	i = 0
	for pt in zip(*locs[::-1]):
		i = i + 1
		#if i > max_rects:
		#	break
		cv.rectangle(img_copy, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)

	cv.imshow(win, img_copy)

win = 'window'
cv.namedWindow(win)
cv.createTrackbar('threshold', win, threshold_max, threshold_max, on_trackbar)
on_trackbar(threshold_max)

cv.waitKey()
