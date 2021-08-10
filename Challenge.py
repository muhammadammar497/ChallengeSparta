import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime

print("Memulai Pembantu Bule Indo")

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)

def ngomong(text):
    engine.say(text)
    engine.runAndWait()

def perintah():
    perintah = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mendengarkan..")
        suara = perintah.listen(source)
    
    try:
        print("Merekognasi..")
        kalimat = perintah.recognize_google(suara, language="id-ID")
        print(f"dia bilang : {kalimat}\n")

    except Exception as any:
        print("Coba ulangi omongannya")
        kalimat = None
    
    return kalimat
    
ngomong("Hallo namaku Bule Indo, ada yang bisa aku bantu?")
kalimat = perintah()

if "instagram" in kalimat.lower():
    url = "instagram.com"
    bukaweb = "C:/Users/MSI TRUE GAMING/AppData/Local/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(bukaweb).open(url)
elif "facebook" in kalimat.lower():
    url = "facebook.com"
    bukaweb = "C:/Users/MSI TRUE GAMING/AppData/Local/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(bukaweb).open(url)
elif "youtube" in kalimat.lower():
    url = "youtube.com"
    bukaweb = "C:/Users/MSI TRUE GAMING/AppData/Local/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(bukaweb).open(url)
elif "sparta" in kalimat.lower():
    url = "sparta2020.tech/#/"
    bukaweb = "C:/Users/MSI TRUE GAMING/AppData/Local/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(bukaweb).open(url)

elif "jam" in kalimat.lower():
    jam = datetime.datetime.now().strftime("%H:%M")
    ngomong(f"sekarang pukul {jam}")
