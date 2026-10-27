import threading
import time

def cric():
    while True:
        print("The background is running")
        time.sleep(1)

thread1 = threading.Thread(target=cric)
thread1.daemon =True

time.sleep(3)

print("Main program ends")