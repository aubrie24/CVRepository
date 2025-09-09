#Author: Aubrie Pressley
#Date: 09/08/2023
#Description: This file helps visualize the relationships between key camera parameters
#Sources: Class Lecture slides and ChatGPT

import numpy as np
import matplotlib.pyplot as plt

#function to compute and return zi given zo and f
def thin_lins_zi(f, z0):
    zi = 1/((1/f) - (1/z0))
    return zi

#(1) plot the lens to image distance as a function of the object distance for four different focal lengths 
f = [3, 9, 50, 200] #focal lengths in mm

#use a loop to plot a curve for each focal length
plt.figure(figsize=(10, 6))
colors = ['b', 'g', 'r', 'm'] #colors for each focal length

points_per_mm = 4 #number of points to plot per mm of object distance
for i, focal_length in enumerate(f):
    z0_min = 1.1 * focal_length #minimum object distance in mm
    z0_max = 1e4 #maximum object distance in mm
    z0 = np.linspace(z0_min, z0_max, int((z0_max - z0_min) * points_per_mm)) #used chatGPT for this line
    zi = thin_lins_zi(focal_length, z0)
    plt.loglog(z0, zi, color=colors[i], label=f'f = {focal_length} mm')
    plt.axvline(x=focal_length, color=colors[i], linestyle='--') #vertical dashed line at z0 = f

plt.title('Lens to Image Distance vs Object Distance for Various Focal Lengths')
plt.xlabel('Object Distance $z0$ (mm)')
plt.ylabel('Image Distance $zi$ (mm)')
plt.ylim([1e-1, 3000])  # or even [1, 3000] depending on your data
plt.legend()
plt.grid(True, which="both", ls="--")
plt.show()

# (2) Plot the aperature diameter (D) as a function of the focal length (f) for several popular f numbers

#function to compute and return diameter given focal length and f_number
def calc_diameter(f, f_number): 
    D = f / f_number #f number = f / D, so D = f / f number
    return D #return aperature diameter

#(focal length, f/#)
examples = [(24, 1.4), (50, 1.8), (70, 2.8), (200, 2.8), (400, 2.8), (600, 4)]

#loop through examples, calculate diameter, and print results
focal_lengths = []
diameters = []
#plot the results and print in the terminal 
for f_val, f_number in examples:
    D = calc_diameter(f_val, f_number)
    focal_lengths.append(f_val)
    diameters.append(D)
    print(f"For a focal length of {f_val} mm and an f-number of {f_number}, the aperture diameter is {D:.2f} mm.")

plt.figure(figsize=(8, 5))
plt.plot(focal_lengths, diameters, marker='o', color='orange', linewidth=2)
plt.xlabel('Focal Length (mm)')
plt.ylabel('Aperture Diameter (mm)')
plt.title('Aperture Diameter vs Focal Length for Various f-numbers')
plt.grid(True, which="both", ls="--")
plt.show()