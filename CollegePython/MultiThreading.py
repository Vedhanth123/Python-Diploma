# You can create threads in python using Threading module

from threading import Thread

# creating a thread
t1 = Thread(target=lambda : print("Thread"))

# starting a thread
t1.start()

