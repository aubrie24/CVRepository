#Author: Aubrie Pressley
#Date: 10/01/2025
#Description: Perform contrast stretching on an image
#Acklowledgements: https://samirkhanal35.medium.com/contrast-stretching-f25e7c4e8e33 to get the general formula for contrast stretching

import cv2
import matplotlib.pyplot as plt

#function to map the intensity range of an image [r_min, r_max] to the full output rage [0, 255] linearly
def contrast_stretch(img, r_min, r_max):
    t_min, t_max = 0, 255 #define the target min and max values

    #apply the contrast stretching formula
    stretched_img = (img - r_min) * ((t_max - t_min) / (r_max - r_min)) + t_min

    #handle out of range values
    stretched_img = stretched_img.clip(0, 255).astype('uint8')

    return stretched_img

def main(img):

    #define the pixel min and max values from the image
    r_min = img.min()
    r_max = img.max()
    print(f"Minimum pixel value in the image: {r_min}")
    print(f"Maximum pixel value in the image: {r_max}")

    #perform contrast stretching
    new_img = contrast_stretch(img, r_min, r_max)

    #define the pixel min and max values from the new image
    new_r_min = new_img.min()
    new_r_max = new_img.max()
    print(f"Minimum pixel value in the contrast stretched image: {new_r_min}")
    print(f"Maximum pixel value in the contrast stretched image: {new_r_max}")

    return new_img

if __name__ == "__main__":
    main()