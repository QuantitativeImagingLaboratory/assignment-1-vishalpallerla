

import numpy as np
#import dip_hw1_region_analysis as dip

class binary_image:

    def compute_histogram(self, image):
        """Computes the histogram of the input image
        takes as input:
        image: a grey scale image
        returns a histogram"""
        hist = [0] * 256
        [h, w] = image.shape
        print(h,w)
        i = 0
        while i < 256:
            for row in range(h):
                for col in range(w):
                    if image[row, col] == i:
                        hist[i] += 1
            #print(hist[i])
            i += 1

        return hist

    def find_optimal_threshold(self, hist):
        """analyses a histogram it to find the optimal threshold value assuming a bimodal histogram
        takes as input
        hist: a bimodal histogram
        returns: an optimal threshold value"""

        threshold = 0
        tot_int = 0
        for c in range(256):
            tot_int += hist[c]
        print(tot_int)
        for i in range(256):
            threshold += (i) * (hist[i] / tot_int)

        return threshold

    def binarize(self, image, threshold):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()
        [h, w] = bin_img.shape
        #opt_threshold = dip.main().threshold
        #print("Threshold in bin",opt_threshold)
        opt_threshold = threshold
        print(opt_threshold)
        for row in range(h):
            for col in range(w):
                if bin_img[row, col] < opt_threshold:
                    bin_img[row, col] = 255
                elif bin_img[row, col] > opt_threshold:
                    bin_img[row, col] = 0

        return bin_img


