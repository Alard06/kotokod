import cv2
import numpy as np

img = cv2.imread('img_1.png' )

h = img.shape[0]
w = img.shape[1]

for i in range(h):
   for a in range(w):
       for b in range(3):
           img[i][a][b] += np.uint8(10)

cv2.imshow( 'zzz', img)
cv2.waitKey(0)