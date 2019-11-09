fd = open("C:/Users/Uczeń/Desktop/git/pythong/pliki/iwokacja.txt","r")
lines = fd.readlines()
fd.close()
nn=[]
for i in lines:
    nn.append(i.replace("o","X"))

fd = open("C:/Users/Uczeń/Desktop/git/pythong/pliki/new.txt","w")
fd.writelines(nn)
fd.close()