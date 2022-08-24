# write a python program to turn on and off LED light using Raspberry pi

# import GPIO, RPI as GPIO
# import time

# GPIO.setmode(GPIO, BCM)
# GPIO.setwarnings(False) 
# GPIO.setup(18, GPIO, OUT)
# while True:
#     print("LED on")
#     GPIO.output(18, GPIO, HIGH)
#     time.sleep(1)
#     print("LED off")
#     GPIO.output(18, GPIO, LOW)
#     time.sleep(1)


# write a python program to Tkinter checkbox

from tkinter import *
master = Tk()

def var_states():
   print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))

Label(master, text="Your sex:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="male", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="female", variable=var2).grid(row=2, sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=3, sticky=W, pady=4)
Button(master, text='Show', command=var_states).grid(row=4, sticky=W, pady=4)
mainloop()