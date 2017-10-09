import numpy as np
import cv2
class cell_counting:

    def blob_coloring(self, image):
        """Uses the blob coloring algorithm based on 8 pixel window assign region names
        takes a input:
        image: binary image
        return: a list of regions"""

        [h,w] = image.shape

        regions = dict()
        R = np.zeros((h, w))
        #I = image.copy()
        region_counter = 1
        for row in range(h):
            for col in range(w):
                if row != 0 and col != 0:
                    if image[row, col] == 255 and image[row, col - 1] == 0 and image[row-1, col] == 0:
                        R[row, col] = region_counter
                        region_counter = region_counter + 1
                    if image[row, col] == 255 and image[row, col - 1] == 0 and image[row-1, col] == 255:
                        R[row, col] = R[row-1, col]
                    if image[row, col] == 255 and image[row, col - 1] == 255 and image[row-1, col] == 0:
                        R[row, col] = R[row, col - 1]
                    if image[row, col] == 255 and image[row, col - 1] == 255 and image[row-1, col] == 255:
                        R[row, col] = R[row-1, col]
                        if R[row, col - 1] != R[row-1, col]:
                            R[row, col - 1] = R[row-1, col]
        for i in range(0, h):
            for j in range(0, w):
                if R[i, j] in regions.keys():
                    regions[R[i, j]].append([i, j])
                else:
                    regions[int(R[i, j])] = [[i, j]]

        print(regions)

        return regions




    def compute_statistics(self, region):
    #     """Compute cell statistics area and location
    #     takes as input
    #     region: a list of pixels in a region
    #     returns: area"""

        reg_copy = dict()
        count = 1

        for key, value in region.items():
            x = 0
            y = 0

            for i in range(0, len(value)):
                x = x + value[i][0]
                y = y + value[i][1]
            x = round(x / len(value))
            y = round(y / len(value))
            centroid = [x, y]
            if (len(value) >= 15):
                reg_copy[count] = [centroid, len(value)]
                count = count + 1

        print(len(reg_copy))
        print(reg_copy)
        # Please print your region statistics to stdout
        # <region number>: <location or center>, <area>
        # print(stats)

        return reg_copy





    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""
        for key, value in stats.items():
            msg = "*" +str(key)+ ","+str(value[1])
            pixel = (value[0][1], value[0][0])
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(image, msg, pixel, font, 0.2, (255, 255, 255), 1, cv2.LINE_AA)

        return image


