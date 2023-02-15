import math

word = input("what color is your shirt:")         #i had white shirt
print(word)
print("number of alphabets in his word ", len(word))
print(word[0:3])
print(word.index("e"))
if word.islower():
    print(False)
else:
    print(True)
sentence = input("how was your day:")
res = len(sentence.split())
print(str(res))
print(sentence.rindex("a"))
if sentence.endswith("."):
    print("the sentence ends with(.) ")
else:
    print("the sentence doesnt end with(.)")
print(sentence.title())
#v39uppgifter
x = int(input("enter a number:"))
y = int(input("second number:"))
print(x/y)
print("first number we got:", x)
print("second number we got:", y)
x = int(input("give me a  number:"))
y = float(input("give me decimal number:"))
print(float(x))
print(int(y))
print("när man conventerar int till float, kommer den byte heltal till decimal tal/komma tecken och en nolla/, om man gör det tvärtom, kommer det byta decimal till heltal")
import math
print(math.ceil(x))
print(math.floor(x))
print(math.ceil(y))
print(math.floor(y))

list1 = ["ANUKA", "KHALIUN", "OCHIRMAA", "AMINER", "BOOGII"]
print(list1)
list2 = list1.copy()
print(list2)
list2 = list1.reverse()
print(list2)
element1 = list2[0]
print(element1)

