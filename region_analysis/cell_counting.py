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
                if image[row, col] == 0 and image[row, col - 1] == 255 and image[row - 1, col] == 255:
                    R[row, col] = region_counter
                    region_counter = region_counter + 1
                if image[row, col] == 0 and image[row, col - 1] == 255 and image[row - 1, col] == 0:
                    R[row, col] = R[row - 1, col]
                if image[row, col] == 0 and image[row, col - 1] == 0 and image[row - 1, col] == 255:
                    R[row, col] = R[row, col - 1]
                if image[row, col] == 0 and image[row, col - 1] == 0 and image[row - 1, col] == 0:
                    t = R[row, col]
                    R[row, col] = R[row - 1, col]
                    if R[row, col - 1] != R[row - 1, col]:
                        R[row, col - 1] = R[row - 1, col]
                        #if image[row, col -1] == image[row -1, col]:
                    #R[row, col] = region_counter
                    #R[row, col] = region_counter
        print(region_counter)
        for obj in range(1,region_counter):
            regions[obj] = []
            #if len(R[obj])>15:
            for row in range(h):
                for col in range(w):
                    if R[row,col] == obj:
                        regions[obj].append((row,col))
                        # if not obj in regions:
                        #     regions[obj] = [(row, col)]
                        # else:
                        #     regions[obj].append((row, col))
        print(regions)
        return regions




    def compute_statistics(self, region):
    #     """Compute cell statistics area and location
    #     takes as input
    #     region: a list of pixels in a region
    #     returns: area"""
    #
    #
    #
    #     # Please print your region statistics to stdout
    #     # <region number>: <location or center>, <area>
    #     # print(stats)
    #     region_count = region.copy()
    #     for key,value in region.items():
    #         #print(key, len([item for item in value if item]))
    #         region_count[key] = len([item for item in value if item])
    #     print(region_count)
     return 0


    def mark_regions_image(self, image, stats):
        """Creates a new image with computed stats
        takes as input
        image: a list of pixels in a region
        stats: stats regarding location and area
        returns: image marked with center and area"""

        return image

