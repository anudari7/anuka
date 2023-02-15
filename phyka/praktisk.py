tal1 = float(input("första tal:"))
tal2 = float(input("andra tal:"))
tal3 = float(input("tredje tal:"))

lis1 = [tal1, tal2, tal3]
print(lis1)

def sorted_list(tal1, tal2, tal3): #kan vara också t1,t2,t3
    tal2 =[]
    if tal1<=tal2 and tal1<=tal3:
        tal2.append(tal1)
        if tal2<= tal3:
            tal2.append(tal2)
            tal2.append(tal3)
        else:
            tal2.append(tal3)
            tal2.append(tal2)