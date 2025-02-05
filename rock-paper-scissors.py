import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # For background images
import random

# Game choices
choices = ["Rock", "Paper", "Scissors"]


# Function to determine the winner
def get_winner(user_choice):
    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a Draw! 😐"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
            (user_choice == "Paper" and computer_choice == "Rock") or \
            (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "🎉 You Win!"
    else:
        result = "🤖 Computer Wins!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")


# Function to reset the game
def new_game():
    result_label.config(text="Make your choice!")


# Initialize main window
root = tk.Tk()
root.title("Rock Paper Scissors - Modern UI")
root.geometry("700x700")  # Increased window size to 700x700
root.resizable(False, False)

# Load background image
bg_image = Image.open("background.jpg")  # Use an actual image file
bg_image = bg_image.resize((700, 700), Image.LANCZOS)  # Fit background to window size
bg_photo = ImageTk.PhotoImage(bg_image)

# Background Label
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Title Label (transparent background, white text)
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), fg="white", bg="black", pady=5,
                       bd=0, highlightthickness=0)
title_label.pack(pady=15)

# Game Buttons Frame (transparent background)
button_frame = tk.Frame(root, bg=None)
button_frame.pack(pady=15)

# Styling for buttons (custom style to match background)
style = ttk.Style()
style.theme_use("clam")  # Use the 'clam' theme for better customization

# Configure button style
style.configure("TButton",
                font=("Arial", 12, "bold"),
                padding=10,
                relief="flat",  # Flat buttons
                background="#4CAF50",  # Green background
                foreground="white",  # White text
                borderwidth=0,
                focusthickness=3,
                focuscolor="#4CAF50")
style.map("TButton",
          background=[("active", "#45a049")],  # Darker green when active
          foreground=[("active", "white")])

# Create buttons
rock_btn = ttk.Button(button_frame, text="🪨 Rock", command=lambda: get_winner("Rock"), style="TButton")
rock_btn.grid(row=0, column=0, padx=10, pady=8, ipadx=8, ipady=4)

paper_btn = ttk.Button(button_frame, text="📄 Paper", command=lambda: get_winner("Paper"), style="TButton")
paper_btn.grid(row=0, column=1, padx=10, pady=8, ipadx=8, ipady=4)

scissors_btn = ttk.Button(button_frame, text="✂️ Scissors", command=lambda: get_winner("Scissors"), style="TButton")
scissors_btn.grid(row=0, column=2, padx=10, pady=8, ipadx=8, ipady=4)

# Result Label (transparent background, white text)
result_label = tk.Label(root, text="Make your choice!", font=("Arial", 16, "bold"), fg="white", bg="black", pady=15,
                        bd=0, highlightthickness=0)
result_label.pack()

# New Game Button (custom style)
new_game_btn = ttk.Button(root, text="🔄 New Game", command=new_game, style="TButton")
new_game_btn.pack(pady=25, ipadx=12, ipady=4)

# Run the Tkinter loop
root.mainloop()