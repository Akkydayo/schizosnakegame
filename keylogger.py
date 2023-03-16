import tkinter as tk
from tkinter import *
import random
import pygame
#^These are modules, probably^

#Game rules
GAME_WIDTH = 1000
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#64d86b"
FOOD_COLOR = "#8b0000"
BACKGROUND_COLOR = "#000000"

#Pygame mixer for your DJing needs
pygame.mixer.init()

#Loads the munch sound effect
sound_effect = pygame.mixer.Sound("SnakerNumberOne\Sounds\Munch.mp3")

#Snek
class Snake:
    
    #The snek
    def __init__(self):
        #Snek body
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        #Creates green squares that are the "Snake"
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

#Food
class Food:
    
    #The Food
    def __init__(self):

        #defines x and y as random coordinates in the playfield
        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        #very cool
        self.coordinates = [x, y]

        #Creates the food in a random place within the playfield
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

#Defines what gone happen when u do stuff u know
def next_turn(snake, food):

    #X and Y are snake coordinates in the new hit movie "Snake"
    x, y = snake.coordinates[0] 

    #if u go up u minus y
    if direction == "up":
        y -= SPACE_SIZE
    #if u go down u plus y
    elif direction == "down":
        y += SPACE_SIZE
    #if u go left u minus x
    elif direction == "left":
        x -= SPACE_SIZE
    #if u go right u plus x
    elif direction == "right":
        x += SPACE_SIZE
    
    #Inserts snake coordinates
    snake.coordinates.insert(0, (x,y))
    #Poor snake has the feds tracking his coordinates

    #Creates a new bodypart for tha snake when u move (because one gets deleted(high level programming amirite))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    #Now they are inserting bodyparts to the poor snake that are labeled as "square"
    snake.squares.insert(0, square)

    #Checks if u ate tha food
    if x == food.coordinates[0] and y == food.coordinates[1]:

        #Might be the global variable for score
        global score
        
        #Might play the sound effect while eating the food
        sound_effect.play()
        
        #100% chance of adding 1 score after consuming the red food(redpill??)
        score += 1

        #Configures the label depending on your score
        label.config(text="Score:{}".format(score))

        #Now the feds delete the poor snakes food
        canvas.delete("food")

        #I think food is Food also
        food = Food()

    #Or else
    else:
        #Delete snake coordinates? How nice of the feds
        del snake.coordinates[-1]

        #Deletes the Snake Squares on the canvas
        canvas.delete(snake.squares[-1])

        #I think this qualifies as animal torture and is a punishable crime
        del snake.squares[-1]

    #If a collision happens with tha snake it will run the definition "game_over"
    if check_collisions(snake):
        #100% of ending the game
        game_over()
    #Or else
    else:
        #Calls tha functions
        window.after(SPEED, next_turn, snake, food)

#High chance of defining the change of direction
def change_direction(new_direction):
    
    #The global variable of direction I believe
    global direction
    
    #if u ur new direction is left
    if new_direction == 'left':
        #if u were going right
        if direction != 'right':
            #u will now go towards the new_direction
            direction = new_direction
    #else if ur new direction is right
    elif new_direction == 'right':
        #and ur were going left
        if direction != 'left':
            #u will now go towards the new_direction
            direction = new_direction
    #else if ur new direction is up
    elif new_direction == 'up':
        #and ur were going down
        if direction != 'down':
            #u will now go towards the new_direction
            direction = new_direction
    #else if ur new direction is down
    elif new_direction == 'down':
        #and ur were going up
        if direction != 'up':
            #u will now go towards the new_direction
            direction = new_direction

#Defines the check of collisions with the snake
def check_collisions(snake):
    
    #They are tracking the coordinates of the snake again
    x, y = snake.coordinates[0]

    #Simon says that if you hit the edge of the playarea check_collisions returns True
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    #Simon says that if you run into yourself check_collisions returns True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
  
    #Simon says that if you don't collide check_collisions returns False
    return False

#Game Over
def game_over():

    #Deletes everything (muhahaha)
    canvas.delete(ALL)
    #Creates the huge "GAME OVER" text in the middle of the canvas
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/4,
                       font=('consolas',70), text="GAME OVER", fill="#64d86b", tag="gameover")            

    #Now this is interesting
    def printScore():
        #score is now playerScore
        playerScore = score
        #prints the playerScore
        print (f"{playerScore}")
        #name_entry.get is now name
        name = name_entry.get()
        #punishing all the goofy goobers trying to make the highscore.txt not open
        processed_name = name.replace ("|", "GoofyGoober")
        #print the name
        print (f"{processed_name}")
        #opens the highscores.txt file 
        with open("SnakerNumberOne\Highscores.txt", 'a', encoding = 'utf-8') as file:
            #writes the name and score of the player in the file with the special character "|" in between
            file.write(f'{processed_name}|{playerScore}\n')
        #Disables some button called "submit_button" or something
        submit_button["state"] = DISABLED

    #creates the tkineter window for game over
    game_over_screen = tk.Tk()
    game_over_screen.geometry("300x180")
    game_over_screen.title("Game Over")
    game_over_screen.configure(background='black')
    game_over_screen.resizable(False, False)


    #now there is a label that the game is over
    game_over_label = tk.Label(game_over_screen, font=("Arial", 14, "bold"), bg="black", fg="#64d86b", text="Game Over!")
    game_over_label.pack(pady=2)

    #Now it's trying to get your name?
    name_label = tk.Label(game_over_screen, font=("Arial", 14, "bold"), bg="black", fg="#64d86b", text="Enter your name:")
    name_label.pack(pady=2)

    #This creates a box you can eneter text into
    #But don't give them your name, they will sell your info to china
    name_entry = tk.Entry(game_over_screen, bg="#3A3A3A", fg="#CCCCCC", font=("Arial", 14, "bold"))
    name_entry.pack(pady=5)

    #Creates a button that says "submit" on it
    #Please do not submit into anything
    submit_button = tk.Button(game_over_screen, fg="#46036A", bg="green", text="Submit", command=printScore)
    submit_button.pack(pady=5)
    
    #Closes the game over screen and the game
    def mega():
        game_over_screen.destroy()
        canvas.destroy()
        window.destroy()

    #Finally the Quit button that definetly doesn't install a keylogger on your computer if you press it (/s)
    quit_button = tk.Button(game_over_screen, text="Quit", fg="#46036A", bg="green", command=mega)
    quit_button.pack(pady=5)

    #Collects information of your screen height and width
    screen_width = game_over_screen.winfo_screenwidth()
    screen_height = game_over_screen.winfo_screenheight()

    #Calculates the center of your screen
    x = int((screen_width / 2) - (300 / 2))
    y = int((screen_height / 2) - (180 / 2))

    #Sets the game over screen in the middle of the screen using complex geometry that humans can't comprehend
    game_over_screen.geometry(f"300x180+{x}+{y}")

    #lööps bröther
    game_over_screen.mainloop()

#Creates the window with a very based title
window = Tk()
window.title("Don't trust the federal agents")
window.resizable(False, False)

#Score is 0 on default and the direction is down
score = 0
direction = 'down'

#Labels score on the top of the window
label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

#Defines canvas
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

#Updates the window (NOT WINDOWS DON'T WORRY)
window.update()

#Sets the volume of the munching sound effect to 0.05 so it doesn't demolish your eardrums (thank me later)
sound_effect.set_volume(0.05)

#Now this steals information about your computers screen
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width =  window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#Defines x and y with your screen info divided by 2
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

#I failed geometry at school but this centers the window
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

#My game is so bad, One Direction CHANGED DIRECTION
#Jokes aside binds WASD to change direction
window.bind('<a>', lambda event: change_direction('left'))
window.bind('<d>', lambda event: change_direction('right'))
window.bind('<w>', lambda event: change_direction('up'))
window.bind('<s>', lambda event: change_direction('down'))

#It seems like I had to bind it 2 times because movement wouldn't work if the caps were on lmao
window.bind('<A>', lambda event: change_direction('left'))
window.bind('<D>', lambda event: change_direction('right'))
window.bind('<W>', lambda event: change_direction('up'))
window.bind('<S>', lambda event: change_direction('down'))

#snake is Snake
snake = Snake()
#food is Food
food = Food()

#call next turn for snake and food
next_turn(snake, food)

#lööps bröther
window.mainloop()