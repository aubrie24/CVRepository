#Author: Aubrie Pressley
#Date: 10/01/2025
#Description: Obtain the gradient direction map and apply thresholding based on the values or direction_range

import calculate_gradient
import numpy as np

def directional_edge_detector(img, direction_range):
    #get the gradient angle 
    _, grad_angle = calculate_gradient.calculate_gradient(img)
    edge_map = np.zeros_like(grad_angle, dtype=np.uint8)

    #keep only edges within the angle range (keep in mind angles wrap around at 180 degrees)
    mask = ((grad_angle >= direction_range[0]) & (grad_angle <= direction_range[1])) | \
       ((grad_angle >= (direction_range[0] + 180)) & (grad_angle <= (direction_range[1] + 180)))
    edge_map[mask] = 255
    return edge_map