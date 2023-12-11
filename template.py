from common import *
import cv2 as cv
import numpy as np
from glob import glob


img = cv.imread('./artifact-page.png')

templates = [cv.imread(f) for f in glob('./templates/*.png')]

threshold_max = 1000

def on_trackbar(val):
	img_copy = img.copy()

	threshold = val / threshold_max

	for template in templates:
		matches = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
		locs = np.where(matches > threshold)
		h, w, _ = template.shape

		for pt in zip(*locs[::-1]):
			cv.rectangle(img_copy, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)

	cv.imshow(win, img_copy)

win = 'window'
cv.namedWindow(win)
cv.createTrackbar('threshold', win, threshold_max, threshold_max, on_trackbar)
on_trackbar(threshold_max)

cv.waitKey()
