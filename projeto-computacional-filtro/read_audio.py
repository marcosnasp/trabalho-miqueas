import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

# Replace 'your_audio_file.wav' with the path to your WAV file
file_path = r'C:\Users\Marcos Portela\Documents\Desenv\repository\github\trabalho-miqueas\projeto-computacional-filtro\arquivos_trabalho\ImperialPlusCantina.wav'

# Step 1: Read the WAV file
sample_rate, signal = wav.read(file_path)

# Step 2: Create time axis in seconds
time = np.arange(0, len(signal)) / sample_rate

# Step 3: Create subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# Plot the entire signal
axs[0].plot(time, signal, color='b')
axs[0].set_title('Audio Signal')
axs[0].set_xlabel('Time (s)')
axs[0].set_ylabel('Amplitude')
axs[0].grid(True)

# Plot a zoomed-in portion of the signal (adjust the limits as needed)
start_time = 1  # example start time in seconds
end_time = 2    # example end time in seconds
axs[1].plot(time, signal, color='r')
axs[1].set_title('Zoomed-in Audio Signal')
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('Amplitude')
axs[1].grid(True)
axs[1].set_xlim(start_time, end_time)

# Adjust layout for better spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()
