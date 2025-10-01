#Author: Aubrie Pressley
#Date: 10/01/2025
#Description: Calculate and normalize the histogram of an image without using CV2 functions
#Acklowledgements:

import cv2

#function to calculate the histgram (counts) and the normalized histogram 
def calculate_histogram(img, bins):
    #histogram calculation 
    bin_counts = [0] * bins #to hold results
    bin_width = 256 / bins #width of each bin
    for pixel in img.flatten(): #iterate through each pixel
        #calculate the bin index 
        bin_index = int(pixel / bin_width)

        #safety check for the highest possible value to ensure it lands in last bin 
        if bin_index >= bins: 
            bin_index = bins - 1

        bin_counts[bin_index] += 1 #increment the count for that bin

    #normalize histogram 
    total_pixels = img.size
    norm_hist = [count / total_pixels for count in bin_counts] #divide each bin count by number of pixels 

    return bin_counts, norm_hist