import tkinter as tk
from tkinter import scrolledtext


def get_response(user_input):
    """Processes user input using if-elif logic and returns a predefined reply."""
    clean_input = user_input.strip().lower()

    if clean_input in ["hello", "hi", "hey"]:
        return "Hi! How can I help you today😀?"
    elif clean_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks for asking🥰! How are you doing?"
    elif clean_input in ["what is your name", "what's your name?", "who are you"]:
        return "I am a simple rule-based chatbot!"
    elif clean_input in ["bye", "goodbye", "exit"]:
            return "Goodbye😊! Have a great day!"
    else:
        return "I'm sorry😥, I don't understand that. Try saying 'hello', 'how are you', or 'bye'."



class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Rule-Based Chatbot")
        self.root.geometry("400x500")
        self.root.configure(bg="#2c3e50")

        header = tk.Label(
            root,
            text="ChatBot v1.0",
            font=("Helvetica", 14, "bold"),
            bg="#34495e",
            fg="#ecf0f1",
            pady=10
        )
        header.pack(fill=tk.X)

       
        self.chat_area = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            state="disabled",
            font=("Helvetica", 10),
            bg="#ecf0f1",
            fg="#2c3e50"
        )
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        
        input_frame = tk.Frame(root, bg="#2c3e50")
        input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        self.entry_field = tk.Entry(
            input_frame,
            font=("Helvetica", 11),
            bg="#ffffff",
            fg="#2c3e50"
        )
        self.entry_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.entry_field.bind("<Return>", self.send_message)  # Press Enter to send

       
        send_button = tk.Button(
            input_frame,
            text="Send",
            font=("Helvetica", 10, "bold"),
            bg="#2980b9",
            fg="#ffffff",
            activebackground="#3498db",
            activeforeground="#ffffff",
            relief=tk.FLAT,
            command=self.send_message
        )
        send_button.pack(side=tk.RIGHT)

        
        self.append_message("Bot", "Hello! Type 'hello', 'how are you', or 'bye'.")

    def send_message(self, event=None):
        """Triggered when clicking Send or pressing Enter."""
        user_text = self.entry_field.get().strip()
        if not user_text:
            return

        
        self.entry_field.delete(0, tk.END)

         
        self.append_message("You", user_text)

        
        bot_reply = get_response(user_text)
        self.append_message("Bot", bot_reply)

        if user_text.lower() in ["bye", "goodbye", "exit"]:
            self.root.after(1500, self.root.destroy)

    def append_message(self, sender, text):
        """Appends formatted messages to the chat window."""
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, f"{sender}: {text}\n\n")
        self.chat_area.see(tk.END)  # Auto-scroll to bottom
        self.chat_area.config(state="disabled")



if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()