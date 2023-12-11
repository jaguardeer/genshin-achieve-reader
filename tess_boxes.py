import cv2 as cv
import pytesseract
import numpy as np

test_file = 'artifact-page.png'

img = cv.imread(test_file)


tess_data = pytesseract.image_to_data(img)

header, *data = tess_data.strip().split('\n')

header = header.split('\t')
data = [i.split('\t') for i in data]

objects = [{k: v for k, v in zip(header, item)} for item in data]

def tess2cv_rect(tess_rect):
	# opencv rect: left, top, width, height
	left = int(tess_rect['left'])
	top = int(tess_rect['top'])
	width = int(tess_rect['width'])
	height = int(tess_rect['height'])
	return left, top, width, height

print(header)
for o in objects:
	try:
		print(o['conf'], o['text'])
	except:
		pass
	cv.rectangle(img, tess2cv_rect(o), (0, 255, 0))
cv.imshow('test', img)
cv.waitKey()