import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("file_example_WAV_1MG.wav", "rb")

sample_freq = obj.getframerate()
n_sample = obj.getnframes()
n_channels = obj.getnchannels() 
signal_wave = obj.readframes(-1)
#print(len(signal_wave))
obj.close()

t_audio = n_sample/sample_freq

print(t_audio)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)
#print(signal_array.shape)

# Reshape for stereo files
if n_channels == 2:
    signal_array = signal_array.reshape(-1, 2)
    signal_array = signal_array[:, 1]  # take left channel (or [:,1] for right)

times = np.linspace(0, t_audio, num=n_sample)
plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title('Audio')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()