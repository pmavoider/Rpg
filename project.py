from tkinter import *
from tkinter import ttk
from explore import gameplay
root = Tk()
frm = ttk.Frame(root )
frm.grid(row=0,column=0,sticky="")
frm.grid_rowconfigure(0, weight=1)
frm.grid_columnconfigure(0, weight=1)
root.title( "My Rpg")
root.geometry("700x350")
global username 

 

def characterCreation(x):
    username = nameEntry.get()
    print(username)
    userClass= x
    gameplay(username,userClass )





myLabel = Label(frm,text="Welcome to my rpg", font=("Arial",  30), padx=10, pady=10)
classChoiceLabel = Label(frm,text = "Please Choose a Class", font=15, padx=10,pady=10)
myButton = Button(frm,text="paladin", padx=10, pady=10, command=lambda: characterCreation("paladin"))
myButton2 = Button(frm,text="wizard", padx=10, pady=10, command=lambda: characterCreation("wizard"))
myButton3 = Button(frm,text="warrior", padx=10, pady=10, command=lambda: characterCreation("warrior"))
myButton4 = Button(frm,text="Thief", padx=10, pady=10, command=lambda: characterCreation("thief"))
nameEntry = Entry(frm, width=25)
nameEntry.get()
nameLabel = Label(frm, text="Enter your characters name")

myLabel.grid(row=1 , column=0, columnspan=4)

classChoiceLabel.grid(row=3, column= 0, columnspan=4)

nameEntry.grid(row=2, column=2, columnspan=3)
nameLabel.grid(row=2, column=0, columnspan=2)

myButton.grid(row=4, column=0)
myButton2.grid(row=4, column=1)
myButton3.grid(row=4, column=2)
myButton4.grid(row=4, column=3)




root.mainloop()