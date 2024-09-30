import numpy as np
import matplotlib.pyplot as plt

def bipolar_ami_encoding(bit_sequence):
    signal = []
    polarity = 1
    
    for bit in bit_sequence:
        if bit == '0':
            signal.append(0)
        elif bit == '1':
            signal.append(polarity)
            polarity *= -1
    
    return signal

def plot_signal(bit_sequence, signal):
    time = np.arange(len(bit_sequence))
    
    plt.step(time, signal, where='post', marker='o', linestyle='-', color='b')
    plt.title("Bipolar AMI Encoding")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.yticks([-1, 0, 1])
    plt.grid(True)
    plt.show()

bit_sequence = "0100100"
encoded_signal = bipolar_ami_encoding(bit_sequence)
plot_signal(bit_sequence, encoded_signal)