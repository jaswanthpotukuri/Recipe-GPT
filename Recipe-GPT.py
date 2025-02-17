import google.generativeai as ai
import os
import tkinter as tk
from tkinter import scrolledtext, Frame

# API KEY
API_KEY = 'AIzaSyDWXiY-rGSWTJwQmoB8C3UF1jbzxj3Z24o'

# Configure the API
ai.configure(api_key=API_KEY)

# Create a new model
model = ai.GenerativeModel("gemini-pro")
chat = model.start_chat()

def send_message():
    user_message = entry.get().strip()
    if not user_message:
        return
    
    chat_display.insert(tk.END, f"\nYou: {user_message}\n", "user")
    entry.delete(0, tk.END)
    
    prompt = f"You are Recipe GPT, an AI assistant that provides cooking tips and recipes. Answer the following query accordingly: {user_message}"
    response = chat.send_message(prompt)
    chat_display.insert(tk.END, f"Chef: {response.text}\n", "bot")

def clear_chat():
    chat_display.delete(1.0, tk.END)

def exit_app():
    root.quit()

# Creating GUI window
root = tk.Tk()
root.title("Recipe GPT - Your AI Cooking Assistant")
root.geometry("1000x650")
root.configure(bg="#FFE4B5")

# Main Frame
main_frame = Frame(root, bg="#FFFFFF", padx=20, pady=20, relief=tk.GROOVE, bd=3)
main_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# Title and Caption
title_label = tk.Label(main_frame, text="Recipe GPT", font=("Comic Sans MS", 30, "bold"), fg="#D2691E", bg="#FFFFFF")
title_label.pack(pady=5)
caption_label = tk.Label(main_frame, text="Your AI-powered recipe assistant. Ask me anything about cooking!", font=("Verdana", 14), fg="#8B4513", bg="#FFFFFF")
caption_label.pack(pady=5)

# Chat Display Area
chat_display = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=90, height=20, bg="#FFF8DC", fg="#2c3e50", font=("Courier New", 12), relief=tk.FLAT)
chat_display.pack(pady=10)
chat_display.tag_config("user", foreground="#8B0000", font=("Courier New", 12, "bold"))
chat_display.tag_config("bot", foreground="#228B22", font=("Courier New", 12, ))

# Entry Box and Buttons
entry_frame = tk.Frame(main_frame, bg="#FFFFFF")
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, width=60, font=("Georgia", 14), bd=2, relief=tk.GROOVE)
entry.grid(row=0, column=0, padx=5)
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(entry_frame, text="Send", command=send_message, bg="#32CD32", fg="white", font=("Tahoma", 12, "bold"), padx=15, pady=8, relief=tk.RAISED)
send_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(entry_frame, text="Clear", command=clear_chat, bg="#FF6347", fg="white", font=("Tahoma", 12, "bold"), padx=15, pady=8, relief=tk.RAISED)
clear_button.grid(row=0, column=2, padx=5)

exit_button = tk.Button(entry_frame, text="Exit", command=exit_app, bg="#696969", fg="white", font=("Tahoma", 12, "bold"), padx=15, pady=8, relief=tk.RAISED)
exit_button.grid(row=0, column=3, padx=5)

root.mainloop()


