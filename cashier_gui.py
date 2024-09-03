import tkinter as tk
import pyttsx3
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox

#Speak Hello
def speak_text():
    engine = pyttsx3.init()
    engine.say("Hello!")
    engine.runAndWait()

    #Speak Good Morning
def speak_morning():
    engine = pyttsx3.init()
    engine.say("Good Morning!")
    engine.runAndWait()

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

 
#HELLO BUTTON
speak_button = tk.Button(root, text="Hello", command=speak_text)
speak_button.pack()
speak_button.place(x=550,y=110)

speak_button = tk.Button(root, text="Good Morning", command=speak_morning)
speak_button.pack()
speak_button.place(x=550,y=150)


#Start the main loop
root.mainloop()