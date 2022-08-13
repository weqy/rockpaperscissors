import tkinter as tk
from tkinter import *
import random
import playsound

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Rock, Paper, Scissors')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Which would you like to play as?')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)

choices = ["rock", "paper", "scissors"]
my_choice = random.choice(choices)


def clear_text():
   entry1.delete(0, END)


def user_entry_check():
    if "scissors" in entry1.get():
        rock_paper_scissors()
    elif "rock" in entry1.get():
        rock_paper_scissors()
    elif "paper" in entry1.get():
        rock_paper_scissors()
    else:
        error = tk.Label(root, fg="red", text="Please check your entry.")
        error.config(font=('helvetica', 10))
        canvas1.create_window(200, 220, window=error)
        clear_text()


def rock_paper_scissors():
    if my_choice == entry1.get():
        result = tk.Label(root, text="Tie! Both players chose " + my_choice)
        result.config(font=('helvetica', 10))
        canvas1.create_window(200, 220, window=result)
    elif my_choice == "scissors" and "rock" in entry1.get():
        result = tk.Label(root, text="User wins! User chose " + entry1.get() + "\n and computer chose " + my_choice)
        result.config(font=('helvetica', 10))
        canvas1.create_window(200, 220, window=result)
        playsound.playsound('winner.mp3')
    elif my_choice == "rock" and "scissors" in entry1.get():
        result = tk.Label(root, text="Computer wins! User chose " + entry1.get() + "\n and computer chose " + my_choice)
        result.config(font=('helvetica', 10))
        canvas1.create_window(200, 220, window=result)
        playsound.playsound('loser.mp3')
    elif my_choice == "paper" and "rock" in entry1.get():
        result = tk.Label(root, text="Computer wins! User chose " + entry1.get() + "\n and computer chose " + my_choice)
        result.config(font=('helvetica', 10))
        canvas1.create_window(200, 220, window=result)
        playsound.playsound('loser.mp3')
    elif my_choice == "rock" and "paper" in entry1.get():
        result = tk.Label(root, text="User wins! User chose " + entry1.get() + "\n and computer chose " + my_choice)
        result.config(font=('helvetica', 10))
        canvas1.create_window(200, 220, window=result)
        playsound.playsound('winner.mp3')
    elif my_choice == "paper" and "scissors" in entry1.get():
        result = tk.Label(root, text="User wins! User chose " + entry1.get() + "\n and computer chose " + my_choice)
        result.config(font=('helvetica', 10))
        canvas1.create_window(200, 220, window=result)
        playsound.playsound('winner.mp3')
    elif my_choice == "scissors" and "paper" in entry1.get():
        result = tk.Label(root, text="Computer wins! User chose " + entry1.get() + "\n and computer chose " + my_choice)
        result.config(font=('helvetica', 10))
        playsound.playsound('loser.mp3')



button1 = tk.Button(text='Play!', command=user_entry_check, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()
