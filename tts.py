# TTS (Text to Speech)
# STT (Speech to Text)

from gtts import gTTS # Google Text-to-Speech
from playsound import playsound

file_name = "tts.mp3"

# language: English
# text = "Not All Of Us Can Afford To Be Romantic."
# tts_en = gTTS(text=text, lang="en")
# tts_en.save(file_name)
# playsound(file_name)

# language: Korean
# text = "편견은 내가 다른 사람을 사랑하지 못하게 하고, 오만은 다른 사람이 나를 사랑하지 못하게 한다."
# tts_ko = gTTS(text=text, lang="ko")
# tts_ko.save(file_name)
# playsound(file_name)

# tts from a text file
with open("bigbang.txt", "r", encoding="utf8") as f:
    text = f.read()

tts_file = gTTS(text=text, lang="en")
tts_file.save(file_name)
playsound(file_name)
