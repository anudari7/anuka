def sayhi(name, age):
    print("hello "+ name + " you are " + str(age))
sayhi("anuka", 16)

def cube(num):
    return num*num*num
result = cube(4)
print(result)
print(cube(150))

def min_num(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num1
    else:
        return num3
print(min_num(24,65,1))
fusk
mimi = min(25, 53, 870)
print(mimi)