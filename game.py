import tkinter as tk
import subprocess

def start_game():
    subprocess.call ('python matopeli.py')

def view_highscores():

    with open('Highscores.txt', 'r') as file:
        
        scores = {}
    
        for line in file:
            name, score = line.strip().split('|')
            scores[name] = int(score)
    
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:10]
    
        window = tk.Tk()
        window.geometry("200x300")
        window.title("Highscores")
    
        for i, (name, score) in enumerate(sorted_scores):
            name_label = tk.Label(window, text=f"{i+1}. {name}: {score}")
            name_label.pack()

        window.mainloop()

def view_instructions():
    # Define the actions that will be taken when the user clicks the view instructions button.
    pass

def exit_program():
    
    root.destroy()

root = tk.Tk()
root.title("They are listening")

title_label = tk.Label(root, text="Normal Snake Game", font=("Arial", 24))
title_label.pack(pady=20)

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=10)

instructions_button = tk.Button(root, text="View Instructions", command=view_instructions)
instructions_button.pack(pady=10)

highscores_button = tk.Button(root, text="Highscores", command=view_highscores)
highscores_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_program)
exit_button.pack(pady=10)

root.mainloop()