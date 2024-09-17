import tkinter as tk
import pyttsx3
import speech_recognition as sr
import PySimpleGUI as sg
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox


#Speak Hello
def speak_text():
    engine = pyttsx3.init()
    engine.say("Hello!")
    engine.runAndWait()
    engine.stop()


#Speak Good Morning
def speak_morning():
    engine = pyttsx3.init()
    engine.say("Good Morning!")
    engine.runAndWait()
    engine.stop()


#Speak Good Afternoon
def speak_afternoon():
    engine = pyttsx3.init()
    engine.say("Good Afternoon!")
    engine.runAndWait()
    engine.stop()


#Speak Good Evening
def speak_evening():
    engine = pyttsx3.init()
    engine.say("Good Evening!")
    engine.runAndWait()
    engine.stop()

#Speak How May I help
def speak_help():
    engine = pyttsx3.init()
    engine.say("How May I help you?")
    engine.runAndWait()
    engine.stop()


#Speak Do you want to add anything
def speak_add():
    engine = pyttsx3.init()
    engine.say("Do you want too add anything?")
    engine.runAndWait()
    engine.stop()

#Speak Thank you
def speak_thanks():
    engine = pyttsx3.init()
    engine.say("Thank you!!")
    engine.runAndWait()
    engine.stop()

#Window Title
root = tk.Tk()
root.title("Cashier Text to Speech - Speech to Text")

#Replaced Window Icon
icon_path = "./images/title_Icon.ico"
root.iconbitmap(icon_path)

#Size of Window
root.geometry("900x600+100+100")
root.resizable(False,False)
root.configure(bg="#f64d29")


#Header
Top_frame=Frame(root,bg="#ffffff",width=900,height=100)
Top_frame.place(x=0,y=0)
Logo=PhotoImage(file="./images/tonyo_Icon.png")
Label(Top_frame,image=Logo,bg="#ffffff").place(x=10,y=5)

 
# Create a label and entry field for the text
text_label = tk.Label(root, text="Preset Conversations:", bg="white", font=("bold", 10))
text_label.pack()
text_label.place(x=550,y=200)

#HELLO BUTTON
speak_button = tk.Button(root, text="Hello", command=speak_text)
speak_button.pack()
speak_button.place(x=550,y=260)

#GOOD MORNING BUTTON
speak_button = tk.Button(root, text="Good Morning", command=speak_morning)
speak_button.pack()
speak_button.place(x=550,y=300)


#GOOD AFTERNOON BUTTON
speak_button = tk.Button(root, text="Good Afternoon", command=speak_afternoon)
speak_button.pack()
speak_button.place(x=550,y=340)


#GOOD EVENING BUTTON
speak_button = tk.Button(root, text="Good Evening", command=speak_evening)
speak_button.pack()
speak_button.place(x=550,y=380)

#HOW MAY I HELP YOU BUTTON
speak_button = tk.Button(root, text="How May I help you?", command=speak_help)
speak_button.pack()
speak_button.place(x=550,y=420)

#DO YOU WANT ANYTHING BUTTON
speak_button = tk.Button(root, text="Do you want to add anything?", command=speak_add)
speak_button.pack()
speak_button.place(x=550,y=460)


#THANK YOU BUTTON
speak_button = tk.Button(root, text="Thank you!!", command=speak_thanks)
speak_button.pack()
speak_button.place(x=550,y=500)


#Speech To Text Button
text_box = tk.Text(root, height=5, width=30, x=20, y=100)
text_box.pack()
record_button = tk.Button(root, text="Speak")
record_button.pack()
record_button.place(x=50, y=100)


#Start the main loop
root.mainloop()
