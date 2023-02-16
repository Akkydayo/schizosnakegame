import tkinter as tk
import subprocess

def start_game():
    subprocess.call ('python matopeli.py')

def view_highscores():
    pass

def view_instructions():
    # Define the actions that will be taken when the user clicks the view instructions button.
    pass

def view_settings():
    pass

def exit_program():
    # Define the actions that will be taken when the user clicks the exit button.
    root.destroy()

# Create a new tkinter window.
root = tk.Tk()
root.title("They are listening")

# Add a title label to the window.
title_label = tk.Label(root, text="Schizo Snake Game", font=("Arial", 24))
title_label.pack(pady=20)

# Create buttons for starting the game, viewing instructions, and exiting the program.
start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=10)

instructions_button = tk.Button(root, text="View Instructions", command=view_instructions)
instructions_button.pack(pady=10)

highscores_button = tk.Button(root, text="Highscores", command=view_highscores)
highscores_button.pack(pady=10)

settings_button = tk.Button(root, text="Settings", command=view_settings)
settings_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.pack(pady=10)

# Display the window.
root.mainloop()