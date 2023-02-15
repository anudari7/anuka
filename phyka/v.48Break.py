#while loops break example:
n=1
while n<=14:
    print(n)
    n=n+2
    if n==13:
        break
print(n)
print("finished with first example")
#samma loop fast utan break:
n1=1
while n1<=14:#om jag vill inte t.ex att det ska loopa mer än 14, måste jag använda break-
    print(n1)
    n1=n1+2
print(n1)#annars kommer det bli mer än 15.
print("finished with second example")
#för for loop är det nästan samma sak.Se exemplet nedan
w = "anudari"
for letter in w:
    print(letter)
    if letter == "u":
        break
print("las example finished:)")