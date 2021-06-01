def firePL():
    import os
    os.system('cls')
    print("Loading modules...")

    import re
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    from textblob import TextBlob
    import time
    import json
    import requests
    import pandas as pd
    from datetime import datetime
    import en_core_web_sm
    import playsound
    from gtts import gTTS
    from time import ctime
    import speech_recognition as sr
    import spacy
    import drawingShapes as ds

    nlp = spacy.load("en_core_web_sm")
    colorENG = ["red", "blue", "green", "yellow",
                "purple", "black", "fuchsia"]
    shapeENG = ["circle", "square", "triangle",
                "rectangle", "hexagon", "star"]

    color = ["czerwony", "niebieski", "zielony", "żółty",
             "purpurowy", "czarny", "fuksja"]
    shape = ["koło", "kwadrat", "trójkąt",
             "prostokąt", "sześciokąt", "gwiazda"]

    def record_audio():
        try:
            with sr.Microphone() as source:
                print("Listening...\n")
                audio = r.listen(source, timeout=3)
                voice_data = r.recognize_google(
                    audio, language='pl-PL')  # pl-PL for Polish
                return str(voice_data)
        except Exception as e:
            print(f"Something went wrong... {e}")

    def speak(text, lang):
        tts = gTTS(text, lang=lang)
        r = datetime.now()
        timeStr = r.strftime("%H.%M.%S")
        audio_file = 'audio-' + str(timeStr) + '.mp3'
        tts.save(audio_file)
        print(text)
        playsound.playsound(audio_file)
        os.remove(audio_file)

    def translate(text, dest='en', src='pl'):
        from textblob import TextBlob
        blob = TextBlob(text)
        try:
            tr = blob.translate(to=dest, from_lang=src)
            return str(tr)
        except Exception as e:
            return text

    r = sr.Recognizer()

    os.system('cls')
    colors = ""
    for c in color:
        colors += c + " "

    shapes = ""
    for s in shape:
        shapes += s + " "

    msg = "Powiedz wyraźnie kolor oraz kształt z pośród dostępnych i odczekaj kilka sekund. \nKolory: " + \
        colors + "\nKształty: " + shapes
    ds.turtleLabel(colors, shapes, msg)

    record = record_audio()

    recordEng = translate(record)

    try:
        args = recordEng.split()

    except Exception as e:
        args = recordEng

    print(args)
    print(recordEng)
    speak(record, lang='pl')  # pl for Polish

    if(args == None):
        ds.draw("error")

    elif(len(args) < 2):
        if(args[0].lower() == "greenstar"):
            ds.draw("star", "green")

        else:
            ds.draw(args[0])

    else:
        if(args[0].lower() in colorENG):
            ds.draw(args[1].lower(), args[0].lower())

        elif(args[0].lower() in shapeENG):
            ds.draw(args[0].lower(), args[1].lower())

        else:
            ds.draw(args[0])
