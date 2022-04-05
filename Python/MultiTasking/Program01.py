# Share a single variable between two continuous loops in threads

import threading 
import time

global var
var = 0  

def thread1():
    global var
    while True:
        print("Variable inside thread1 ",var)
        var += 1
        time.sleep(1)

def thread2():
    global var
    while True:
        print("Variable inside thread2 ",var)
        var += 1
        time.sleep(3)

thread1 = threading.Thread(target = thread1)
thread2 = threading.Thread(target = thread2)

thread1.start()
thread2.start()