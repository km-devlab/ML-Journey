from gtts import gTTS

text = "Hello! You built a fully functional speech engine in five lines of code."
tts = gTTS(text=text, lang="en")
tts.save("speech.mp3")
