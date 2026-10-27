import threading
import time

def num():
    for i in range(1,6):
        print(f"Number: {i}")
        time.sleep(1)

def alpha():
    for a in ['A','B','C','D','E']:
        print(f"Alpha: {a}")
        time.sleep(1)

thread1 = threading.Thread(target=num())
print("                ")
thread2 = threading.Thread(target=alpha())

thread1.start()
thread1.join()
thread2.start()

thread2.join()

print("All tasks are completed")