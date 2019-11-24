import tkinter 
import tkinter.messagebox

def click():
    # tkinter.messagebox.showinfo("info","o/")
    s=""
    for i in b:
        s+=b[i].get()+" "
    print(s.strip())
        # print(i[1])


top = tkinter.Tk()
label = tkinter.Label(top,text="imie i nazwisko: ").grid(column=0,row=0)
e = tkinter.Entry(top).grid(column=1,row=0)
# label = tkinter.Label(top).grid(column=0,row=1)
Rvar=tkinter.StringVar()
label_p = tkinter.Label(top,text="płeć").grid(column=0,row=1)
radio = tkinter.Radiobutton(top,text="M",variable=Rvar,value="M").grid(column=0,row=2)
radio2 = tkinter.Radiobutton(top,text="W",variable=Rvar,value="W").grid(column=1,row=2)

tkinter.Label(top,text="zainteresowania").grid(column=0,row=3)
a = ["pływanie","bieganie" , "siadanie","latanie","ruwanie","spadanie","skakanie","frytkowanie"]
b={}
c=0
r=0
smt=[]
for i in a:
    b[i]=tkinter.StringVar()
    smt.append(tkinter.Checkbutton(top,text=i,onvalue=i,offvalue="",variable=b[i]).grid(column=c%3,row=4+int(c/3)))
    c=c+1


button = tkinter.Button(top,text="save",command=click).grid(column=1)

top.mainloop()