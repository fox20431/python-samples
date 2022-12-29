import pyttsx3

# tts: text to speech
engine = pyttsx3.init() # object creation

engine.setProperty('voice', 'Chinese (Cantonese)')

engine.say("你好！这里是小明正义化身！")
engine.runAndWait()
engine.stop()