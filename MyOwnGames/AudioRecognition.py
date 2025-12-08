import speech_recognition as sr

# Create a recognizer
recognizer = sr.Recognizer()

with sr.Microphone() as mic:
    print("Adjusting for background noise...")   
    recognizer.adjust_for_ambient_noise(mic, duration=1)
    print("Listening... Say something!")

    audio = recognizer.listen(mic)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("API request error:", e)
