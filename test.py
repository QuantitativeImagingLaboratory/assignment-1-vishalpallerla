import cv2
import numpy as np
import matplotlib


img = cv2.imread('cell2.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
[h,w] = img_gray.shape
print(h,w)

scale = [1,1]

blank_image = np.zeros((int(scale[0]*h),int(scale[1]*w)))
print(blank_image.shape)
#blank_image[new_w-1,new_h-1] = [255,255,0]

for row in range(int(scale[0]*h)):
    for col in range(int(scale[1]*w)):
        #blank_image[int(col/0.5),int(row/0.5)] = blank_image[col,row]
         new_row = round((row - 1) * (h - 1) / int((scale[0] * h - 1)) + 1)
         new_col = round((col - 1) * (w - 1) / int((scale[1] * w - 1)) + 1)

         blank_image[row,col] = img_gray[new_row-1,new_col-1]

cv2.imshow('Image', blank_image)
cv2.waitKey(0)