from tkinter import *
from PIL import Image, ImageTk
import random

root = Tk()
root.title("ROCK PAPER SCISSORS GAME")
root.configure(bg="#1da1f2")
root.geometry("600x500")

rock_img = ImageTk.PhotoImage(Image.open("rock.jpeg").resize((100,100)))
paper_img = ImageTk.PhotoImage(Image.open("paper.jpeg").resize((100,100)))
scissors_img = ImageTk.PhotoImage(Image.open("scissors.png").resize((100,100)))
user_icon = ImageTk.PhotoImage(Image.open("user.png").resize((50,50)))
comp_icon = ImageTk.PhotoImage(Image.open("computer.png").resize((50,50)))

choices = ["rock", "paper", "scissors"]

main_frame = Frame(root, bg="#1da1f2")
main_frame.pack(expand=True)

score_frame = Frame(main_frame, bg="#1da1f2")
score_frame.pack(pady=10)
playerScore = Label(score_frame, text=0, font=("Georgia", 20, "bold"), bg="#9b59b6", fg="white")
computerScore = Label(score_frame, text=0, font=("Georgia", 20, "bold"), bg="#9b59b6", fg="white")
playerScore.grid(row=0, column=0, padx=50)
computerScore.grid(row=0, column=2, padx=50)

indicator_frame = Frame(main_frame, bg="#1da1f2")
indicator_frame.pack()
user_indicator = Label(indicator_frame, font=("Georgia", 12, "bold"), text="User", bg="#1da1f2", fg="white")
comp_indicator = Label(indicator_frame, font=("Georgia", 12, "bold"), text="Computer", bg="#1da1f2", fg="white")
user_indicator.grid(row=0, column=0, padx=50)
comp_indicator.grid(row=0, column=2, padx=50)

icon_frame = Frame(main_frame, bg="#1da1f2")
icon_frame.pack(pady=5)
user_label_icon = Label(icon_frame, image=user_icon, bg="#1da1f2")
user_label_icon.grid(row=0, column=0, padx=50)
comp_label_icon = Label(icon_frame, image=comp_icon, bg="#1da1f2")
comp_label_icon.grid(row=0, column=2, padx=50)

choice_frame = Frame(main_frame, bg="#1da1f2")
choice_frame.pack(pady=10)
user_label = Label(choice_frame, image=rock_img, bg="#1da1f2")
user_label.grid(row=0, column=0, padx=50)
msg = Label(choice_frame, font=("Georgia", 14, "bold"), bg="#9b59b6", fg="white", text="")
msg.grid(row=0, column=1, padx=20)
comp_label = Label(choice_frame, image=rock_img, bg="#1da1f2")
comp_label.grid(row=0, column=2, padx=50)

def updateChoice(player_choice):
    if player_choice == "rock":
        user_label.configure(image=rock_img)
    elif player_choice == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissors_img)
    
    comp_choice = random.choice(choices)
    if comp_choice == "rock":
        comp_label.configure(image=rock_img)
    elif comp_choice == "paper":
        comp_label.configure(image=paper_img)
    else:
        comp_label.configure(image=scissors_img)
    
    if player_choice == comp_choice:
        msg.config(text="It's a Tie!")
    elif (player_choice == "rock" and comp_choice == "scissors") or \
         (player_choice == "paper" and comp_choice == "rock") or \
         (player_choice == "scissors" and comp_choice == "paper"):
        msg.config(text="You Win!")
        playerScore.config(text=int(playerScore["text"]) + 1)
    else:
        msg.config(text="Computer Wins!")
        computerScore.config(text=int(computerScore["text"]) + 1)

button_frame = Frame(main_frame, bg="#1da1f2")
button_frame.pack(pady=20)
rock_btn = Button(button_frame, width=15, height=2, text="ROCK", font=("Georgia", 12, "bold"),
                  bg="#FF3E4D", fg="white", command=lambda: updateChoice("rock"))
paper_btn = Button(button_frame, width=15, height=2, text="PAPER", font=("Georgia", 12, "bold"),
                   bg="#FAD02E", fg="black", command=lambda: updateChoice("paper"))
scissor_btn = Button(button_frame, width=15, height=2, text="SCISSORS", font=("Georgia", 12, "bold"),
                     bg="#0ABDE3", fg="white", command=lambda: updateChoice("scissors"))
rock_btn.grid(row=0, column=0, padx=10)
paper_btn.grid(row=0, column=1, padx=10)
scissor_btn.grid(row=0, column=2, padx=10)

def reset_game():
    playerScore.config(text=0)
    computerScore.config(text=0)
    msg.config(text="")
    user_label.configure(image=rock_img)
    comp_label.configure(image=rock_img)

reset_btn = Button(main_frame, width=20, height=2, text="RESET GAME", font=("Georgia", 12, "bold"),
                   bg="#FF5733", fg="white", command=reset_game)
reset_btn.pack(pady=10)

root.mainloop()
