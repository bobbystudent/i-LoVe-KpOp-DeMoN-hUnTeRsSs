from tkinter import *
import random

import tkinter.messagebox

root = tkinter.Tk()

root.title("when you press a button the message will pop up")
root.geometry('500x300')

def RandoFact():
    fact = ""
    factlist = ["you dont want to mess with me.. im the alpha",
                "one day a light breeze happened, and then you flew away",
                "The animals with the lowest brain cell count are sponges and placozoans, which have zero brain cells because they do not have a centralized brain or a nervous system. you have less than that somehow",
                "one time i jumped into a stream and the water raised a bit, then another time your mom jumped into the stream and the stream somehow was empty of water",
                "did you know this fact? its SOOOOO crazy you wont believe me. crazyy right??!?!?!?!?!? ok here it goes. 1, 2, 3, YOU HAVE THE SAME BRAINCELL COUNT AS YOUR MOM, NOTHING. have a terrible day i hope you trip over the bottom step of your stairs"]
    return random.choice(factlist)
def onClick():
   for i in range(10):
       tkinter.messagebox.showinfo("Virus.net", RandoFact())

button = Button(root, text="cool facts", command=onClick, height=5, width=20)

button.pack(side='bottom')
root.mainloop()
