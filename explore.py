from tkinter import *
from tkinter import ttk 

def gameplay(name, userClass):
    win = Toplevel()
    win.title("My RPG")
    messageFrame = Frame(win, bg="black",border=20)
    messageFrame.grid(row=0,column=0, columnspan=4, padx=10,pady=10)
    header = Label(messageFrame, justify="center",  wraplength=150, text="A weary traveller you see a cave in the storm and head toward it. As you approach the cave you see a small light within the opening. Ypu call out but recieve no response. You Continue into the cae opening", bg="black", fg="white")
    header.grid(row=0, column=0,columnspan=3)
    myButton = Button(win,text="explore", padx=10, pady=10)
    myButton2 = Button(win,text="fight", padx=10, pady=10)
    myButton3 = Button(win,text="speak", padx=10, pady=10)
    myButton4 = Button(win,text="Leave Room", padx=10, pady=10)


    myButton.grid(row=4, column=0)
    myButton2.grid(row=4, column=1)
    myButton3.grid(row=4, column=2)
    myButton4.grid(row=4, column=3)