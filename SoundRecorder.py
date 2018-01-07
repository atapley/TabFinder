import pyaudio
import wave
import os
from pathlib import Path

def record():
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 10
    SAVE_PATH = '/Users/alex_tapley/Documents/Python_Projects/TabFinder/'
    WAVE_OUTPUT_FILENAME = 'file.wav'
    COMPLETE_NAME = os.path.join(SAVE_PATH, WAVE_OUTPUT_FILENAME)

    if Path(COMPLETE_NAME).is_file():
        os.remove(COMPLETE_NAME)

    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("listening...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("finished listening")

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
