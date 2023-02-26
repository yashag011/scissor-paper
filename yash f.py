from tkinter import *
from PIL import Image,ImageTk
from random import randint

#main window 
root = Tk()
root.title("stone paper")
root.configure(background="#9b59b6")

#picture
rock_image = ImageTk.PhotoImage(Image.open("ock.png"))
paper_image = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_image = ImageTk.PhotoImage(Image.open("scissor.png"))
rock_image_comp = ImageTk.PhotoImage(Image.open("o.png"))
paper_image_comp = ImageTk.PhotoImage(Image.open("p.png"))
scissor_image_comp = ImageTk.PhotoImage(Image.open("sc.png"))

#insert
user_label = Label(root, image=scissor_image, bg="#9b59b6")
comp_label = Label(root, image=scissor_image_comp, bg="#9b59b6")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#scores
playerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore = Label(root, text=0, font=100, bg="#9b59b6", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

#indicators
user_indicator = Label(root, font=50, text="USER", bg="#9b59b6", fg="white").grid(row=0, column=3)
computer_indicator = Label(root, font=50, text="COMPUTER", bg="#9b59b6", fg="white").grid(row=0, column=1)

#messages
msg = Label(root, font=50, bg="#9b59b6", fg="white")
msg.grid(row=3,column=2)
# update message 
def updateMessage(x):
    msg["text"] = x
#update user score 
def updateUserscore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)
#update computer score
def updateCompscore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

#checkwinner
def checkwin(player,computer):
    if player == computer:
        updateMessage("tie")
    elif player == "rock":
        if computer == "paper":
            updateMessage("you lose")
            updateCompscore()
        else:
            updateMessage("you win")
            updateUserscore() 
    elif player == "paper":
        if computer == "scissor":
            updateMessage("you lose")
            updateCompscore()
        else:
            updateMessage("you win")
            updateUserscore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("you lose")
            updateCompscore()
        else:
            updateMessage("you win")
            updateUserscore()
    else:
        pass                        


#UPDATE CHOICES
choices = ["rock","paper","scissor"]
def updatechoices(x):
    #for computer
    compchoices= choices[randint(0,2)]
    if compchoices=="rock":
        comp_label.configure(image=rock_image_comp)
    elif compchoices=="paper":
        comp_label.configure(image=paper_image_comp)
    else:
        comp_label.configure(image=scissor_image_comp)        

    #for user
    if x=="rock":
        user_label.configure(image=rock_image)
    elif x=="paper":
        user_label.configure(image=paper_image)
    else:
        user_label.configure(image=scissor_image)

    checkwin(x,compchoices)    

#buttons
rock = Button(root, width=20, height=2, text="rock", bg="#FF3E4D", fg="white", command= lambda:updatechoices("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="paper", bg="#FAD02E", fg="white", command= lambda:updatechoices("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="scissor", bg="#0ABDE3", fg="white", command= lambda:updatechoices("scissor")).grid(row=2, column=3)

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
w = 815
h = 300
x = (sh/2) - (h/2)
y = (sw/2) - (w/2)
root.geometry('%dx%d+%d+%d' % (w,h,x,y))
root.resizable(False, False)
root.mainloop()