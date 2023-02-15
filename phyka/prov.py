num1 = float(input("give me a number:"))
num2 = float(input("another number:"))
num3 = float(input("last number:"))
list1 = (num1, num2, num3)
print("numbers you entered:", list1)
if num1<=num2 and num1<=num3 and num2<=num3:     #om num1 är mindre än de andra två, kommer de skrivas som minsta tal som vi ser.
    print(num1, num2, num3)
elif num1<=num2 and num1<=num3 and num3<=num2:
    print(num1, num3, num3)
elif num2<=num1 and num2<=num3 and num1<=num3:
    print(num2, num1, num3)
elif num2<=num1 and num2<=num3 and num3<=num1:
    print(num2, num3, num1)
elif num3<=num1 and num3<=num2 and num1<=num2:
    print(num3, num1, num2)
else:
    print(num3, num2, num1)  #sista varianten av lista

