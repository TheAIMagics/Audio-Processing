import librosa.display
import matplotlib.pyplot as plt

def plot_original_and_augmented_signal(signal, augmented_signal, sample_rate):
    fig, ax = plt.subplots(nrows=2)
    librosa.display.waveshow(signal,sr= sample_rate, ax=ax[0])
    ax[0].set(title="random_gain Original Signal")
    librosa.display.waveshow(augmented_signal,sr= sample_rate, ax=ax[1])
    ax[1].set(title="random_gainGI Augmented Signal")
    plt.show()