import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from common import *


frame = get_test_img()

frame = cv.imread('./frames/4612.png')

roi = select_roi(frame)

fig = plt.figure()
ax = fig.add_subplot(projection = '3d')

print(roi[0, 0])
points = roi.ravel()

hues = roi[:, :, 0].ravel()
sats = roi[:, :, 1].ravel()
vals = roi[:, :, 2].ravel()

print(f'Plotting {len(points)} points.')
print(f'There are {len(np.unique(hues))} unique Hue values')
print(f'There are {len(np.unique(sats))} unique Sat values')
print(f'There are {len(np.unique(vals))} unique Val values')

ax.scatter(hues, sats, vals)
ax.set_xlabel('Hue')
ax.set_ylabel('Sat')
ax.set_zlabel('Val')

plt.show()