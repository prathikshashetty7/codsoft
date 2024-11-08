import tkinter as tk
from PIL import Image, ImageTk  
import random

# Initializing score variables
user_score = 0
computer_score = 0

# Function to play the game
def play_game(user_choice):
    global user_score, computer_score
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    # Updating the result and score labels
    label_result.config(
        text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\nResult: {result}",
        fg="black", font=("Times New Roman", 12, "bold")
    )
    label_score.config(text="Score", fg="black", font=("Times New Roman", 14, "bold"))
    label_individual_scores.config(
        text=f"You: {user_score}   Computer: {computer_score}",
        fg="black", font=("Times New Roman", 12)
    )

    # Showing "Try Again" button 
    try_again_button.pack(pady=10)

# Function to reset the result display for a new round
def reset_game():
    label_result.config(text="Make your choice!")
    try_again_button.pack_forget()

# Initialize the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x500")
root.configure(bg="#efd7f3")  #background color

# Heading
label_heading = tk.Label(root, text="Rock-Paper-Scissors", bg="#efd7f3", fg="#333333", font=("Times New Roman", 18, "bold"))
label_heading.pack(pady=15)

# Centered score title
label_score = tk.Label(root, text="Score", bg="#efd7f3", fg="black", font=("Times New Roman", 14, "bold"))
label_score.pack(pady=5)

# Individual scores for user and computer below the score title
label_individual_scores = tk.Label(root, text="You: 0   Computer: 0", bg="#efd7f3", fg="black", font=("Times New Roman", 12))
label_individual_scores.pack(pady=5)

# Sticker (image) choices for Rock, Paper, Scissors
button_frame = tk.Frame(root, bg="#efd7f3")
button_frame.pack(pady=10)

# Load images
rock_img = ImageTk.PhotoImage(Image.open("rock.png").resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100)))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png").resize((100, 100)))

# Creating buttons with stickers
rock_button = tk.Button(button_frame, image=rock_img, command=lambda: play_game("Rock"), bg="#efd7f3", relief="flat")
rock_button.pack(side="left", padx=10)

paper_button = tk.Button(button_frame, image=paper_img, command=lambda: play_game("Paper"), bg="#efd7f3", relief="flat")
paper_button.pack(side="left", padx=10)

scissors_button = tk.Button(button_frame, image=scissors_img, command=lambda: play_game("Scissors"), bg="#efd7f3", relief="flat")
scissors_button.pack(side="left", padx=10)

# Label to display the result
label_result = tk.Label(root, text="Make your choice!", bg="#efd7f3", font=("Times New Roman", 12, "bold"), fg="black")
label_result.pack(pady=20)

# "Try Again" button to reset the game
try_again_button = tk.Button(root, text="Try Again", command=reset_game, bg="#4CAF50", fg="white", font=("Times New Roman", 12, "bold"))
try_again_button.pack_forget()  # Hide initially

# Start the main loop
root.mainloop()
