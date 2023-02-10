import random
import librosa
import numpy as np
import soundfile as sf
from utils.plot_signal import plot_original_and_augmented_signal

#Add a white noise
def add_white_noise(signal, noise_percentage_factor):
    noise = np.random.normal(0, signal.std(), signal.size)
    augmented_signal = signal + noise * noise_percentage_factor
    return augmented_signal

#Time Stretch
def time_strech(signal, strech_rate):
    return librosa.effects.time_stretch(signal, strech_rate)

# Pitch Scaling
def pitch_scale(signal, sr, num_semitones):
    return librosa.effects.pitch_shift(signal, sr, num_semitones)

#Polarity Inversion
def invert_polarity(signal):
    return signal*-1

#Random Gain
def random_gain(signal, min_factor, max_factor):
    gain_rate = random.uniform(min_factor, max_factor)
    augmented_signal = signal * gain_rate
    return augmented_signal


if __name__ == "__main__":
    signal, sr = librosa.load("piano.wav")
    augmented_signal = random_gain(signal,2,4)
    sf.write("augmented_audio.wav", augmented_signal, sr)
    plot_original_and_augmented_signal(signal, augmented_signal, sr)