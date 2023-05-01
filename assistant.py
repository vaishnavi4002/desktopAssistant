import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import time
import desktopAssistant

# Define a function to record audio from microphone
def record_audio(duration, sr):
    print("Recording started...")
    audio = sd.rec(int(duration * sr), samplerate=sr, channels=1)
    sd.wait()  # Wait until recording is finished
    print("Recording finished...")
    return np.squeeze(audio)

# Define main function for voice assistant
def voice_assistant():
    sr = 44100  # Sample rate for recording
    duration = 10  # Duration of recording in seconds
   

 
        # Record audio from microphone
    audio = record_audio(duration, sr)

        # Plot waveform graph of recorded audio
    plt.plot(audio)
    plt.title("Recorded Audio Waveform")
    plt.xlabel("Time (samples)")
    plt.ylabel("Amplitude")
    plt.show()
        
    

# Start voice assistant
voice_assistant()
