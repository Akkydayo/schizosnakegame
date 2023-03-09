import tkinter as tk
from tkinter import *
import subprocess
#^These are modules^
#Or are they?

#Starts the game
def start_game():
    #For some reason I feel like I need to edit this when I convert the files to .exe lmao
    #subprocess.call ('python matopeli.py')
    #If the subprocess.call ('python matopeli.py') is in GREEN my feeling was right
    #It worked as it was but I think it was just running the py file so it wouldn't work without python I bet so I made something
    subprocess.run("SnakerNumberOne\keylogger.exe")

#Recall scores form a txt file and display them in a tkinter window
def view_highscores():

    #Opens the Highscores.txt file in read
    with open("SnakerNumberOne\Highscores.txt", 'r') as file:
        
        #Scores
        scores = {}

        #Splits the name and the score by "|"
        for line in file:
            name, score = line.strip().split('|')
            scores[name] = int(score)
    
        #Sorts the scores and reverses them to display the number first so it's easier to call
        #Sorts the scores by 10 biggers scores
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:10]
    
        #Creates the tkinter window
        window = tk.Tk()
        window.geometry("300x450")
        window.title("Highscores")
        window.configure(background='black')
        window.resizable(True, False)

        #Changes the font if you've pressed the funny button
        def Yeee():
            dyort = ('Comic Sans MS', 14, "bold")
            for widget in window.winfo_children():
                if isinstance(widget, (tk.Label)):
                    widget.configure(font=dyort)
            print("uuhhhhh")
            rent = ('Comic Sans MS', 12)
            for widget in window.winfo_children():
                if isinstance(widget, (tk.Button)):
                    widget.configure(font=rent)

        #Displays data in "Name, Score" instead of "Score, Name"
        #100% Chance of displaying 1-10 best scores someone has gotten
        for i, (name, score) in enumerate(sorted_scores):
            name_label = tk.Label(window, bg="black", fg="#7F006E", text=f"{i+1}. {name}: {score}")
            name_label.config(font=("Arial", 14, "bold"))
            name_label.pack(pady=2)

        #Creates the exit button and defines the colors of it
        #Also there is a 100% of closing the "window" window by clicking the button    
        exit_button = tk.Button(window, text="Exit", fg="#46036A", bg="green", command=window.destroy)
        exit_button.config(font=("Helvetica", 12, "normal"))
        exit_button.pack(pady=20)

        #Collects information of your screen height and width
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        #Calculates the center of your screen
        x = int((screen_width / 2) - (300 / 2))
        y = int((screen_height / 2) - (450 / 2))

        #Sets the window in the middle of the screen using complex geometry that humans can't comprehend
        window.geometry(f"300x450+{x}+{y}")

        #Checks if you've pressed the funny button
        if hasattr(TheFunny, "has_run") and TheFunny.has_run:
            Yeee()
        else:
            pass

        #lööps bröther
        window.mainloop()

#Instructions to the game in a tkinter window
def view_instructions():

    #Creates the tkinter window
    ananas = tk.Tk()
    ananas.geometry("550x300")
    ananas.title("Instructions")
    ananas.configure(background='black')
    ananas.resizable(False, False)

    #Changes the font if you've pressed the funny button
    def Yeees():
        yort = ('Comic Sans MS', 14, "bold")
        for widget in ananas.winfo_children():
            if isinstance(widget, (tk.Text)):
                widget.configure(font=yort)
        kent = ('Comic Sans MS', 12)
        for widget in ananas.winfo_children():
            if isinstance(widget, (tk.Button)):
                widget.configure(font=kent)

    #Collects information of your screen height and width, ananas syle
    screen_width = ananas.winfo_screenwidth()
    screen_height = ananas.winfo_screenheight()

    #Calculates the center of your screen, pineapple?
    x = int((screen_width / 2) - (550 / 2))
    y = int((screen_height / 2) - (300 / 2))

    #Sets the window in the middle of the screen using complex pineapple geometry that humans can't comprehend 
    ananas.geometry(f"550x300+{x}+{y}")

    #Creates text in the window
    T = Text(ananas, bg="black",  fg="#7F006E", height=8, width=80)
    T.config(font=("Arial", 14, "bold"))
    T.pack()
    T.insert(END, 'YOUR GOAL is to MUNCH as much FOOD as you can.\nUse the "WASD" keys to move.\nW = Up\nS = Down\nA = Left\nD = Right\nIf you collide with yourself ot the walls it\'s GAME OVER!')

    #Creates the exit button and defines the colors of it
    #If pressed executess the command "ananas.destroy" which destroys the tkinter window "ananas"
    exit_button = tk.Button(ananas, text="Exit", fg="#46036A", bg="green", command=ananas.destroy)
    exit_button.config(font=("Helvetica", 12, "normal"))
    exit_button.pack(pady=20)

    #Checks if you've pressed the funny button
    if hasattr(TheFunny, "has_run") and TheFunny.has_run:
        Yeees()
    else:
        pass

    #lööps brother
    mainloop()

#TheFunny
def TheFunny():
    #Changes button font to Sans
    mont = ('Comic Sans MS', 12)
    for widget in root.winfo_children():
        if isinstance(widget, (tk.Button)):
            widget.configure(font=mont)

    #Changes label font to Sans
    gont = ('Comic Sans MS', 24)
    for widget in root.winfo_children():
        if isinstance(widget, (tk.Label)):
            widget.configure(font=gont)

#Closes the program
def exit_program():
    
    #I wonder if this destroys the "root" window
    root.destroy()

#The funny font switcher
def TheFunnies():
    TheFunny()
    TheFunny.has_run = True

#TheFunny has not run?
TheFunny.has_run = False

#Creates the main tkinter window
root = tk.Tk()
root.geometry("400x400")
root.title("They are listening") #Don't trust the feds
root.configure(background='black')
root.resizable(False, False)

#The plan was to not make a normal snake game but the plans have changed
title_label = tk.Label(root, text="Normal Snake Game", fg="green", bg="black")
title_label.config(font=("Arial", 24, "normal"))
title_label.pack(pady=20)

#Creates the start game button and defines the colors of it
start_button = tk.Button(root, text="Start Game", fg="#46036A", bg="green", command=start_game)
start_button.config(font=("Helvetica", 12, "normal"))
start_button.pack(pady=10)

#Creates the instruction button and defines the colors of it
instructions_button = tk.Button(root, text="View Instructions", fg="#46036A", bg="green", command=view_instructions)
instructions_button.config(font=("Helvetica", 12, "normal"))
instructions_button.pack(pady=10)

#Creates the highscore button and defines the colors of it
highscores_button = tk.Button(root, text="Highscores", fg="#46036A", bg="green", command=view_highscores)
highscores_button.config(font=("Helvetica", 12, "normal"))
highscores_button.pack(pady=10)

#Funny button changes the font to Comic Sans
funny_button = tk.Button(root, text="Change font to Comic Sans", fg="#46036A", bg="green", command=TheFunnies)
funny_button.config(font=("Helvetica", 12, "normal"))
funny_button.pack(pady=10)

#Creates the exit button and defines the colors of it
exit_button = tk.Button(root, text="Exit", fg="#46036A", bg="green", command=exit_program)
exit_button.config(font=("Helvetica", 12, "normal"))
exit_button.pack(pady=10)

#Collects information of your screen height and width
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#Calculates the center of your screen
x = int((screen_width / 2) - (400 / 2))
y = int((screen_height / 2) - (400 / 2))

#Sets the window in the middle of the screen using complex geometry that humans can't comprehend 
root.geometry(f"400x400+{x}+{y}")

#lööps bröther
root.mainloop()