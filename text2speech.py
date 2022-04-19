import pyttsx3
engine = pyttsx3.init()
text = "So guys i created this text2 speech program and calling name of our two IPL lovers. Anand anand anand anand daana daana daana daana daana daana"
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 105)
engine.say(text)
engine.runAndWait()
