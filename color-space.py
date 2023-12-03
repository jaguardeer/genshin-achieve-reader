import cv2 as cv
import numpy as np

filename = './2023-11-28 06-38-47.mkv'
cap = cv.VideoCapture(filename)

if not cap.isOpened():
	print("Cannot open file")
	exit()

#grab first frame
ret, frame = cap.read()
if not ret:
	print("Can't receive frame (stream end?). Exiting ...")
	exit()

class trackbar:
	def __init__(self, name, parent_window, initial_value, max_value, on_change):
		self.name = name
		self.parent_window = parent_window
		cv.createTrackbar(self.name, self.parent_window, initial_value, max_value, on_change)

	def __int__(self):
		return cv.getTrackbarPos(self.name, self.parent_window)


def on_trackbar(val):
	hue = int(hue_slider)
	sat = int(sat_slider)
	val = int(val_slider)

	shape = (1080, 1920, 3)
	img = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
	img[:, :, 0] = hue
	img[:, :, 1] = sat
	#img[:, :, 2] = val
	#img = np.full(shape, (hue, sat, val), dtype = np.uint8)
	img = cv.cvtColor(img, cv.COLOR_HSV2BGR)
	cv.imshow(window_name, img)

def on_mouse(event, x, y, flags, param):
	if event != cv.EVENT_LBUTTONDOWN:
		return
	print(f'{x}, {y}:\n'	\
		f'\tBGR: {''.join("%0.2x" % n for n in frame[y, x])}\n'	\
		f'\tHSV: {''.join("%0.2x" % n for n in cv.cvtColor(np.uint8([[frame[y, x]]]), cv.COLOR_BGR2HSV)[0][0])}')

window_name = 'test'
cv.namedWindow(window_name)
hue_slider = 0
sat_slider = 0
val_slider = 0
hue_slider = trackbar('hue', window_name, 0, 179, on_trackbar)
sat_slider = trackbar('sat', window_name, 255, 255, on_trackbar)
val_slider = trackbar('val', window_name, 255, 255, on_trackbar)
cv.setMouseCallback(window_name, on_mouse)
on_trackbar(0)
cv.waitKey()
