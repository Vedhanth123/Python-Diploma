# create a tkinter app which will take data using entry and store it into database
import mysql.connector
from tkinter import *

# mysql connnection
databaseconnection = mysql.connector.connect(host="localhost",user="root",password="admin",database="library")

# cursor
mycursor = databaseconnection.cursor()

def Store(*data):
    
    query = 'INSERT INTO SIGNUP (Name, Pin, Branch, Email, Phone, Password) VALUES ("%s","%s", "%s", "%s", "%s", "%s")'

    data = (data[0].get(), data[1].get(), data[2].get(), data[3].get(), data[4].get(), data[5].get())
    
    mycursor.execute(query, data)

    databaseconnection.commit()

# create a mainwindow
mainwindow = Tk()

# labels
namelabel = Label(mainwindow, text="Name").grid(row=0,column=0)
pinlabel = Label(mainwindow, text="pin").grid(row=1,column=0)
Branchlabel = Label(mainwindow, text="Branch").grid(row=2,column=0)
Emailabel = Label(mainwindow, text="Email").grid(row=3,column=0)
Phoneabel = Label(mainwindow, text="Phone").grid(row=4,column=0)
Passwordabel = Label(mainwindow, text="Password").grid(row=5,column=0)

# Stringvar objects to store data coming from Entry widget
name = StringVar()
pin = StringVar()
Branch = StringVar()
Email = StringVar()
Phone = StringVar()
Password = StringVar()

# Entryfields
Entry(mainwindow,textvariable=name).grid(row=0,column=1)
Entry(mainwindow,textvariable=pin).grid(row=1,column=1)
Entry(mainwindow,textvariable=Branch).grid(row=2,column=1)
Entry(mainwindow,textvariable=Email).grid(row=3,column=1)
Entry(mainwindow,textvariable=Phone).grid(row=4,column=1)
Entry(mainwindow,textvariable=Password).grid(row=5,column=1)

# submit button to store the data to the database
submitbutton = Button(mainwindow, command=lambda: Store(name,pin,Branch, Email,Phone,Password),text="Submit!").grid(row=6,column=0,columnspan=2)


# run the mainloop
mainwindow.mainloop()