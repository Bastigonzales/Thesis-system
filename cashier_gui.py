import tkinter as tk
import pyttsx3
import os
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox

root = tk.Tk()
root.title("Cashier Text to Speech - Speech to Text")

#Replaced Window Icon
icon_path = "./images/title_Icon.ico"
root.iconbitmap(icon_path)

#Size of Window
root.geometry("900x600")
root.resizable(False,False)

#Start the main loop
root.mainloop()