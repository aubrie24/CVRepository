#Author: Aubrie Pressley
#Date: 09/09/2025
#Description: Model noise by adding a Guassian random signal and observe the effect in the captured signal. 
#Sources: ChatGPT, Repository assignment 1, Lecture slides

import numpy as np
import matplotlib.pyplot as plt
#use refactored functions from exercise 3
from sampling_quantization import original_signal, plot_signal, sample_signal, quantize_signal

#global parameters
mean = 0
std_dev = 0.1 #noise level 
signal_freq = 5 #in Hz
duration = 2 #in seconds
sampling_freq = 8 #in Hz
num_bits = 3 #3 bit quantization (8 levels: 0-7)
min_signal = -1 #min signal value
max_signal = 1 #max signal value

#function to create a vector of random values pulled from a 
#gaussian distribution with given mean and standard deviation and then add it to signal
def add_Gaussian_noise(signal, mean, std):
    mag = np.max(signal) - np.min(signal) #magnitude of the signal
    noise = np.random.normal(mean, std * mag, len(signal)) #generate noise
    noisy_signal = signal + noise #add noise to original signal
    return noisy_signal

def main(): 
    #create the original signal over a 2 second time window
    t_points = np.linspace(0, duration, 1000, endpoint=False) #1000 points in [0, duration)
    cont_signal = original_signal(t_points)

    #add noise to the original signal 
    noisy_signal = add_Gaussian_noise(cont_signal, mean, std_dev)

    #plot the noisy signal
    plot_signal(t_points, noisy_signal, "noisy signal")

    #sample
    t_sampled, sampled_signal = sample_signal(duration, sampling_freq)
    plot_signal(t_sampled, sampled_signal, "sampled signal") 

    #quantize 
    qs, qv = quantize_signal(sampled_signal, num_bits, min_signal, max_signal)

    #plot the quantized signal as a staricase plot
    plt.step(t_sampled, qv, where='post', label=f'Quantized Signal ({num_bits} bits)', color='r', linestyle='--')
    plt.show()

    #compute and print MSE, RMSE, PSNR 
    #mse = 1/n * sum((signal original - signal noisy)^2) when the sum is over i = 0 to n -1
    mse = np.mean((cont_signal - noisy_signal) ** 2) #line created by ChatGPT
    rmse = np.sqrt(mse)
    psnr = 10 * np.log10((np.abs(np.max(cont_signal)) ** 2) / mse)
    print(f"MSE: {mse:.6f}\n")
    print(f"RMSE: {rmse:.6f}\n")
    print(f"PSNR: {psnr:.2f} dB\n")

if __name__ == "__main__":
    main()

