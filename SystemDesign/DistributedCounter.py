import time
def distributedCounter():
    start = time.time()
    counter = 0
    while counter < 1000000001:
        counter+=1
        print(counter)
    end = time.time()
    print(end - start)
distributedCounter()