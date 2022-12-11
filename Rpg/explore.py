from tkinter import *
from tkinter import ttk 
from rooms import entry
import random

rooms =[
    ["Small Room", True], 
    ["Large Room", False], 
    [ "Medium Room", True] 
]
outcomes = [True,True,True,False]
treasure = [20, 5, 10, 0]
npcCues = ["You hear heavy breathing. ", "You hear a shuffling of feet", "you see movement out of the corner of your eye", "you hear a voice in the darkness"]
traps = ["As you exit you hear a click and watch as spikes shoot out of the wall you are dead."]

enemies = [ 
    ["goblin", 1, True ],
    ["troll", 8, False],
    ["human", 3, True],
    ["human", 4, False]
]
global life
life = 20
global gold
gold = 0


curentTreasure = 0 
def gameplay(name, userClass):
    global treasureCount
    treasureCount = 0
# functions to grey buttons
    def interaction():
        leaveButton.config(state=DISABLED)
        exploreButton.config(state=DISABLED)
        speakButton.config(state=NORMAL)
        fightButton.config(state=NORMAL)

    def nonInteraction():
        leaveButton.config(state=NORMAL)
        exploreButton.config(state=NORMAL)
        speakButton.config(state=DISABLED)
        fightButton.config(state=DISABLED)

   
    def explore():
        global treasureCount
        if random.choice(outcomes):

            found = random.choice(treasure)
            header["text"] = "You found " + str(found) + " gold Pieces."
            treasureCount += found
        else:
            header["text"] = random.choice(npcCues)
            interaction()
        update()

    def speak():
        global life
        global treasureCount
        character = random.choice(enemies)
        print(character[2])
        if random.choice(outcomes):
            if random.choice(outcomes):
                header["text"] = "The " + character[0] +  " attacks you, After a small skirmish you slay the " + character[0]+ ". You gain " + str(character[1]) + " gold, and lose " + str(character[1]) + " life."
                life -= character[1]
                treasureCount += character[1]
                print(life)
                if life <= 0:
                    header["text"] = "you are dead"
            else:
                header["text"] = "you are dead"
        else:
            if random.choice(outcomes):
                header["text"] = "The " + character[0] + " is friendly, and gives you directions to the exit."
            else:
                 header["text"] = "The " + character[0] + " gives you a healing potion. You heal 3 hp."
                 life += 3

        update()
        nonInteraction()
            # add a variety of outcomes


    def roomChange():
        global life

        global room
        room = random.choice(rooms)
        messages = ["You find yourself in a dimly lit " + room[0] +  ", The room smells musty to your left you see an opening with a well lit pathway, to your right you see another opening with a dimly lit path.", "You enter a dark " + room[0] + ", The Room smells musty and is damp. you barely make out 2 paths one to the left and one to the right." ]
        # trigger trap here
        if random.randint(1,8) != 7:
            msg = random.choice(messages)
            header["text"] = msg
        else:
            header["text"] = traps[0]
        update()
    
    def update():
        lifeLabel["text"] = "Life: " + str(life)
        goldLabel["text"] = "Gold: " + str(treasureCount)

        


    win = Toplevel()
    win.title("My RPG")
    messageFrame = Frame(win, bg="black",border=20)
    messageFrame.grid(row=0,column=0, columnspan=4, padx=10,pady=10)
    header = Label(messageFrame, justify="center",  wraplength=150, text="A weary traveller you see a cave in the storm and head toward it. As you approach the cave you see a small light within the opening. Ypu call out but recieve no response. You Continue into the cave opening", bg="black", fg="white")
    header.grid(row=0, column=0,columnspan=3)
    exploreButton = Button(win,text="explore", padx=10, pady=10, command=explore)
    fightButton = Button(win,text="fight", padx=10, pady=10, state=DISABLED)
    speakButton = Button(win,text="speak", padx=10, pady=10, command=speak , state=DISABLED)
    leaveButton = Button(win,text="Leave Room", padx=10, pady=10, command=roomChange)
    
    lifeLabel = Label(win, text="Life: " + str(life))
    goldLabel = Label(win, text="Gold: " + str(treasureCount))

    lifeLabel.grid(row=3, column=1, pady=20)
    goldLabel.grid(row=3, column=2)

   

    exploreButton.grid(row=4, column=0)
    fightButton.grid(row=4, column=1)
    speakButton.grid(row=4, column=2)
    leaveButton.grid(row=4, column=3)