#Author: Aubrie Pressley
#Date: 10/1/2025
#Description: Use my apply convolution function to apply the Sobel Sx and Sy filters, then compute the gradient magnitude

import numpy as np

#function that takes a single channel image and applies a convolution filter, from project 1
#Assign 0s to border pixels
def apply_convolution(image, filter):
    k = filter.shape[0] #number of rows and columns in square filter
    pad = k //2 #for border handling 

    #empty array to hold new image, target size is the same as original image (rows, columns)
    convolved_img = np.zeros([image.shape[0], image.shape[1]]) 

    for i in range(convolved_img.shape[0]): #iterate through rows 
        for j in range(convolved_img.shape[1]): #iterate through columns
        
            #check if the value is a border value and assign it 0 if so 
            if i < pad or i >= image.shape[0] - pad or j < pad or j >= image.shape[1] - pad:
                convolved_img[i, j] = 0
            else: 
                mat = image[i - pad: i + pad + 1, j - pad : j + pad + 1] #the block of image that the filter is going to be applied to, region centered at [i, j]
                convolved_img[i, j] = np.sum(np.multiply(mat, filter)) #perform element wise multiplication and sum everything after
    
    # normalize the convolved image to 0–255 and convert to uint8
    convolved_img = np.clip(convolved_img, 0, 255).astype(np.uint8)
    return convolved_img

def calculate_gradient(img):
    #define Sobel filters 
    Sx = np.array([[-1, 0, 1], 
                   [-2, 0, 2], 
                   [-1, 0, 1]])
    Sy = np.array([[-1, -2, -1], 
                   [0, 0, 0], 
                   [1, 2, 1]])
    
    #apply convolution 
    grad_x = apply_convolution(img, Sx)
    grad_y = apply_convolution(img, Sy)

    #compute gradient magnitude
    gradient_magnitude = np.sqrt(np.square(grad_x.astype(float)) + np.square(grad_y.astype(float)))

    #normalize to 0-255 and convert to uint8
    gradient_magnitude = (gradient_magnitude / np.max(gradient_magnitude)) * 255
    gradient_magnitude = gradient_magnitude.astype(np.uint8)

    #gradient direction (in degrees, range -180 to 180)
    grad_angle = np.arctan2(grad_y, grad_x) * (180 / np.pi)

    return gradient_magnitude, grad_angle


