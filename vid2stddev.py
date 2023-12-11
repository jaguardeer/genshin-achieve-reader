import cv2 as cv



def process_frame(frame):
	kernel_x = 2
	kernel_y = 2

	img = frame / 255

	ksize = (kernel_x, kernel_y)
	img_mu = cv.blur(img, ksize)
	img2_mu = cv.blur(cv.pow(img, 2), ksize)
	img_sigma = cv.sqrt(img2_mu - cv.pow(img_mu, 2))

	return img_sigma


filename = './2023-12-05 19-15-24.mkv'
cap = cv.VideoCapture(filename)
if not cap.isOpened():
	print("Cannot open file")
	exit()

i = 0
while True:
	ret, frame = cap.read()
	if not ret:
		print("Can't receive frame (stream end?). Exiting ...")
		exit()

	img = process_frame(frame)
	cv.imwrite(f'./frames/{i}.png', img * 255)
	#cv.imshow('test', img)
	#cv.waitKey(1)

	i = i + 1