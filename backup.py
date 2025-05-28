import customtkinter as ctk
import pyttsx3
from RealtimeSTT import AudioToTextRecorder
 
# Menu items
menu = {
    "Tonyo's Special Lugaw": 99.00,
    "Longsilog": 129.00,
    "Tapsilog": 129.00,
    "Tocilog": 129.00,
    "Pansit bihon (Regular)": 189.00,
    "Lumpiang Shanghai (20pcs)": 269.00,
    "Coke Can": 75.00,
    "Iced tea": 80.00,
    "Halo-Halo": 120.00,
}


# Initialize TTS engine
tts_engine = pyttsx3.init()

#Speak Hello
def speak_hello():
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
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.title("Speech to Text - Text to Speech")
        self.geometry("1100x700")
        self.resizable(False, False)

        # --- Left-Side Menu ---
        self.title = ctk.CTkFrame(self, width=200, corner_radius=10)
        self.title.pack(side="left", fill="y", padx=10, pady=10)

        self.menu_label = ctk.CTkLabel(self.title, text="Menu", font=ctk.CTkFont(size=14, weight="bold"))
        self.menu_label.pack(pady=10)

        for index, (item, price) in enumerate(menu.items(), start=1):
            menu_item_label = ctk.CTkLabel(self.title, text=f"{index}. {item} - ₱{price:.2f}")
            menu_item_label.pack(anchor="w", padx=10, pady=2)

        # Initialize the audio-to-text recorder
        self.recorder = AudioToTextRecorder(spinner=False, model="small.en", language="en")
        
        # Textbox widget to display the transcribed text
        self.text_widget = ctk.CTkTextbox(self, height=120, width=250)
        self.text_widget.place(x=800, y=50)
        
        # Button to start the speech-to-text transcription process
        self.start_button = ctk.CTkButton(self, text="Speak", width=50, command=self.start_transcription)
        self.start_button.place(x=800, y=210)
        
        # Button to stop the speech-to-text transcription process
        self.stop_button = ctk.CTkButton(self, text="Stop", width=50, command=self.stop_transcription)
        self.stop_button.place(x=900, y=210)
        # Disable the stop button initially because transcription hasn't started yet
        self.stop_button.configure(state=ctk.DISABLED)

        # Button to exit the application
        self.ctrl_c_button = ctk.CTkButton(self, text="Exit", width=50, command=self.exit_with_ctrl_c)
        self.ctrl_c_button.place(x=1000, y=210)

        #Text to Speech Buttons

        self.tts_label = ctk.CTkLabel(self, text="STT/TTS", font=ctk.CTkFont(size=14, weight="bold"))
        self.tts_label.place(x=900, y=10)

        self.speak_button = ctk.CTkButton(self, text="Hello", width=70, command=speak_hello)
        self.speak_button.place(x=800,y=270)

        self.speak_button = ctk.CTkButton(self, text="Good Morning", width=70, command=speak_morning)
        self.speak_button.place(x=800,y=310)

        self.speak_button = ctk.CTkButton(self, text="Good Afternoon", width=70, command=speak_afternoon)
        self.speak_button.place(x=800,y=350)

        self.speak_button = ctk.CTkButton(self, text="Good Evening", width=70, command=speak_evening)
        self.speak_button.place(x=800,y=390)

        self.speak_button = ctk.CTkButton(self, text="How May I help you?", width=70, command=speak_help)
        self.speak_button.place(x=800,y=430)

        self.speak_button = ctk.CTkButton(self, text="Do you want too add anything?", width=70, command=speak_add)
        self.speak_button.place(x=800,y=470)

        self.speak_button = ctk.CTkButton(self, text="Thank You", width=70, command=speak_thanks)
        self.speak_button.place(x=800,y=510)

    # Cart and Total Section
        self.cart_label = ctk.CTkLabel(self, text="Cart", font=ctk.CTkFont(size=14, weight="bold"))
        self.cart_label.place(x=500, y=10)

        self.cart_box = ctk.CTkTextbox(self, height=120, width=250)
        self.cart_box.place(x=400, y=50)

        self.total_label = ctk.CTkLabel(self, text="Total: ₱0.00", font=ctk.CTkFont(size=12, weight="bold"))
        self.total_label.place(x=480, y=200)

        

    # Add Items to Cart Buttons
        self.cart = []
        self.total = 0

        # Define button positions (adjust x, y as needed)
        button_positions = [
            (300, 250),
            (300, 300),
            (300, 350),
            (300, 400),
            (300, 450),
            (500, 250),
            (500, 300),
            (500, 350),
            (500, 400),
        ]

        # Create buttons for each menu item
        for (index, (item, price)), (x, y) in zip(enumerate(menu.items(), start=1), button_positions):
            btn = ctk.CTkButton(
                self,
                text=f"Add {item}",
                command=lambda i=item, p=price: self.add_to_cart(i, p),
                width=140,  # Adjust button width
            )
            btn.place(x=x, y=y)  # Place button at custom position

    # --- Add Items to Cart ---
    def add_to_cart(self, item, price):
        self.cart.append(item)
        self.cart_box.insert("end", f"{item}\n")
        self.total += price
        self.total_label.configure(text=f"Total: ₱{self.total:.2f}")

    # --- Clear Cart Button ---
        self.clear_cart_button = ctk.CTkButton(self, text="Clear Cart", command=self.clear_cart, width=140)
        self.clear_cart_button.place(x=450, y=600)  # Place clear button at a desired position
    
    # --- Clear Cart ---
    def clear_cart(self):
        self.cart.clear()  # Clear the cart list
        self.cart_box.delete(1.0, "end")  # Clear the cart display
        self.total = 0  # Reset total
        self.total_label.configure(text="Total: ₱0.00")  # Update total label

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