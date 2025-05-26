import tkinter as tk
import random

# Initialize main window
root = tk.Tk()
root.title("Rock, Paper, Scissors - Yellow Theme")
root.geometry("520x480")
root.configure(bg="#fff89a")  # Light yellow background
root.resizable(False, False)

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0
history = []

# Function to play the game
def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(choices)

    user_choice_label.config(text=f"Your choice: {user_choice}")
    computer_choice_label.config(text=f"Computer's choice: {computer_choice}")

    if user_choice == computer_choice:
        result = "Draw"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win"
        user_score += 1
    else:
        result = "You Lose"
        computer_score += 1

    result_label.config(text=f"Result: {result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

    history.append(f"You: {user_choice}, Computer: {computer_choice} → {result}")
    update_history()

# Function to update history display
def update_history():
    history_text.delete(1.0, tk.END)
    for entry in history[-10:]:
        history_text.insert(tk.END, entry + "\n")

# Title
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 20, "bold"), bg="#fff89a", fg="#cc9900")
title_label.pack(pady=10)

# Button Frame
button_frame = tk.Frame(root, bg="#fff89a")
button_frame.pack(pady=10)

btn_style = {"width": 12, "height": 2, "font": ("Arial", 12), "bg": "#ffeb3b", "fg": "black", "activebackground": "#fdd835"}

rock_btn = tk.Button(button_frame, text="Rock", command=lambda: play("Rock"), **btn_style)
paper_btn = tk.Button(button_frame, text="Paper", command=lambda: play("Paper"), **btn_style)
scissors_btn = tk.Button(button_frame, text="Scissors", command=lambda: play("Scissors"), **btn_style)

rock_btn.grid(row=0, column=0, padx=10)
paper_btn.grid(row=0, column=1, padx=10)
scissors_btn.grid(row=0, column=2, padx=10)

# Labels
user_choice_label = tk.Label(root, text="Your choice: ", font=("Arial", 12), bg="#fff89a")
user_choice_label.pack()

computer_choice_label = tk.Label(root, text="Computer's choice: ", font=("Arial", 12), bg="#fff89a")
computer_choice_label.pack()

result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"), bg="#fff89a", fg="#cc6600")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12), bg="#fff89a", fg="#444")
score_label.pack(pady=5)

# Game History
history_label = tk.Label(root, text="Game History (last 10):", font=("Arial", 12, "bold"), bg="#fff89a", fg="#444")
history_label.pack(pady=5)

history_text = tk.Text(root, height=6, width=55, font=("Courier", 10), bg="#fffde7")
history_text.pack(pady=5)

#Start the GUI loop

root.mainloop()