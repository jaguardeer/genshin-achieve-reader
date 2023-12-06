import cv2 as cv


class trackbar:
	def __init__(self, name, parent_window, initial_value, max_value, on_change):
		self.name = name
		self.parent_window = parent_window
		cv.createTrackbar(self.name, self.parent_window, initial_value, max_value, on_change)

	def __int__(self):
		return cv.getTrackbarPos(self.name, self.parent_window)


def get_test_img():
	filename = './2023-11-28 06-38-47.mkv'
	cap = cv.VideoCapture(filename)
	if not cap.isOpened():
		print("Cannot open file")
		exit()
	ret, frame = cap.read()
	if not ret:
		print("Can't receive frame (stream end?). Exiting ...")
		exit()
	return frame