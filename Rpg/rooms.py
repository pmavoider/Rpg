from tkinter import *
from tkinter import ttk 
import random

# room with no enemies actions search, 

rooms =[
    ["Small Room", True], 
    ["Large Room", False], 
    [ "Medium Room", True] 
]

treasure = [20, 5, 10, 0]
print (random.choice(rooms)[0])

def entry():
    room = random.choice(rooms)
    messages = ["You find yourself in a dimly lit " + room[0] +  ", The room smells musty to your left you see an opening with a well lit pathway, to your right you see another opening with a dimly lit path.", "You enter a dark " + room[0] + ", The Room smells musty and is damp. you barely make out 2 paths one to the left and one to the right." ]
    if room:
          msg = random.choice(messages)
          print(msg)
    

entry()