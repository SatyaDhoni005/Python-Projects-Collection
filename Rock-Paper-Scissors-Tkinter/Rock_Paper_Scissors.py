from tkinter import *
from PIL import Image,ImageTk
from random import randint

#Main Window
root = Tk()
root.title("Rock Paper Scissor")
root.configure(background="light blue")

#Picture
rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

#Insert Picture
user_label = Label(root, image=scissor_img, bg="light blue")
comp_label = Label(root, image=scissor_img_comp, bg="light blue")
user_label.grid(row=1, column=4)
comp_label.grid(row=1, column=0)

#Scores
playerScore = Label(root, text=0, font=100, bg="light blue", fg="red")
computerScore = Label(root, text=0, font=100, bg="light blue", fg="red")
playerScore.grid(row=1, column=3)
computerScore.grid(row=1, column=1)

#Buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="red", fg="white", command=lambda: updateChoice("rock"))
paper = Button(root, width=20, height=2, text="PAPER", bg="green", fg="white", command=lambda: updateChoice("paper"))
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="blue",fg="white", command=lambda: updateChoice("scissor"))
rock.grid(row=2, column=1)
paper.grid(row=2, column=2)
scissor.grid(row=2, column=3)

#Indicators
user_indicator = Label(root, font=50, text="USER", bg="black", fg="red")
computer_indicator = Label(root, font=50, text="COMPUTER", bg="black", fg="red")
user_indicator.grid(row=0, column=3)
computer_indicator.grid(row=0, column=1)

#Messages
msg = Label(root, font=50, bg="red", fg="white")
msg.grid(row=3, column=2)

#Update Message
def updateMessage(x):
    msg['text'] = x

#Update User Score 
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

#Update Computer Score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

#Check Winner
def checkWinner(player,computer):
    if player == computer:
        updateMessage("Its a Tie!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You Lose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You Lose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You Lose")
            updateCompScore()
        else:
            updateMessage("You Win")
            updateUserScore()
    else:
        pass

#Update Choices
choices = ["rock","paper","scissor"]

def updateChoice(x):
    
    #For Computer Choice
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)
    
    #For User Choice
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    
    checkWinner(x,compChoice)

root.mainloop()