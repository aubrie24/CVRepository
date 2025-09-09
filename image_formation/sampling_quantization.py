#Author: Aubrie Pressley
#Date: 09/08/2025
#Description: Explore how contiuous signals is converted into a digital one.
#Sources: Repository assignment 1, Lecture slides
#Refactored the code so functions can be used in exercise 4

import numpy as np
import matplotlib.pyplot as plt

#global parameters 
signal_freq = 5 #in Hz
duration = 2 #in seconds
sampling_freq = 8 #in Hz
num_bits = 3 #3 bit quantization (8 levels: 0-7)
min_signal = -1 #min signal value
max_signal = 1 #max signal value

#t is a value or numpy vector
def original_signal(t):
    return np.sin(2 * np.pi * signal_freq * t)

#plotting function 
def plot_signal(t, signal, title):
    plt.figure()
    plt.plot(t, signal)
    plt.title(title)
    plt.grid()
    plt.show()

#sampling function 
def sample_signal(duration, sampling_freq):
    n = int(sampling_freq * duration) #number of samples
    t_sampled = np.linspace(0, duration, n, endpoint=False) #sampled time points
    sampled_signal = original_signal(t_sampled)
    return t_sampled, sampled_signal

#quantization function
def quantize_signal(sampled_signal, num_bits, min_signal, max_signal):
    qs = np.round((sampled_signal - min_signal) / (max_signal - min_signal) * (num_bits - 1)) #quantized signal
    qv = min_signal + qs * (max_signal - min_signal) / (num_bits - 1) #quantized values
    return qs, qv

def main(): 
    #plot the original signal over a 2 second time window
    t_points = np.linspace(0, duration, 1000, endpoint=False) #1000 points in [0, duration)
    cont_signal = original_signal(t_points)
    plot_signal(t_points, cont_signal, "continuous signal")

    #sample the original signal
    t_sampled, sampled_signal = sample_signal(duration, sampling_freq)
    plot_signal(t_sampled, sampled_signal, "sampled signal")

    #quantize the sampled signal
    qs, qv = quantize_signal(sampled_signal, num_bits, min_signal, max_signal)

    #plot the quantized signal as a staricase plot
    plt.step(t_sampled, qv, where='post', label=f'Quantized Signal ({num_bits} bits)', color='r', linestyle='--')
    plt.show()

if __name__ == "__main__":
    main()
