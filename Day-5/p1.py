import time
import threading

def f1():
    print("f1 thread is started")
    for v in range(6):
        result = v+0
        #time.sleep(1)

    else:
        print(f'resut:{result}')
    print("exit fron f1 thread")

print("main thread:")

obj = threading.Thread(target=f1)

print("B4 calling f1 thread")
#f1()
obj.start()
          #obj.join()
          #for v in range(5):
          #time.sleep(1)

print("Exit from Main thread")
