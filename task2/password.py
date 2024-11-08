import tkinter as tk
import random
import string
import tkinter.messagebox as messagebox

def generate_password():
    try:
        length = int(entry_length.get())
        if length < 6:
            # Show error popup message if length is less than 6
            messagebox.showerror("Error", "Password length must be at least 6 characters")
            return

        # Determine character set based on selected complexity
        complexity = complexity_var.get()
        if complexity == "Easy":
            characters = string.ascii_lowercase
        elif complexity == "Medium":
            characters = string.ascii_letters  # Uppercase + Lowercase
        elif complexity == "Strong":
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            label_result.config(text="Error: Select a complexity level")
            return

        # Generate password
        password = ''.join(random.choice(characters) for _ in range(length))
        label_result.config(text="Generated Password: " + password)
    except ValueError:
        label_result.config(text="Error: Enter a valid length")

# Initialize the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.configure(bg="#efd7f3")

# Title label at the top
label_title = tk.Label(root, text="Password Generator", bg="#efd7f3", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

# Password length input (label and textbox adjacent)
frame_length = tk.Frame(root, bg="#efd7f3")
frame_length.pack(pady=10)

label_length = tk.Label(frame_length, text="Password Length:", bg="#efd7f3", font=("Arial", 12))
label_length.pack(side="left", padx=10)

entry_length = tk.Entry(frame_length, width=10)
entry_length.pack(side="left")

# Password complexity selection (centered)
label_complexity = tk.Label(root, text="Select Complexity:", bg="#efd7f3", font=("Arial", 12))
label_complexity.pack(pady=5)

frame_radio_buttons = tk.Frame(root, bg="#efd7f3")
frame_radio_buttons.pack(pady=5)

complexity_var = tk.StringVar(value="Medium")  # Default to Medium complexity

radio_easy = tk.Radiobutton(frame_radio_buttons, text="Easy (Lowercase)", variable=complexity_var, value="Easy", bg="#efd7f3", font=("Arial", 10))
radio_easy.pack(side="left", padx=20)

radio_medium = tk.Radiobutton(frame_radio_buttons, text="Medium (Upper + Lower)", variable=complexity_var, value="Medium", bg="#efd7f3", font=("Arial", 10))
radio_medium.pack(side="left", padx=20)

radio_strong = tk.Radiobutton(frame_radio_buttons, text="Strong (Upper + Lower + Digits + Symbols)", variable=complexity_var, value="Strong", bg="#efd7f3", font=("Arial", 10))
radio_strong.pack(side="left", padx=20)

# Button to generate password
button_generate = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
button_generate.pack(pady=15)

# Label to display the result
label_result = tk.Label(root, text="Generated Password: ", bg="#efd7f3", font=("Arial", 12, "bold"))
label_result.pack(pady=5)

root.mainloop()
