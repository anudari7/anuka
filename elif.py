is_male = True
is_tall = False
if is_male and is_tall:
    print(" you are a tall male")
elif is_male and not (is_tall):
    print(" you are a short male")
elif not(is_male) and is_tall:
    print("you are nor male but tall")
else:
    print("you either nor male or not tall or both")