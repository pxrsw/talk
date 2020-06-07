import pyttsx3
engine = pyttsx3.init()
while True:
    text = input()
    if text == '0':
        exit()
    else:
        engine.say(text)
        engine.runAndWait()
