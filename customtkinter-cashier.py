import customtkinter as ctk
import pyttsx3
from RealtimeSTT import AudioToTextRecorder

# Menu items
menu = {
    "Tonyo's Special Lugaw": 3.00,
    "Longsilog": 129.00,
    "Tapsilog": 129.00,
    "Tocilog": 129.00,
    "Pansit bihon (Regular)": 189.00,
    "Lumpiang Shanghai (20pcs)": 269.00,
    "Coke Can": 75.05,
    "Iced tea": 80.00,
    "Halo-Halo": 120.00,
}

# Initialize TTS engine
tts_engine = pyttsx3.init()

# Text-to-Speech functions
def speak_text(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.title("Speech to Text - Text to Speech - Menu Concession")
        self.geometry("1200x600")

        # Initialize the audio-to-text recorder
        self.recorder = AudioToTextRecorder(spinner=False, model="small.en", language="en")

        # --- Left-Side Menu ---
        self.left_frame = ctk.CTkFrame(self, width=200, corner_radius=10)
        self.left_frame.pack(side="left", fill="y", padx=10, pady=10)

        self.menu_label = ctk.CTkLabel(self.left_frame, text="Menu", font=ctk.CTkFont(size=14, weight="bold"))
        self.menu_label.pack(pady=10)

        for index, (item, price) in enumerate(menu.items(), start=1):
            menu_item_label = ctk.CTkLabel(self.left_frame, text=f"{index}. {item} - ₱{price:.2f}")
            menu_item_label.pack(anchor="w", padx=10, pady=2)

        # --- Right-Side Content ---
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Cart and Total Section
        self.cart_label = ctk.CTkLabel(self.main_frame, text="Cart", font=ctk.CTkFont(size=14, weight="bold"))
        self.cart_label.pack(anchor="nw", pady=10)

        self.cart_box = ctk.CTkTextbox(self.main_frame, height=250, width=400)
        self.cart_box.pack(pady=10)

        self.total_label = ctk.CTkLabel(self.main_frame, text="Total: ₱0.00", font=ctk.CTkFont(size=12))
        self.total_label.pack(anchor="nw", pady=10)

        # Add Items to Cart Buttons
        self.cart = []
        self.total = 0
        for index, (item, price) in enumerate(menu.items(), start=1):
            btn = ctk.CTkButton(self.main_frame, text=f"Add {item}", command=lambda i=item, p=price: self.add_to_cart(i, p))
            btn.pack(pady=2)

        # Speech-to-Text Section
        self.text_widget = ctk.CTkTextbox(self.main_frame, height=120, width=250)
        self.text_widget.place(x=600, y=20)

        self.start_button = ctk.CTkButton(self.main_frame, text="Speak", width=50, command=self.start_transcription)
        self.start_button.place(x=600, y=200)

        self.stop_button = ctk.CTkButton(self.main_frame, text="Stop", width=50, command=self.stop_transcription)
        self.stop_button.place(x=700, y=220)
        self.stop_button.configure(state=ctk.DISABLED)

        # Text-to-Speech Buttons
        self.tts_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        self.tts_frame.pack(pady=20)

        self.speak_buttons = [
            ("Hello", "Hello!"),
            ("Good Morning", "Good Morning!"),
            ("Good Afternoon", "Good Afternoon!"),
            ("Good Evening", "Good Evening!"),
            ("How May I Help You?", "How May I Help You?"),
            ("Do You Want to Add Anything?", "Do You Want to Add Anything?"),
            ("Thank You", "Thank you!"),
        ]

        for text, message in self.speak_buttons:
            btn = ctk.CTkButton(self.tts_frame, text=text, width=200, command=lambda m=message: speak_text(m))
            btn.pack(pady=5)

    # --- Add Items to Cart ---
    def add_to_cart(self, item, price):
        self.cart.append(item)
        self.cart_box.insert("end", f"{item}\n")
        self.total += price
        self.total_label.configure(text=f"Total: ₱{self.total:.2f}")

    # --- Speech-to-Text Methods ---
    def start_transcription(self):
        if self.recorder:
            self.recorder.start()
            self.start_button.configure(state=ctk.DISABLED)
            self.stop_button.configure(state=ctk.NORMAL)

    def stop_transcription(self):
        if self.recorder:
            self.recorder.stop()
            text = self.recorder.text()
            self.update_text(text)
            self.start_button.configure(state=ctk.NORMAL)
            self.stop_button.configure(state=ctk.DISABLED)

    def update_text(self, text):
        self.text_widget.insert(ctk.END, text)
        self.text_widget.see(ctk.END)

# Run the application
if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    app = App()
    app.mainloop()
