from tkinter import *
from tkinter import ttk
from explore import gameplay
from PIL import Image, ImageTk
import random 
# This is the main page of the game, On this screen the user creates a user name and chooses a class. The user name and class are passed to the next screen to be used.
#Main Function
def MainGame():
    #set up for window 
    root = Tk()
    frm = ttk.Frame(root )
    frm.grid(row=0,column=0,sticky="")
    frm.grid_rowconfigure(0, weight=1)
    frm.grid_columnconfigure(0, weight=1)
    root.title( "The Cave of Wonders")
    root.geometry("500x500")
    global username 



# image at bottom of screen 
    pillow_image = Image.open("background.jpg")
    test = ImageTk.PhotoImage( pillow_image)
    label1 = Label( image=test, padx=50)
    label1.image = test
    label1.grid(row=6,column=0)
    
    #function to verify username entere and to pass name and class choice 
    def characterCreation(x):
        username = nameEntry.get()
        if username:
            print(username)
            userClass= x
            root.destroy()
            gameplay(username,userClass )
        else:
            errorLabel["text"] = "You failed to enter a username"





# label and buttons for screen 
    myLabel = Label(frm,text="The Cave of Wonders", font=("Arial",  30), padx=10, pady=10)
    classChoiceLabel = Label(frm,text = "Please Choose a Class", font=15, padx=10,pady=10)
    myButton = Button(frm,text="paladin", padx=10, pady=10, command=lambda: characterCreation("paladin"))
    myButton2 = Button(frm,text="wizard", padx=10, pady=10, command=lambda: characterCreation("wizard"))
    myButton3 = Button(frm,text="warrior", padx=10, pady=10, command=lambda: characterCreation("warrior"))
    myButton4 = Button(frm,text="Thief", padx=10, pady=10, command=lambda: characterCreation("thief"))
    nameEntry = Entry(frm, width=25)
    nameEntry.get()
    nameLabel = Label(frm, text="Enter your characters name")
    errorLabel = Label(frm, text="", fg="red")

# placment of label and buttons 
    myLabel.grid(row=1 , column=0, columnspan=4)
    errorLabel.grid(row=3, column=2, columnspan=3)
    classChoiceLabel.grid(row=4, column= 0, columnspan=4)

    nameEntry.grid(row=2, column=2, columnspan=3)
    nameLabel.grid(row=2, column=0, columnspan=2)

    myButton.grid(row=5, column=0)
    myButton2.grid(row=5, column=1)
    myButton3.grid(row=5, column=2)
    myButton4.grid(row=5, column=3)




    root.mainloop()

MainGame()