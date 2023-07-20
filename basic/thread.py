import threading
 
def one():
    print("one start")
 
def two():
    print("two start")

first = threading.Thread(target=one)
threading.Thread(target=two).start
first.start()
 
print("Main")