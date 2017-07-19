import threading as th
anzeigevar = 0
mutex = th.Lock()
limit = int(input("Limit: "))

def counter(thread_id, counter_limit):
    """counts to a conting limit with threads
    """
    global anzeigevar
    global mutex
    while anzeigevar < counter_limit:
        mutex.acquire()
        i = anzeigevar
        i += 1
        anzeigevar = i
        mutex.release()
        print("Thread Nr. " + str(thread_id)+ " Der Zähler ist bei " + str(anzeigevar)+ "\n", end="")
        
for plusvar in range(0, 10):
    new_thread1 = th.Thread(target=counter, args=(plusvar, limit))
    new_thread1.start()
    

