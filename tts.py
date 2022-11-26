# TTS (Text to Speech)
# STT (Speech to Text)

from gtts import gTTS # Google Text-to-Speech
from playsound import playsound

file_name = "sample.mp3"

# language: English
# text = "Imagine that you have just arrived at a hotel after a tiring 7-hour overnight flight."
# tts_en = gTTS(text=text, lang="en")
# tts_en.save(file_name)
# playsound(file_name)

# language: Korean
# text = "라이브러리를 활용한 데이터 과학과 머신러닝"
# tts_ko = gTTS(text=text, lang="ko")
# tts_ko.save(file_name)
# playsound(file_name)

# long text (open from a file)
with open("sample.txt", "r", encoding="utf8") as f:
    text = f.read()

tts_ko = gTTS(text=text, lang="ko")
tts_ko.save(file_name)
playsound(file_name)
