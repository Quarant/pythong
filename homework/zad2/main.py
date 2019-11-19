import threading
from math import *
from os import mkdir

SAVE_FILES_LOCATION="./files"

def function(strName,intNum):
    

    ff=open("{}/{}.txt".format(SAVE_FILES_LOCATION,strName),"w")

    for i in range(1500):
        intNum = intNum+sin(intNum)*cos(intNum)*(tan(intNum)*1.000000000087*pi)
    ff.write(str(intNum))
    ff.close()

def main():

    fd=open("listaNazwILiczb2.txt","r")

    try:
        mkdir(SAVE_FILES_LOCATION)
    except FileExistsError as e:
        print("folder {} allredy exist skipping creation".format(SAVE_FILES_LOCATION))

    for line in fd.readlines():
        strName,intNum = line.split(";")
        # print("{},{}".format(strName,intNum))
        t=threading.Thread(target=function,daemon=False,args=(strName,int(intNum)))
        t.start()

    fd.close()

if __name__=="__main__":
    main()
