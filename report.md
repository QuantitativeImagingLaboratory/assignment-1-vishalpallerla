#Write everything related to report here

1. Resampling:
    Nearest Neighbor:
    - Height and width of the image are taken using the shape property.
    - new scaling factors fx and fy are converted to float since they are in string format by default and then new height and new width are      calculated and stored in h_rs and w_rs
    - A blank image is generated using all zeroes with new height and weight so that it we can use it to regenerate the original image with      new scaling factors
    - Running through each pixel in the blank image from left to right and top to bottom calculate the new intensity using the old          intensity     values according to the nearest neighbor algorithm(implementation of code in respective files) and assign them i.e store the nearest pixel value from the source image in the destination image array.
    - Resampled image will be generated and stored in the output folder.
    - Nearest neighbor is fast and does not introduce any new or artificial data into the final output.
    - But result image contains some block artifacts(distortions which are not visually very clear)

    Bilinear Interpolation:
    - Height and width of the image are taken using the shape property.
    - new scaling factors fx and fy are converted to float since they are in string format by default and then new height and new width are      calculated and stored in h_rs and w_rs
    - A blank image is generated using all zeroes with new height and weight so that it we can use it to regenerate the original image with      new scaling factors
    - Running through each pixel in the blank image from left to right and top to bottom calculate the new intensity using the old          intensity     values according to the bilinear interpolation algorithm and assign them.
    -This method checks the points surrounding the missing data to mathematically approximate the needed values. This method produces       blurring of edges and edge details


2. Region Counting:
   a) Binarization of image:
      - Computing a histogram:
        *An empty list is initialized with zeroes with the count of 256(intensity values are from 0 to 255)
        *looping from 0 to 255, Going through each pixel in the image, checking the intensity if it is equal to the current iteration value,
         increase the counter by 1 and store in the list.
        * List contains number of pixels for each intensity value.
        * Histogram is generated when list is returned.

      - Find Optimal Threshold:
        *Initialize threshold value to half of the length of the histogram
        *Calculate the expected values in the first half and second half of the histogram respectively.
        *Average the expected values to get the optimal threshold

      - Binarize:
        *For the input image, running through each pixel from left to right and top to bottom, if the intensity is less than the optimal threshold , assign 255 else assign the intensity 0
        *Resulting binary image is stored in the output folder

    b) Blob Coloring:
      - For binary input image I, a region color array R is defined.
      - region counter is initialized with 1
      - While scanning the image left-to-right and top-to-bottom , region numbers are assigned to each pixel according to the blob cooring algorithm written in the code.
      - Then the pixels associated with each region are appended to the regions dictionary
      - Number of regions detected is 71 and associated pixels are printed for each region.

    c) In compute statistics, centroid and the area of each region is calculated
      - Region, Area and Centroid are marked in the figure.
      -

