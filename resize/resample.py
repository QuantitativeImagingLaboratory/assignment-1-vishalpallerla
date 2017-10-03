import cv2
import numpy as np
class resample:

    def resize(self, image, fx = None, fy = None, interpolation = None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """

        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, fx, fy)

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, fx, fy)

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        #Write your code for nearest neighbor interpolation here
        [h, w] = image.shape
        #print(h, w)

        x = float(fx)
        h_rs = int(x * h)

        y = float(fy)
        w_rs = int(y * w)

        blank_image = np.zeros((h_rs, w_rs))
        #print(blank_image.shape)

        for row in range(h_rs):
            for col in range(w_rs):
                # blank_image[int(col/0.5),int(row/0.5)] = blank_image[col,row]
                new_row = round((row - 1) * (h - 1) / h_rs)
                new_col = round((col - 1) * (w - 1) / w_rs)

                blank_image[row, col] = image[new_row - 1, new_col - 1]

        return blank_image


    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bilinear interpolation method
        """

        # Write your code for bilinear interpolation here


        return image

