from tkinter import *

# create a main window
mainwindow = Tk()

# creating a stringvar class to store data coming from entry widget
entrytext = StringVar(mainwindow)

# creating a label
lb = Label(mainwindow, text="I am a label").grid(row=0,column=0)

# creating an entry
entry = Entry(mainwindow,textvariable=entrytext).grid(row=0,column=1)

# creating a Text widget which shows whatever is written into the entry
txt = Text(mainwindow)
txt.grid(row=1,column=0,columnspan=2)

def display():
    txt.insert(END, entrytext.get())

# creating a button which displays whatever is written on entry widget
bt = Button(mainwindow,command=display,text="Display!").grid(row=2,column=0,columnspan=2)

mainwindow.mainloop()