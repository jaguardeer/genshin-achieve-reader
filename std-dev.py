import cv2 as cv
import numpy as np

from common import *

"""

# THIS ONE ACTUALLY HIGHLIGHTS TEXT PRETTY WELL
def on_trackbar(val):
	global frame, window_name, kernel_x_slider, kernel_y_slider
	kernel_x = int(kernel_x_slider)
	kernel_y = int(kernel_y_slider)

	img = frame / 255

	ksize = (kernel_x, kernel_y)
	img_mu = cv.blur(img, ksize)
	img2_mu = cv.blur(cv.pow(img, 2), ksize)
	img_sigma = cv.sqrt(img2_mu - cv.pow(img_mu, 2))


	cv.imshow(window_name, img_sigma)

"""

def on_trackbar(val):
	global frame, window_name, kernel_x_slider, kernel_y_slider, sat_thresh_slider, val_thresh_slider
	
	kernel_x = int(kernel_x_slider)
	kernel_y = int(kernel_y_slider)

	img = frame / 255

	ksize = (kernel_x, kernel_y)
	img_blur = cv.blur(img, ksize)
	img_diff = cv.absdiff(img, img_blur)
	
	sat_thresh = int(sat_thresh_slider)
	val_thresh = int(val_thresh_slider)
	img_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
	img_sat = img_hsv[:, :, 1]
	img_val = img_hsv[:, :, 2]
	_, sat_mask = cv.threshold(img_sat, sat_thresh, 255, cv.THRESH_BINARY)
	_, val_mask = cv.threshold(img_val, val_thresh, 255, cv.THRESH_BINARY_INV)
	mask = cv.bitwise_or(sat_mask, val_mask)
	img_final = cv.bitwise_and(frame, frame, mask = mask)
	cv.imshow(window_name, img_final)



frame = get_test_img()

window_name = 'test'
cv.namedWindow(window_name)
kernel_x_slider = trackbar('kernel_x', window_name, 2, 255, on_trackbar)
kernel_y_slider = trackbar('kernel_y', window_name, 2, 255, on_trackbar)
sat_thresh_slider = trackbar('sat_thresh', window_name, 25, 255, on_trackbar)
val_thresh_slider = trackbar('val_thresh', window_name, 25, 255, on_trackbar)

on_trackbar(0)

#cv.imshow(window_name, img)
cv.waitKey()
