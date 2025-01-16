import tkinter as tk
from tkinter import scrolledtext
import subprocess
import threading

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Your Friendly AI Chat Companion")
        self.root.geometry("500x600") 
        self.root.configure(bg="#2c2f33")

        self.header = tk.Label(
            self.root,
            text="Let's Chat!",
            font=("Arial", 14, "bold"),
            bg="#23272a",
            fg="#7289da",
            pady=8
        )
        self.header.pack(fill="x")

        self.chat_display = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            width=45,  
            height=20,
            font=("Arial", 11),
            bg="#23272a",
            fg="#ffffff",
            padx=10,
            pady=10,
            state="disabled",
            relief=tk.FLAT,
            borderwidth=5
        )
        self.chat_display.pack(pady=10, padx=10, expand=True, fill="both")

        self.input_frame = tk.Frame(self.root, bg="#2c2f33")
        self.input_frame.pack(fill="x", pady=10)

        self.input_field = tk.Entry(
            self.input_frame,
            font=("Arial", 12),
            bg="#23272a",
            fg="#ffffff",
            insertbackground="#ffffff",
            relief=tk.FLAT,
            borderwidth=5,
            highlightbackground="#7289da",
            highlightthickness=2
        )
        self.input_field.pack(side=tk.LEFT, fill="x", expand=True, padx=(10, 5), pady=5)

        self.send_button = tk.Button(
            self.input_frame,
            text="Chat →", 
            command=self.send_message,
            font=("Arial", 11, "bold"),
            bg="#7289da",
            fg="#ffffff",
            activebackground="#5b6eae",
            activeforeground="#ffffff",
            relief=tk.FLAT,
            padx=12,
            pady=4
        )
        self.send_button.pack(side=tk.RIGHT, padx=(5, 10), pady=5)

        self.input_field.bind("<Return>", lambda event: self.send_message())

        self.display_bot_message("Hi there! 👋 I'm your AI friend powered by Phi-3. What's on your mind?")

    def chat_with_ollama(self, prompt):
        try:
            result = subprocess.run(
                ['ollama', 'run', 'phi3:mini'],
                input=prompt,
                text=True,
                capture_output=True,
                encoding='utf-8'
            )

            response = result.stdout.strip()
            return response if response else "Oops! I'm drawing a blank. Could you rephrase that?"

        except Exception as e:
            return "Something went wrong on my end. Mind trying again?"

    def send_message(self):
        user_message = self.input_field.get().strip()
        if not user_message:
            return

        self.input_field.delete(0, tk.END)
        self.display_user_message(user_message)
        
        threading.Thread(target=self.process_message, args=(user_message,)).start()

    def process_message(self, user_message):
        bot_response = self.chat_with_ollama(user_message)
        self.display_bot_message(bot_response)

    def display_user_message(self, message):
        self.chat_display.configure(state="normal")
        self.chat_display.insert(tk.END, f"You: {message}\n", ("user"))
        self.chat_display.insert(tk.END, "\n")
        self.chat_display.tag_config("user", foreground="#43b581")
        self.chat_display.configure(state="disabled")
        self.chat_display.see(tk.END)

    def display_bot_message(self, message):
        self.chat_display.configure(state="normal")
        self.chat_display.insert(tk.END, f"AI Friend: {message}\n", ("bot"))  
        self.chat_display.tag_config("bot", foreground="#7289da")
        self.chat_display.configure(state="disabled")
        self.chat_display.see(tk.END)

def main():
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()