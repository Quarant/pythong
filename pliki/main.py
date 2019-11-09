fd = open("./iwokacja.txt","r")
lines = fd.readlines()
fd.close()
for i in lines:
    print(i)
input()