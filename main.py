import cv2 as cv
import numpy as np

dog = "assets/dog.jpeg"


img = cv.imread(dog)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2RGB)

x=50
y=50
trans_mat = np.float32([[1,0,x], [0,1,y]])
dimensions = (img.shape[1], img.shape[0])
shifted_img = cv.warpAffine(img, trans_mat, dimensions)

(height, width) = img.shape[:2]
rotPoint = (width//2, height//2)
rot_mat = cv.getRotationMatrix2D(rotPoint, angle= 45, scale = 1)
dimensions_2 = (width, height)
rotate_img = cv.warpAffine(img,rot_mat, dimensions)

kernel_size = (20, 20)
blur_img = cv.blur(img, kernel_size)


cv.imshow('doggy', blur_img)
cv.waitKey(0)

