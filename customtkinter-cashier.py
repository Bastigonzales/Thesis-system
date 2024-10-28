import customtkinter as ctk
from RealtimeSTT import AudioToTextRecorder
 

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.title("Speech to Text - Text to Speech")
        self.geometry("900x500")

        # Initialize the audio-to-text recorder
        self.recorder = AudioToTextRecorder(spinner=False, model="small.en", language="en")
        
        # Textbox widget to display the transcribed text
        self.text_widget = ctk.CTkTextbox(self, height=120, width=250)
        self.text_widget.place(x=600, y=20)
        
        # Button to start the speech-to-text transcription process
        self.start_button = ctk.CTkButton(self, text="Speak", width=50, command=self.start_transcription)
        self.start_button.place(x=600, y=160)
        
        # Button to stop the speech-to-text transcription process
        self.stop_button = ctk.CTkButton(self, text="Stop", width=50, command=self.stop_transcription)
        self.stop_button.place(x=700, y=160)
        # Disable the stop button initially because transcription hasn't started yet
        self.stop_button.configure(state=ctk.DISABLED)

        # Button to exit the application
        self.ctrl_c_button = ctk.CTkButton(self, text="Exit", width=50, command=self.exit_with_ctrl_c)
        self.ctrl_c_button.place(x=800, y=160)

    # Method to handle the exit button click (closes the window)
    def exit_with_ctrl_c(self):
        self.destroy()  # Destroys the window and exits the application

    # Method to start the transcription process
    def start_transcription(self):
        print("start pressed")  # For debugging purposes
        if self.recorder:
            print("starting recording")  # Debugging message

            # Start the speech-to-text recording
            # Disable the start button and enable the stop button while recording
            self.recorder.start()  
            self.start_button.configure(state=ctk.DISABLED)
            self.stop_button.configure(state=ctk.NORMAL)

    # Method to update the text widget with transcribed text
    def update_text(self, text):

        # Insert the transcribed text at the end of the text widget
        self.text_widget.insert(ctk.END, text)

        # Scroll the text widget to show the latest transcribed text
        self.text_widget.see(ctk.END)

    # Method to stop the transcription process and display the result
    def stop_transcription(self):
        if self.recorder:
            self.recorder.stop()  # Stop the speech-to-text recording

            text = self.recorder.text()  # Get the transcribed text

            self.update_text(text)  # Update the text widget with the transcription
            # Re-enable the start button and disable the stop button after recording
            
            self.start_button.configure(state=ctk.NORMAL)
            self.stop_button.configure(state=ctk.DISABLED)

# Main execution starts here
if __name__ == "__main__":
    # Set the appearance mode (light or dark theme)
    ctk.set_appearance_mode("light") 

    # Set the default color theme for the widgets
    ctk.set_default_color_theme("blue")
    
    # Create an instance of the App class and run the main event loop
    app = App()
    app.mainloop()