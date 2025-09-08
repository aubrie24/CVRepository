import cv2
import numpy as np
import matplotlib.pyplot as plt

#Author: Aubrie Pressley
#Date: 09/08/2025
#Description: Given an original image and it's transformed version, apply 2D transformations to get as close as possible to the transformed version.
#Sources used: https://docs.opencv.org/4.x/da/d6e/tutorial_py_geometric_transformations.html and chatGPT

#read the original image
img = cv2.imread('../images/original_image.jpg')
transformed_img = cv2.imread('../images/transformed_image.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"
rows,cols, ch = img.shape #get dimensions of image

#define points for affine transformation
pts1 = np.float32([[35, 36], [209, 34], [34, 209]]) #original points
pts2 = np.float32([[91.7, 57.5], [178.4, 118.2], [159.8, 232.4]])  # desired points

M = cv2.getAffineTransform(pts1, pts2) #get affline matrix
dst = cv2.warpAffine(img, M, (cols, rows)) #apply transformation
print(f"\nAffine has been applied. Here is the warp affline Matrix:\n{M}\n")

#now, perform translation to move the image downwards slightly 
tx, ty = 0, 7 #no horizontal shift, 5 pixel vertical shift
T = np.float32([[1, 0, tx], [0, 1, ty]]) #translation matrix
dst_translated = cv2.warpAffine(dst, T, (cols, rows)) #apply translation with the same size 
print(f"Translation has been applied. Here is the translation Matrix:\n{T}\n")

#display original, transformed image, and reversed engineered output image
plt.figure(figsize=(15, 5))
plt.subplot(1, 4, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) #convert BGR to RGB for displaying correctly
plt.title('Original Image')

plt.subplot(1, 4, 2)
plt.imshow(cv2.cvtColor(transformed_img, cv2.COLOR_BGR2RGB)) #convert BGR to RGB for displaying correctly
plt.title('Transformed Image')

plt.subplot(1, 4, 3)
plt.imshow(cv2.cvtColor(dst_translated, cv2.COLOR_BGR2RGB)) #convert BGR to RGB for displaying correctly
plt.title('Reverse Engineered Image')

plt.tight_layout()
plt.show()