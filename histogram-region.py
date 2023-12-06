import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

from common import *


frame = get_test_img()

#window_name = 'test'
#cv.namedWindow(window_name)

gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

while True:
	roi_rect = cv.selectROI("selection", gray)

	print(roi_rect)

	roi = gray[roi_rect[1]:roi_rect[1]+roi_rect[3], roi_rect[0]:roi_rect[0]+roi_rect[2]]

	cv.imshow("roi", roi)

	plt.hist(roi.ravel(),256,[0,256])
	plt.show()