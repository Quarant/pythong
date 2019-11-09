import random

l = []
for i in range(4000):
    l.append(random.randint(1,100))
hits = 0
for i in l:
    if(i%3 is 0):
        print("liczba {} jest podzielna przez 3".format(i))
        hits+=1

print("trafione {} ".format(hits))