import cv2
import numpy as np

img = cv2.imread('img.png' )

# h = img.shape[0]
# w = img.shape[1]
#
# for i in range(h):
#    for a in range(w):
#        for b in range(3):
#            img[i][a][b] += np.uint8(127)


h = img.shape[0]
w = img.shape[1]

z = np.zeros((h,w,3) , dtype='uint8' )
z[...] = np.uint8(100) #меняем 100 для регулировки

result = cv2.add( img , z) #меняем add на sabtract чтобы #затемнять

cv2.imshow( 'zzz', result)
cv2.waitKey(0)