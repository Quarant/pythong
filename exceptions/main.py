import threading
import time
import random

def f(liczba,delay):
    for i in range(20):
        liczba *= liczba
        print(liczba)
        time.sleep(delay)
threads=[]

for i in range(10):
    t=threading.thread(target=f,args=(random.randint(1,42),random.randint(1,42)))
    t.start()
    threads.append(t)

