import pyttsx3
import speech_recognition as sr
import PySimpleGUI as sg
import vosk

#Speech To Text Layout

layout = [[sg.Text("Speech to Text")],
          [sg.Multiline(size=(70, 20), key="-OUTPUT-")], 
          [sg.Button("Record", button_color=('white', 'grey'), border_width=10), 
           sg.Button("Exit", button_color=('white', 'red'), border_width=10)]]


#New window
window = sg.Window("Speech To Text", layout)



#Loop for Events
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    elif event == "Record":
        #recognizer
        r = sr.Recognizer()

        #Record Audio
        with sr.Microphone() as source:
            audio = r.listen(source)


    #Vosk
    try:
        text = r.recognize_vosk(audio)
        window["-OUTPUT-"].update(text)
    except sr.UnknownValueError():
        window["-OUTPUT-"].update("Could not Understand, Try again")
    except sr.RequestError as e:
        window["-OUTPUT-"].update(f"Error: {e}")

window.close()