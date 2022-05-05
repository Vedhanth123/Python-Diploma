# create a main window and host a button on it that prints something on the command line
from tkinter import *

mainwindow = Tk()

# creating a button
bt = Button(mainwindow, text="Click ME!", command=lambda: print("Hello"))
bt.pack()


mainwindow.mainloop()