#Author: Aubrie Pressley
#Date: 10/01/2025
#Description: Perform full historam equalization on an image
#Acklowledgements: 

import cv2
import calculate_histogram
import numpy as np
import contrast_stretch
import matplotlib.pyplot as plt

#function to perform histogram equalization 
def equalize_histogram(img, bins=100):
    hist, norm_hist = calculate_histogram.calculate_histogram(img, bins) #get the histogram and normalized histogram

    #compute the cumulative distribution function (CDF)
    cdf = [0] * len(norm_hist)
    cdf[0] = norm_hist[0]
    for i in range(1, len(norm_hist)):
        cdf[i] = cdf[i - 1] + norm_hist[i]

    #map the CDF to the full intensity range [0, 255]
    equalization_map = [int(c * 255) for c in cdf]

    #apply the mapping to get the equalized image (used chatGPT for help)
    equalized_img = np.zeros_like(img, dtype='uint8')
    bin_width = 256.0 / bins 

    #iterate through every pixel to find its bin and apply the new intensity 
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            pixel = img[i, j]
            bin_index = int(pixel / bin_width) #find bin index for current pixel 
            if bin_index >= bins: #safety check for the highest possible value to ensure it lands in last bin 
                bin_index = bins - 1
            equalized_img[i, j] = equalization_map[bin_index] #apply mapping 

    return equalized_img

#MAIN DRIVER CODE FOR EXERCISE 1
#driver code to create side by side comparison of original, contrast stretched, and equalized images
def main():
    #get the image 
    img_grayscale = cv2.imread('./images/low_contrast.jpg', cv2.IMREAD_GRAYSCALE) #read in grayscale
    img = cv2.imread('./images/low_contrast.jpg') #non gray scale for contrast stretching
    assert img is not None, "file could not be read"

    stretched_img = contrast_stretch.main(img) #perform contrast stretching on original image

    equalized_hist = equalize_histogram(img_grayscale) #compute the entire histogram equalization process on original image

    #print min and max pixel values for equalized hist image
    print(f"Minimum pixel value in equalized image: {np.min(equalized_hist)}")
    print(f"Maximum pixel value in equalized image: {np.max(equalized_hist)}")

    #plot original, contrast stretched, and equalized images side by side
    plt.figure(figsize=(15, 5))
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Original Image')
    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(stretched_img, cv2.COLOR_BGR2RGB))
    plt.title('Contrast Stretched Image')
    plt.subplot(1, 3, 3)
    plt.imshow(equalized_hist, cmap='gray')
    plt.title('Histogram Equalized Image')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()