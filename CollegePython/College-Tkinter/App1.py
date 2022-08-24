# create a main window and host a button on it that prints something on the command line
from tkinter import *

mainwindow = Tk()
mainwindow.geometry("400x500")


def ButtonEvent():
    print("Button Clicked!")

# creating a button
bt = Button(mainwindow, text="Click ME!", command=ButtonEvent)
bt.pack()


mainwindow.mainloop()