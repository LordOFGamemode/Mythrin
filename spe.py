import speech_recognition as sr
srengin = sr.Recognizer()
file_name = "file"
def from_file():
    with sr.AudioFile(file_name) as f:
        data = srengin.record(f)
        text = srengin.recognize_google(data, language="de-DE")
        print(text)
def from_mic():
    with sr.Microphone() as mic:
        print("recording")
        audio = srengin.record(mic, duration=10)

        print('working')
        text = srengin.recognize_google(audio, language='de-DE')
        return text

