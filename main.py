def fireENG():
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
    color = ["red", "blue", "green", "yellow",
             "purple", "black", "magenta"]
    shape = ["circle", "square", "triangle",
             "rectangle", "hexagon", "star"]

    def record_audio():
        try:
            with sr.Microphone() as source:
                print("Listening...\n")
                audio = r.listen(source, timeout=4)
                voice_data = r.recognize_google(
                    audio, language='en-EN')  # pl-PL for Polish
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

    r = sr.Recognizer()

    os.system('cls')
    colors = ""
    for c in color:
        colors += c + " "

    shapes = ""
    for s in shape:
        shapes += s + " "

    msg = "Say any color and shape from available ones, then wait for a few seconds. \nColors: " + \
        colors + "\nShapes: " + shapes
    ds.turtleLabel(colors, shapes, msg)

    record = record_audio()

    try:
        args = record.split()

    except Exception as e:
        args = record

    print(args)
    speak(record, lang='en')  # pl for Polish

    if(args == None):
        ds.draw("error")

    elif(len(args) < 2):
        if(args[0].lower() == "greenstar"):
            ds.draw("star", "green")

        elif(args[0].lower() == "medstar" or args[0].lower() == "radstar"):
            ds.draw("star", "red")

        else:
            ds.draw(args[0])

    else:
        if(args[0].lower() in color or args[1].lower() in shape):
            ds.draw(args[1].lower(), args[0].lower())

        elif(args[0].lower() in shape or args[1].lower() in color):
            ds.draw(args[0].lower(), args[1].lower())

        else:
            ds.draw(args[0])
