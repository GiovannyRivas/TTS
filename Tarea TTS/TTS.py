from gtts import gTTS
import os 
from Clase import *
text = summary
language = 'es-us'
speech = gTTS(text = text, lang = language, slow = False)
speech.save ("Moscow.mp3")
os.system("start Moscow.mp3")


