def fireSentiment(lan='en_EN'):
    import sys
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
    import en_core_web_sm
    import playsound
    from time import ctime
    import speech_recognition as sr
    import spacy

    nlp = spacy.load("en_core_web_sm")

    chosenLang = str(lan)  # pl_PL for Polish, en_EN for English

    def record_audio():
        try:
            with sr.Microphone() as source:
                print("Listening...\n")
                audio = r.listen(source, timeout=3)
                voice_data = r.recognize_google(
                    audio, language=chosenLang)
                return str(voice_data)
        except Exception as e:
            print(f"Something went wrong... {e}")

    # def speak(text, lang):
    #     tts = gTTS(text, lang=lang)
    #     r = datetime.now()
    #     timeStr = r.strftime("%H.%M.%S")
    #     audio_file = 'audio-' + str(timeStr) + '.mp3'
    #     tts.save(audio_file)
    #     print(text)
    #     playsound.playsound(audio_file)
    #     os.remove(audio_file)

    def translate(text, dest='en', src='pl'):
        print("\nTranslating...")
        from textblob import TextBlob
        blob = TextBlob(text)

        try:
            tr = blob.translate(to=dest, from_lang=src)
            print("Translated into: " + str(tr))
            return str(tr)
        except Exception as e:
            return text

    def sentiment(text):
        print("\nSentiment analysys...")
        vader = SentimentIntensityAnalyzer()
        sent = vader.polarity_scores(text)
        print(sent)
        sent['score'] = sent.pop('compound')
        tmp = list(sent.keys())[:-1]
        output = {
            'score': sent['score'],
            'magnitude': max([sent[a] for a in tmp])
        }
        return output

    r = sr.Recognizer()

    record = record_audio()

    print(record)

    recordENG = translate(record)

    sentAnal = sentiment(recordENG)

    print(sentAnal)
    sentAnal.update({'text': record})

    return sentAnal
