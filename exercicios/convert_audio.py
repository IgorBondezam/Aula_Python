from gtts import gTTS

from playsound import playsound


def speak(x, y):
    audio = "speech.mp3"
    language = y
    sp = gTTS(text=x, lang=language, slow=False)

    sp.save(audio)
    playsound(audio)


win = True

if win:
    y = "en"
    x = "Hello Ash, How are youuuuu?"
    speak(x, y)
else:
    y = "pt"
    x = "Sem Congratulation para você"
    speak(x, y)


