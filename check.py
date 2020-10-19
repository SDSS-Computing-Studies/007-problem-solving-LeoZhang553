import time

curTime = time.time()
print("Current epoch time is " + str(curTime))
print("Going to sleep for 10 seconds now...")
for i in range(0,10):
    print(".", end="")
    time.sleep(1)
print("10 seconds have passed")
curTime = time.time()
print("Current epoch time is " + str(curTime))