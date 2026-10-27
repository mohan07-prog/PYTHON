import time

def num():
    for i in range(1,6):
        print(f"Number: {i}")
        time.sleep(1)

def letter():
    for l in ['A','B','C','D','E']:
        print(f"Letter: {l}")
        time.sleep(1)

num()
letter()
print("All Tasks are completed")