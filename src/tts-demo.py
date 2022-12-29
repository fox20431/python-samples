import pyttsx3

# tts: text to speech
engine = pyttsx3.init() # object creation

""" VOICE """
voices = engine.getProperty('voices')
# for voice in voices:
#     print(voice, voice.id)
#     engine.setProperty('voice', voice.id)
#     engine.say("Hello World!")
#     engine.runAndWait()
#     engine.stop()
engine.setProperty('voice', voices[-2].id)

""" RATE """
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 150)     # setting up new voice rate

""" VOLUME """
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

engine.say("你好！这里是小明正义化身！")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()