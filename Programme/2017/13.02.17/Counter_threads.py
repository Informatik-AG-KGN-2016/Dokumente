import threading

def counter(thread_id, counter_limit):
    """counts to a conting limit with threads
    """
    anzeigevar = 1
    while counter_limit != 0:
        print("Thread Nr. " + str(thread_id)+ " Der Zähler ist bei " + str(anzeigevar)+ "\n", end="")
        counter_limit -= 1
        anzeigevar += 1

for i in range(0, 10):
    new_thread1 = threading.Thread(target=counter, args=(i, 100))
    new_thread1.start()
    
