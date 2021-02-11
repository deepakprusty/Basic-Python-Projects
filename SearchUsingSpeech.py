import speech_recognition as sr
import webbrowser

sr.Microphone(device_index=1)
r = sr.Recognizer()

r.energy_threshold = 4500

with sr.Microphone() as source:
    print("OMG Now What? speak up  ")
    audio = r.listen(source)
    try:
        text =r.recognize_google(audio)
        print("you said : ".format(text))
        url = 'https://www.google.com/search?q='
        search_url = url+text
        webbrowser.open(search_url)
    except:
        print("Repeat, cant recognise")
