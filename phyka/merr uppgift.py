list1 = ["ANUKA", "KHALIUN", "OCHIRMAA", "AMINER", "BOOGII"]
print(list1)
list2 = list1.copy()
print(list2)
list2.reverse()
print(list2)
element1 = list2[0]
print(element1)
list1.insert(2, element1)
print(list1)
print(list1.count(element1))
print(len(list1))
lucky_numbers = [2, 4, 6, 8, 0]
print(lucky_numbers)
family = ["anuka", "haliuka", "ochirmaa", "amina", "ganbold"]
print(family)
family.extend(lucky_numbers)
print(family)
family.append("zaya")
print(family)