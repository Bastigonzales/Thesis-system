
import tkinter as tk
from RealtimeSTT import AudioToTextRecorder
 
class SpeechToTextGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Speech to Text")
        self.geometry("900x500")
        self.recorder = AudioToTextRecorder(spinner=False, model="small.en", language="en")
 
        self.text_widget = tk.Text(self, height=20, width=50)
        self.text_widget.pack(pady=10)
 
        self.start_button = tk.Button(self, text="Speak", command=self.start_transcription)
        self.start_button.pack(side="left", padx=10)
 
        self.stop_button = tk.Button(self, text="Stop", command=self.stop_transcription)
        self.stop_button.pack(side="right", padx=10)
 
    def start_transcription(self):
        print("start pressed")
        if self.recorder:
            print("starting recording")
            self.recorder.start()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
 
    def update_text(self, text):
        self.text_widget.insert(tk.END, text)
        self.text_widget.see(tk.END)
 
    def stop_transcription(self):
        if self.recorder:
            self.recorder.stop()
            text = self.recorder.text()
            self.update_text(text)
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
 
if __name__ == "__main__":
    root = SpeechToTextGUI()
    root.mainloop()
