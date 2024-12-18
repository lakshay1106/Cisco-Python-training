import threading

class Box(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)   # super().__init__()
        self.name = name
    def run(self):
        print(f"I m {self.name} Thread")

print("Main thread started")
obj1 = Box("Thread")
obj1.start()
print("Exit from main thread")
