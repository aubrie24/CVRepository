#Author: Aubrie Pressley
#Date: 10/01/2025
#Description: Applies the Sobel filters to the input image, calculates the magnitude, and then applies a binary threshold to produce a clean binary edge map

import calculate_gradient
import directional_edge_detector
import numpy as np
import cv2
import matplotlib.pyplot as plt

def sobel_edge_detector(img, threshold=100):
    #apply the sobel filters and calculate the gradient magnitude
    gradient_magnitude, _ = calculate_gradient.calculate_gradient(img)

    #apply a binary threshold, set pixels above threshold to 255 (white), below to 0 (black)
    edge_map = np.zeros_like(gradient_magnitude, dtype=np.uint8)
    edge_map[gradient_magnitude >= threshold] = 255
    return edge_map

#driver code for exercise 3, load img, apply sobel edge, directional edge, canny edge, display results
def main():
    #load the image in grayscale
    img = cv2.imread('./images/tiger.jpg', cv2.IMREAD_GRAYSCALE)

    #apply the sobel edge detector
    edge_map = sobel_edge_detector(img, threshold=100)

    #apply the directional edge detector for angles between 0 and 45 degrees
    edge_directional_map = directional_edge_detector.directional_edge_detector(img, direction_range=(40, 50))

    #apply the Canny edge detector with thresholds of 100 and 200
    canny_edges = cv2.Canny(img, 100, 200)

    #display the original and edge maps side by side
    plt.figure(figsize=(16, 6))

    plt.subplot(1, 4, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original')
    plt.axis('off')

    plt.subplot(1, 4, 2)
    plt.imshow(edge_map, cmap='gray')
    plt.title('Sobel Edges')
    plt.axis('off')

    plt.subplot(1, 4, 3)
    plt.imshow(edge_directional_map, cmap='gray')
    plt.title('Directional Edges (40–50°)')
    plt.axis('off')

    plt.subplot(1, 4, 4)
    plt.imshow(canny_edges, cmap='gray')
    plt.title('Canny Edges')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()