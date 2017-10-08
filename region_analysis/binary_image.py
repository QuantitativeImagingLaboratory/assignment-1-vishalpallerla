

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

        threshold = int(len(hist)/2)
        tot_int = 0
        threshold1  = 0
        threshold2 = 0
        for c in range(256):
            tot_int += hist[c]
        print(tot_int)
        # for i in range(256):
        #     if i < threshold:
        #         threshold1 += (i) * (hist[i] / tot_int)
        #     elif i >= threshold:
        #         threshold2 += (i) *  (hist[i] / tot_int)
        # threshold = (threshold1 + threshold2)/2

        while True:
            for i in range(256):
                if i < threshold:
                    threshold1 += (i) * (hist[i] / tot_int)
                elif i >= threshold:
                    threshold2 += (i) * (hist[i] / tot_int)
                threshold = (threshold1 + threshold2) / 2
            if threshold - threshold1 != 0 and threshold2 - threshold != 0:
                break
        return threshold





    def binarize(self, image, threshold):
        """Comptues the binary image of the the input image based on histogram analysis and thresholding
        take as input
        image: an grey scale image
        returns: a binary image"""

        bin_img = image.copy()
        [h, w] = bin_img.shape
        opt_threshold = threshold
        print(opt_threshold)
        for row in range(h):
            for col in range(w):
                if bin_img[row, col] > opt_threshold: #greater than threshld white(general)
                    bin_img[row, col] = 255 #0 instead of 1
                else: #less than threshold black(general)
                    bin_img[row, col] = 0 #0 instead of 1

        print(bin_img)
        return bin_img



