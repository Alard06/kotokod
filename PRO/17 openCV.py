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

# z = np.zeros((h,w,3) , dtype='uint8' )
# z[...] = np.uint8(100) #меняем 100 для регулировки
#
# result = cv2.add( img , z) #меняем add на sabtract чтобы #затемнять

cv2.line(img, (10,10), (150, 200), (0, 0, 255), thickness=10)
cv2.circle(img, (w//2, h//2), 100, (0, 255, 0), thickness=cv2.FILLED)  # cv2.FILLED / number
cv2.rectangle(img, (100, 100), (300, 250), (0, 0, 255), thickness=cv2.FILLED)
cv2.putText(img, 'OpenCV', (100, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


cv2.imshow( 'zzz', img)
cv2.waitKey(0)