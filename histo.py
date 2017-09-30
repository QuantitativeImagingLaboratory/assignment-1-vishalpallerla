import cv2
import numpy as np
import matplotlib

hist = [0]*256

img = cv2.imread('cells.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
[h, w] = img_gray.shape
i=0
threshold = 0
while i<256:
    for row in range(h-1):
        for col in range(w-1):
            if img_gray[row,col] == i:
                hist[i] += 1
    i+=1
print(hist)

for i in range(255):
    threshold += (i)*(hist[i]/(h*w))


print(threshold)


for row in range(h-1):
    for col in range(w-1):
        if img_gray[row,col] < threshold:
            img_gray[row,col] = 255
        elif img_gray[row,col] > threshold:
            img_gray[row,col] = 0

#cv2.imshow('Image',img_gray)
#cv2.waitKey(0)

R = np.zeros((h,w))
region_counter = 1
for row in range(h-1):
    for col in range(w-1):
        if img_gray[row,col] == 0 and img_gray[row,col - 1] == 255 and img_gray[row - 1,col] == 255:
            R[row,col] = region_counter
            region_counter = region_counter + 1
        if img_gray[row,col] == 0 and img_gray[row,col - 1] == 255 and img_gray[row - 1,col] == 0:
            R[row,col] = R[row - 1,col]
        if img_gray[row,col] == 0 and img_gray[row,col - 1] == 0 and img_gray[row - 1,col] == 255:
            R[row,col] = R[row,col - 1]
        if img_gray[row,col] == 0 and img_gray[row,col - 1] == 0 and img_gray[row - 1,col] == 0:
            R[row,col] = R[row - 1,col]


[v,ind] = max(R.all())
[v1,ind1] = max(max(R.all()))

print(v1)

