import sounddevice as sd
import numpy as np
import speech_recognition as sr

def record_audio(duration=5, fs=16000):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    print("Done recording!")
    return audio, fs

def main():
    recognizer = sr.Recognizer()

    # Record audio using sounddevice (NO PyAudio)
    audio_data, fs = record_audio(duration=4)

    # Convert numpy audio to SpeechRecognition AudioData
    audio_bytes = audio_data.tobytes()
    audio = sr.AudioData(audio_bytes, fs, 2)  # 2 bytes per sample for int16

    print("Recognizing...")
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except Exception as e:
        print("Recognition error:", e)

if __name__ == "__main__":
    main()
