import cv2 as cv

def vid_to_frames(filename, out_dir):
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
		else:
			out_file = f'./{out_dir}/{i}.png'
			#print(f'Writing to {out_file}')
			cv.imwrite(out_file, frame)
			i = i + 1



filename = 'C:/Users/paco/OneDrive/OneDrive - g.austincc.edu/testvid/lossless.avi'
out_dir = 'frames'

vid_to_frames(filename, out_dir)