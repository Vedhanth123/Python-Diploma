
from tkinter import *

# creating a mainwindow
mainwindow = Tk()
mainwindow.geometry("400x400")

# creating a label and entry widget in tkinter
Modelname = Label(mainwindow, text="ModelName").place(x=30,y=30)
Issue = Label(mainwindow, text="Issue").place(x=30,y=50)
Modelentry = Entry(mainwindow).place(x=120, y=30)
IssueEntry = Entry(mainwindow).place(x=120,y=50)

# running the mainloop
mainwindow.mainloop()