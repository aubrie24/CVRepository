#Author: Aubrie Pressley
#Date: 10/01/2025
#Description: Applies a median filter of the given size to the input image

import cv2
import numpy as np
import matplotlib.pyplot as plt
import calculate_gradient

#for each window, extract the pixel neighborhood, sort the values, replace the center pixel with the median value
def median_filter(img, size=3):
    #check if the filter size is odd
    if size % 2 == 0:
        raise ValueError("Filter size must be odd")
    
    #pad the imagea to handle borders
    pad = size // 2
    padded_img = np.pad(img, pad, mode='edge') #pad with edge values

    #prepare an output image 
    new_img = np.zeros_like(img)

    #apply median filter
    for i in range(img.shape[0]): #iterate through rows
        for j in range(img.shape[1]): #iterate through columns
            #extract the neighborhood
            neighborhood = padded_img[i:i + size, j:j + size]
            #compute the median and assign it to the center pixel
            new_img[i, j] = np.median(neighborhood)

    return new_img

#drive code for exerscise 2, load img, apply median filter, apply Sx and Sy with and without median filter, compare results
def main():
    #read in image 
    img = cv2.imread('images/noisy_image.png', cv2.IMREAD_GRAYSCALE)
    assert img is not None, "file could not be read"
    
    #apply median filter
    filtered_img = median_filter(img, size=3)

    #apply Sx and Sy without median filter (angle is not used in this but is returned by the function)
    edges_without_filter, _ = calculate_gradient.calculate_gradient(img)

    #apply Sx and Sy with median filter
    edges_with_filter, _ = calculate_gradient.calculate_gradient(filtered_img)

    #compare the gradient magnitudes with and without median filtering
    mean_grad_no_filter = edges_with_filter.mean()
    mean_grad_with_filter = edges_without_filter.mean()
    std_grad_no_filter = edges_with_filter.std()
    std_grad_with_filter = edges_without_filter.std()

    #count strong gradients above a threshold
    threshold = 100
    edges_count_no_filter = np.sum(edges_without_filter > threshold)
    edges_count_with_filter = np.sum(edges_with_filter > threshold)

    #print results
    print(f"Without Median Filter: ")
    print(f"    Mean Gradient Magnitude: {mean_grad_no_filter}")
    print(f"    Std Dev of Gradient Magnitude: {std_grad_no_filter}")
    print(f"    Number of Strong Gradients (>{threshold}): {edges_count_no_filter}")

    print(f"With Median Filter: ")
    print(f"    Mean Gradient Magnitude: {mean_grad_with_filter}")
    print(f"    Std Dev of Gradient Magnitude: {std_grad_with_filter}")
    print(f"    Number of Strong Gradients (>{threshold}): {edges_count_with_filter}")

    #sdisplay the results beside the original image using matplotlib
    plt.figure(figsize=(15, 6))
    plt.subplot(1, 4, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')

    plt.subplot(1, 4, 2)
    plt.imshow(filtered_img, cmap='gray')
    plt.title('Median Filtered Image')

    plt.subplot(1, 4, 3)
    plt.imshow(edges_without_filter, cmap='gray')
    plt.title('Edges without Median Filter')

    plt.subplot(1, 4, 4)
    plt.imshow(edges_with_filter, cmap='gray')
    plt.title('Edges with Median Filter')
    plt.show()

if __name__ == "__main__":
    main()