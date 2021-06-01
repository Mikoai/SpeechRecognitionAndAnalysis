import tkinter as tk
import mainPL
import main
from sentiment import fireSentiment
from turtle import *
import turtle
import json

root = tk.Tk()
root.title("Speech recognition")


def sentimentWindow(lang='en_EN'):
    sentWindow = tk.Tk()
    sentWindow.title("Sentiment analisys")
    canv = tk.Canvas(sentWindow, width=640, height=480)
    canv.grid(columnspan=2, rowspan=3)

    def sentReturn():
        value = fireSentiment(lang)
        tk.Label(sentWindow, text=value.get('text')).grid(column=1, row=1)

        result = ""
        if(value.get('score') < -0.1):
            result = "Negative"
        elif(value.get('score') > 0.1):
            result = "Positive"
        else:
            result = "Neutral"

        tk.Label(sentWindow, text="Score: " + str(value.get('score')) +
                 " - " + result).grid(column=1, row=2)

    tk.Label(
        sentWindow, text="Press button, say something, then wait for a few seconds").grid(columnspan=2, column=0, row=0)
    tk.Button(
        sentWindow, text="Start", bg="#20bebe", fg="white", height=1, width=6, command=lambda: sentReturn()).grid(rowspan=2, column=0, row=1)


tk.Canvas(root, width=640, height=480).grid(columnspan=2, rowspan=4)

tk.Label(root, text="Choose an app").grid(columnspan=2, column=0, row=0)

tk.Label(root, text="Drawing shapes based on speech").grid(column=0, row=1)


tk.Button(
    root, text="Polski", bg="#20bebe", fg="white", height=1, width=6, command=mainPL.firePL).grid(column=0, row=2)

tk.Button(
    root, text="English", bg="#20bebe", fg="white", height=1, width=6, command=main.fireENG).grid(column=0, row=3)


tk.Label(root, text="Sentiment analisys").grid(column=1, row=1)

tk.Button(
    root, text="Polski", bg="#20bebe", fg="white", height=1, width=6, command=lambda: sentimentWindow('pl_PL')).grid(column=1, row=2)

tk.Button(
    root, text="English", bg="#20bebe", fg="white", height=1, width=6, command=lambda: sentimentWindow()).grid(column=1, row=3)


root.mainloop()
