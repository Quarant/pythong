import random

def num_len(num_list):
    if(len(num_list)<6):
        raise Exception(1,"fall to reach limit")
    elif(len(num_list)>6):
        raise Exception(2,"list exceeded limit")

def dublicate_number(num_list):
    for i in num_list:
        if(num_list.count(i) > 1):
            raise Exception(3,"dublicate numbers")

def range_of_number(num_list):
    for i in num_list:
        if(not(i>=1 and i<=49)):
            raise Exception(4,"number exceeded range")

def get_numbers():
    temp_list = []
    for i in input("podaj liczby\n").strip().split(" "):
        if(len(i)>0):
            temp_list.append(int(i))
    return temp_list

def calculate_error(num_list):
    num_len(num_list)
    dublicate_number(num_list)
    range_of_number(num_list)

def calculate_winners(num_list):
    temp_list = []
    while len(temp_list) < 6:
        r=random.randint(1,49)
        if(not(temp_list.count(r)>0)):
            temp_list.append(r)
    hits=0
    for i in num_list:
        for j in temp_list:
            if(i==j):
                hits+=1
    return hits,temp_list

def main():    
    nr = get_numbers()
    try:
        calculate_error(nr)
    except Exception as e:
        code,reason = e.args
        print("an error was cought \n{}".format(reason))
        exit(code)

    hits,num = calculate_winners(nr)
    
    print("""Your Numbers was {} \nLucky Numbers Was {}\nAnd you hit {} times!""".format(nr,num,hits))


if __name__=="__main__":
    main()