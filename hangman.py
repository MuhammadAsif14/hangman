
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random

window=Tk()
window.title("Hangman")

word_list = ["HORSE", "COW","SHEEP", "DEER", "LION", "PANDA", "TIGER", "DOG", "CAT", "RABIT", "MOUSE"]

photos = [PhotoImage(file="C:/Users/cop21/OneDrive/Desktop/images/hang0.png"), PhotoImage(file="C:/Users/cop21/OneDrive/Desktop/images/hang1.png"), PhotoImage(file="C:/Users/cop21/OneDrive/Desktop/images/hang2.png"), PhotoImage(file="C:/Users/cop21/OneDrive/Desktop/images/hang3.png"),
          PhotoImage(file="C:/Users/cop21/OneDrive/Desktop/images/hang4.png"), PhotoImage(file="C:/Users/cop21/OneDrive/Desktop/images/hang5.png"), PhotoImage(file="C:/Users/cop21/OneDrive/Desktop/images/hang6.png"), PhotoImage(file="C:/Users/cop21/OneDrive/Desktop/images/hang7.png"),
          PhotoImage(file="C:/Users/cop21/OneDrive/Desktop/images/hang8.png"), PhotoImage(file="C:/Users/cop21/OneDrive/Desktop/images/hang9.png"), PhotoImage(file="C:/Users/cop21/OneDrive/Desktop/images/hang10.png"), PhotoImage(file="C:/Users/cop21/OneDrive/Desktop/images/hang11.png")]


def newGame():
    
    messagebox.showinfo("Hangman", "Its The Animal Name")
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses=0
    imgLabel.config(image=photos[0])
    the_word=random.choice(word_list)
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))




def guess(letter):
    global numberOfGuesses
    if numberOfGuesses<11:
        txt=list(the_word_withSpaces)
        guessed=list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
            for c in range(len(txt)):
                if txt[c]==letter:
                    guessed[c]=letter
                lblWord.set("".join(guessed))
                if lblWord.get()==the_word_withSpaces:
                    messagebox.showinfo("Hangman", "You Guessed it")
                    newGame()
        else:
                numberOfGuesses+=1
                imgLabel.config(image=photos[numberOfGuesses])
                if numberOfGuesses==11:
                 messagebox.showwarning("Hangman", "Game Over")
    
imgLabel=Label(window)
imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
imgLabel.config(image=photos[0])

lblWord=StringVar()
Label(window, textvariable=lblWord, font=("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)
n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font=("Helvetica 18"), width=4).grid(row=1+n//9, column=n%9)
    n+=1

Button(window, text="new\nGame", command=lambda:newGame(),font=("Helvetica 10 bold")).grid(row=3, column=8, sticky="NSWE")

newGame()    
window.mainloop()