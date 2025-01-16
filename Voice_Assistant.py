import tkinter as tk
from tkinter import scrolledtext
import pyttsx3
import speech_recognition as sr
import threading
import webbrowser
import subprocess
import wikipedia
import os
import time
from datetime import datetime
import platform

class VoiceAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Your Voice Assistant")
        self.root.geometry("500x600")
        self.root.configure(bg="#2c2f33")
        
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 180)
        
        self.header = tk.Label(
            self.root,
            text="Hey! I'm listening...",
            font=("Arial", 14, "bold"),
            bg="#23272a",
            fg="#7289da",
            pady=8
        )
        self.header.pack(fill="x")
        
        self.chat_area = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            width=45,
            height=25,
            font=("Arial", 11),
            bg="#23272a",
            fg="#ffffff",
            padx=10,
            pady=10
        )
        self.chat_area.pack(pady=10, padx=10, expand=True, fill="both")
        
        self.button_frame = tk.Frame(self.root, bg="#2c2f33")
        self.button_frame.pack(fill="x", pady=10)
        
        self.listen_button = tk.Button(
            self.button_frame,
            text="Start Listening",
            command=self.start_listening,
            font=("Arial", 11),
            bg="#7289da",
            fg="white",
            padx=20
        )
        self.listen_button.pack(side=tk.LEFT, padx=10)
        
        self.quit_button = tk.Button(
            self.button_frame,
            text="Quit",
            command=self.quit_app,
            font=("Arial", 11),
            bg="#ff4c4c",
            fg="white",
            padx=20
        )
        self.quit_button.pack(side=tk.RIGHT, padx=10)
        
        self.speak_and_display("Hi! I'm your voice assistant. Try saying 'help' to see what I can do!")
        
        self.listening = False

    def speak_and_display(self, text, is_user=False):
        self.chat_area.insert(tk.END, f"{'You' if is_user else 'Assistant'}: {text}\n\n")
        self.chat_area.see(tk.END)
        
        if not is_user:
            self.engine.say(text)
            self.engine.runAndWait()

    def listen_for_command(self):
        recognizer = sr.Recognizer()
        
        while self.listening:
            try:
                with sr.Microphone() as source:
                    self.header.config(text="Listening...")
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    
                self.header.config(text="Processing...")
                command = recognizer.recognize_google(audio).lower()
                self.speak_and_display(command, is_user=True)
                self.process_command(command)
                
            except sr.WaitTimeoutError:
                self.header.config(text="Hey! I'm listening...")
            except sr.UnknownValueError:
                pass
            except Exception as e:
                self.header.config(text="Hey! I'm listening...")
                print(f"Error: {str(e)}")

    def process_command(self, command):
        if 'help' in command:
            help_text = """
            Here's what I can do:
            - Search Wikipedia (say 'wiki' followed by your search)
            - Open YouTube (say 'open youtube')
            - Search on YouTube (say 'search youtube' followed by topic)
            - Adjust Volume ('increase volume' or 'decrease volume')
            - Lock your system ('lock system')
            - Shutdown or restart your system ('shutdown system' or 'restart system')
            - Check the time or date ('what time is it?' or 'what's the date today?')
            - Quit the assistant (say 'quit')
            """
            self.speak_and_display(help_text)

        elif 'wiki' in command:
            query = command.replace('wiki', '').strip()
            try:
                result = wikipedia.summary(query, sentences=2)
                self.speak_and_display(f"According to Wikipedia: {result}")
            except:
                self.speak_and_display("Sorry, couldn't find that on Wikipedia.")

        elif 'open youtube' in command:
            self.speak_and_display("Opening YouTube...")
            webbrowser.open('https://www.youtube.com')

        elif 'search youtube' in command:
            search_term = command.replace('search youtube', '').strip()
            self.speak_and_display(f"Searching YouTube for {search_term}")
            webbrowser.open(f'https://www.youtube.com/results?search_query={search_term}')

        elif 'increase volume' in command:
            os.system("nircmd.exe changesysvolume 2000")  # Requires NirCmd for Windows
            self.speak_and_display("Increasing volume.")

        elif 'decrease volume' in command:
            os.system("nircmd.exe changesysvolume -2000")  # Requires NirCmd for Windows
            self.speak_and_display("Decreasing volume.")

        elif 'lock system' in command:
            self.speak_and_display("Locking your system...")
            os.system("rundll32.exe user32.dll,LockWorkStation")

        elif 'shutdown system' in command:
            self.speak_and_display("Shutting down the system...")
            os.system("shutdown /s /t 0")

        elif 'restart system' in command:
            self.speak_and_display("Restarting the system...")
            os.system("shutdown /r /t 0")

        elif 'what time is it' in command:
            current_time = time.strftime("%I:%M %p")
            self.speak_and_display(f"The current time is {current_time}.")

        elif 'what\'s the date today' in command:
            today_date = datetime.now().strftime("%B %d, %Y")
            self.speak_and_display(f"Today's date is {today_date}.")

        elif 'quit' in command:
            self.quit_app()

        else:
            self.speak_and_display("Not sure about that. Say 'help' to see what I can do!")

    def start_listening(self):
        if not self.listening:
            self.listening = True
            self.listen_button.config(text="Stop Listening", bg="#ff4c4c")
            threading.Thread(target=self.listen_for_command, daemon=True).start()
        else:
            self.listening = False
            self.listen_button.config(text="Start Listening", bg="#7289da")
            self.header.config(text="Hey! I'm listening...")

    def quit_app(self):
        self.listening = False
        self.speak_and_display("Goodbye! Have a great day!")
        self.root.after(2000, self.root.destroy)

def main():
    root = tk.Tk()
    app = VoiceAssistantGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
