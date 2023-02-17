from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import time
from datetime import datetime
import random
from random import choice
import textwrap
import webbrowser


r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            print("Asistan: Anlayamadım")
        except sr.RequestError:
            print("Asistan: Sistem çalışmıyor")
        return voice
        

def response (voice):
    if "hangi gündeyiz" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today ="pazartesi"
        elif today == "Friday":
            today = "cuma"
        speak(today)

    if "saat kaç" in voice:
        selection = ["Hemen Bakıyorum: ","Bekle da ne acelen var: ","Gardas saat: ","İnsan ilk önce selam verir:"]
        clock = datetime.now().strftime("%H:%M")
        selection= random.choice(selection)
        speak(selection + clock)

    if "not et" in voice:
        speak("Dosya ismi ne olsun?")
        txtfile = record() + ".txt"
        speak("Not etmeye hazırım kaptan")
        thefile = record()
        f = open(txtfile,"w" ,encoding="utf-8")
        f.writelines(thefile)
        f.close()

    if "google'da ara" in voice:
        speak("kaptan ne aramak istersin")
        search = record()
        url ="https://www.google.com/search?q={}".format(search)
        webbrowser.get().open(url)
        speak("{} içinde bulduğum sonuçları gösteriyorum.".format(search))

    if "selam" in voice:
        speak("günün nasıl geçti")

    if "senin" in voice:
        speak("benimde senin nasıl geçtiyse")

    if "topla" in voice:
        speak("Kaptan 1. sayıyı söylermisin")
        sayi1 = record()
        speak("kaptan 2. sayıyı alayım")
        sayi2 = record()
        top = sayi1 + sayi2
        speak("reisim toplam" + top)

def speak (string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("Kaptan selam")

while True:
    voice = record()
    if voice != '':
        voice = voice.lower()
        print(voice.capitalize())
        response(voice)


