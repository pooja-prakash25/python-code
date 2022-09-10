from gtts import gTTS
import os


fh = open("ANN.txt","r")
mytext= fh.read().replace("\n"," ")

language = 'en'

voice= gTTS(text=mytext,lang=language,slow=False)

voice.save("voice.mp3")

fh.close()

os.system("start voice.mp3")
