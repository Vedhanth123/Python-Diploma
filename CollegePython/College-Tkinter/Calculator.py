from tkinter import *

# create a calculator which takes input from buttons and adds them

# defining a function to implement button task
def printer():
    print("Button pressed!")

# creating a mainwindow
mainwindow = Tk()

# setting both vars to Null
var1 = var2 = ""
operation = ""

# write a function to store a value in a and b
def inputter(num):
    global var1
    global var2
    if(var1 == ""):
        var1 += num
    else:
        var2 += num


def setoperator(oper):
    global operation
    operation = oper
    

def evalaute():
    
    global operation
    global var1
    global var2

    if(operation == '+'):
        print(int(var1) + int(var2))
        var1 = var2 = ""
    elif(operation == '-'):
        print(int(var1) - int(var2))
        var1 = var2 = ""
    elif(operation == '*'):
        print(int(var1) * int(var2))
        var1 = var2 = ""
    elif(operation == '/'):
        print(int(var1) // int(var2))
        var1 = var2 = ""
    else:
        pass


# creating buttons and placing them on grid
num1 = Button(mainwindow,command=lambda : inputter('1'),text=1).grid(row=0, column=0,padx=5,pady=5)
num2 = Button(mainwindow,command=lambda : inputter('2'),text=2).grid(row=0, column=1,padx=5,pady=5)
num3 = Button(mainwindow,command=lambda : inputter('3'),text=3).grid(row=0, column=2,padx=5,pady=5)
num4 = Button(mainwindow,command=lambda : inputter('4'),text=4).grid(row=1, column=0,padx=5,pady=5)
num5 = Button(mainwindow,command=lambda : inputter('5'),text=5).grid(row=1, column=1,padx=5,pady=5)
num6 = Button(mainwindow,command=lambda : inputter('6'),text=6).grid(row=1, column=2,padx=5,pady=5)
num7 = Button(mainwindow,command=lambda : inputter('7'),text=7).grid(row=2, column=0,padx=5,pady=5)
num8 = Button(mainwindow,command=lambda : inputter('8'),text=8).grid(row=2, column=1,padx=5,pady=5)
num9 = Button(mainwindow,command=lambda : inputter('9'),text=9).grid(row=2, column=2,padx=5,pady=5)
num0 = Button(mainwindow,command=lambda : inputter('0'),text=0).grid(row=3, column=0,columnspan=2,padx=5,pady=5)
plus = Button(mainwindow,command=lambda : setoperator("+"),text='+').grid(row=0, column=3,padx=5,pady=5)
minus = Button(mainwindow,command=lambda : setoperator("-"),text='-').grid(row=1, column=3,padx=5,pady=5)
multiply = Button(mainwindow,command=lambda : setoperator("*"),text='*').grid(row=2, column=3,padx=5,pady=5)
div = Button(mainwindow,command=lambda : setoperator("/"),text='/').grid(row=3, column=3,padx=5,pady=5)
evaluate = Button(mainwindow,command=lambda : evalaute(),text='=').grid(row=4,column=3,padx=5,pady=5,columnspan=3)


# running mainloop
mainwindow.mainloop()