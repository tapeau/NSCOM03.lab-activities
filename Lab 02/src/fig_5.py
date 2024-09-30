import matplotlib.pyplot as plt
import numpy as np

def unipolar_line_encoding(bit_sequence):
    bits = [int(bit) for bit in bit_sequence]
    
    time = np.arange(len(bits))
    
    signal = np.array(bits)
    
    return time, signal

def plot_unipolar_encoding(ax, bit_sequence, title):
    time, signal = unipolar_line_encoding(bit_sequence)
    
    ax.step(time, signal, where='post', color='blue')
    ax.set_title(title)
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.set_yticks([0, 1])
    ax.grid(True)

bit_sequence1 = "10110001"
bit_sequence2 = "110111000011"

fig, axs = plt.subplots(2, 1, figsize=(10, 8))
plot_unipolar_encoding(axs[0], bit_sequence1, "Unipolar Line Encoding Sent By The Sender")
plot_unipolar_encoding(axs[1], bit_sequence2, "Unipolar Line Encoding Misinterpreted By The Receiver")
plt.tight_layout()
plt.show()