# importing threading module to create multiple threads
import threading


# creating a class to define what thread must do
# class myThread(threading.Thread):

#     constructor to name, giveid to a thread
#     def __init__(self, name, id):
#         threading.Thread.__init__(self)
#         self.name = name
#         self.id = id
    
#     defining runner method
#     def run(self):
#         print("Thread running like shit")
    
# creating a thread

def Joking():
    for x in range(100):
        print("I am a joker")

th1 = threading.Thread(target=Joking())
th1.start()
