from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
import random

# Array for room choices 
rooms =[
    ["Small Room", True], 
    ["Large Room", False], 
    [ "Medium Room", True] 
]
#array for room adjectives 
roomAdjectives = ["musty", "dimly lit", "bright", "dirty", "surprisingly clean and well lit" ]
#array used to randomize encounters
outcomes = [True,True,False]
#array to randomize treasures
treasure = [8, 5, 10, 4, 2]
#array for npc clues
npcCues = ["You hear heavy breathing. ", "You hear a shuffling of feet", "you see movement out of the corner of your eye", "you hear a voice in the darkness"]
# array for different traps 
traps = ["As you exit you hear a click and watch as spikes shoot out of the wall you are dead.", "The floor slides out from under you and you find yourself falling."]
# enemies array 
enemies = [ 
    ["goblin", 1, True ],
    ["hobgoblin", 3, False],
    ["centaur" ,5, False],
    ["centaur", 5 , True], 
    ["spirit", 3,True],
    ["spirit", 3, False],
    ["troll", 8, False],
    ["human", 3, True],
    ["human", 4, False]
]



#Main function 
def gameplay(name, userClass):
    # Variable to track users gold count 
    global treasureCount
    treasureCount = 0
    global life
    life = 20


# function disables movement buttons and activates interaction buttons 
    def interaction():
        leaveButton.config(state=DISABLED)
        exploreButton.config(state=DISABLED)
        speakButton.config(state=NORMAL)
        fightButton.config(state=NORMAL)

    # function enables movement buttons and disables interaction buttons
    def nonInteraction():
        leaveButton.config(state=NORMAL)
        exploreButton.config(state=NORMAL)
        speakButton.config(state=DISABLED)
        fightButton.config(state=DISABLED)
    


    #function allows user to explore enviroment 
    def explore():
        global treasureCount
        if random.choice(outcomes):

            found = random.choice(treasure)
            header["text"] = "You found " + str(found) + " treasure."
            treasureCount += found
        else:
            header["text"] = random.choice(npcCues)
            interaction()
        update()
        exploreButton.config(state=DISABLED)

    # function to control speaking with npc's
    def speak():
        global life
        global treasureCount
        character = random.choice(enemies)
        if random.choice(outcomes):
            if random.choice(outcomes):
                header["text"] = "The " + character[0] +  " attacks you, After a small skirmish you slay the " + character[0]+ ". You gain " + str(character[1]) + " gold, and lose " + str(character[1]) + " life."
                life -= character[1]
                treasureCount += character[1]
                update()
                nonInteraction()
                exploreDisable()
                if life <= 0:
                    header["text"] = "you are dead"
                    youlose()
            else:
                header["text"] = "You are confronted by a minotaur."
                youLose()

        else:
            if random.choice(outcomes):
                header["text"] = "The " + character[0] + " is friendly, and gives you directions to the exit."
                update()
                nonInteraction()
                exploreDisable()
            else:
                 header["text"] = "The " + character[0] + " gives you a healing potion. You heal 3 hp."
                 life += 3
                 update()
                 nonInteraction()
                 exploreDisable()

        
            # add a variety of outcomes
    # function to exit program       
    def exit():
        quit()
    # function to fight npc's
    def fight():
        global life
        global treasureCount
        character = random.choice(enemies)
        gain = random.choice(treasure)
        if character[1] >= life:
            header["text"] = "You are bested by the" + character[0] + "."
            youLose() 
        else:
            header["text"] = "You Atack into a "+ character[0] + " you slay the " + character[0] + " You lose " + str(character[1]) + " life and gain " + str(gain) + " treasure."
            life -= character[1]
            treasureCount += gain
            update()
            nonInteraction()
            exploreDisable()

       
    # function to end game disables buttons 
    def youLose():
        header["text"] += "You have died. Luckily you can try again"
        leaveButton.config(state=DISABLED)
        exploreButton.config(state=DISABLED)
        speakButton.config(state=DISABLED)
        fightButton.config(state=DISABLED)
    

    #function for winning the game 
    def youWin():
        header["text"] = "Congratulations you have suprised the cave of wonders. You found the Exit. Thanks for playing. "
        leaveButton.config(state=DISABLED)
        exploreButton.config(state=DISABLED)
        speakButton.config(state=DISABLED)
        fightButton.config(state=DISABLED)
    
    #function to disable explore button after its used once in each room 
    def exploreDisable():
         exploreButton.config(state=DISABLED)

    # function to move forward thru the game 
    def roomChange():
        global life

        global room
        exploreButton.config(state=NORMAL)
        adjective = random.choice(roomAdjectives)
        room = random.choice(rooms)
        messages = ["You find yourself in a " + adjective + " " + room[0] +  "." ]
        # trigger trap here
        if treasureCount >= 75:
            # function for final room 
            youWin()
        else:
            if random.randint(1,8) != 7:
                msg = random.choice(messages)
                header["text"] = msg
                update()
            else:
                header["text"] = random.choice(traps)
                youLose()
            
       
    # function updates totals for treasure and life 
    def update():
        lifeLabel["text"] = "Life: " + str(life)
        goldLabel["text"] = "Tresure: " + str(treasureCount)
    
    
            
    # variable to display correct character  
    imageFile = userClass + ".jpg"
# window creation 
    root = Tk()
    win = ttk.Frame(root )
    win.grid(row=0,column=0,sticky="")
    win.grid_rowconfigure(0, weight=1)
    win.grid_columnconfigure(0, weight=1)
    root.title( "My Rpg")
    # import for character image
    userImage = Image.open(imageFile)
    userImageresized = userImage.resize((80,80), Image.ANTIALIAS)
    display = ImageTk.PhotoImage( userImageresized)
    # image placement 
    userLabel = Label(win, image=display, padx=50)
    userLabel.image = display
    # screen message and button creation
    nameLabel = Label(win,text=name )
    messageFrame = Frame(win, bg="black",border=20)
    header = Label(messageFrame, justify="center",  wraplength=150, text=("Welcome " + name + " You find yourself in the cave of wonders. The only way to escape is to find 75 treasures. Good Luck You will need it"), bg="black", fg="white")
    exploreButton = Button(win,text="explore", padx=10, pady=10, command=explore)
    fightButton = Button(win,text="fight", padx=10, pady=10, command=fight, state=DISABLED)
    speakButton = Button(win,text="speak", padx=10, pady=10, command=speak , state=DISABLED)
    leaveButton = Button(win,text="Move Forward", padx=10, pady=10, command=roomChange)
     # message and button placment 
    messageFrame.grid(row=0,column=2, columnspan=3, padx=10,pady=10)
    nameLabel.grid(column=0, row=2, columnspan=2)
    userLabel.grid(row=0,column=0, columnspan=2)
    header.grid(row=0, column=0,columnspan=3)
    
    #life label and a spacer creation
    buttonSpacer = Label(win, text="")
    exitButton = Button(win, text="exit", bg="red",padx=10, pady=10, fg="white", command=exit)
    lifeLabel = Label(win, text="Life: " + str(life))
    goldLabel = Label(win, text="Treasure: " + str(treasureCount))
    buttonSpacer.grid(row=5, column=0, columnspan=3)
   
   # Life an treasure label placment 
    lifeLabel.grid(row=3, column=1, pady=20)
    goldLabel.grid(row=3, column=2)

   
# button placment 
    exploreButton.grid(row=4, column=0)
    fightButton.grid(row=4, column=1)
    speakButton.grid(row=4, column=2)
    leaveButton.grid(row=4, column=3)
    exitButton.grid(row=7, column=3)

    win.mainloop()