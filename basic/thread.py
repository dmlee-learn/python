import threading
 
def sum():
    print("Subthread")
 
def captureRun():
    print("Subthread start")

t = threading.Thread(target=sum)
tt = threading.Thread(target=captureRun).start
t.start()
 
print("Main Thread")