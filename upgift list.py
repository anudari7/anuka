list1 = ["namjoon", "seokjin", "yoongi", "hoseok", "jimin", "taehyung", "jungkook"]
list2 = list1.copy()
print(list2)
list2.reverse()
print(list2)
element1 = [list2[0]]
print(element1)
list1.insert(3, element1)
print(list1)
print(list1.count(element1))
nummer = [24, 35, 76, 8976, 41]
nummer.append(55)
print(nummer)
nummer2 = (21, 32, 43)
nummer.extend(nummer2)
print(nummer)
print("append kommer adda nåt nytt till listan, medan extend kommer slå ihop två listor ")
nummer.pop(7)
print(nummer)
nummer.remove(8976)
print(nummer)
print("pop radderar element med positon, fast remove radderar med value")
number_of_elements_of_nummerlist = len(nummer)
print("man kan räkna elementet med len", number_of_elements_of_nummerlist)
