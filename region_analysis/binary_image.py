

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


        threshold = int((len(hist)-1)/2)
        ct = len(hist) - 1

        while True:
            if(ct < 1):
                break
            threshold1 = self.evalue(hist,0,threshold)
            threshold2 = self.evalue(hist,threshold,len(hist) - 2)
            nt = int((threshold1+threshold2)/2)
            ct = nt - threshold
            threshold = nt

        return threshold

    def evalue(self,hist,lval,rval):
        tot_int = 0
        final_int = 0
        for row in range(lval,rval):
            tot_int += hist[row]
        for col in range(lval,rval):
            final_int += col*(hist[col]/tot_int)
        return final_int


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


                    #reverse the cases

        return bin_img



