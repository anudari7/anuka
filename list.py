friends = ["Kevin", "Karen", "Jim", "oscar", " batuka"]
lucky_numbers = [2, 5, 6, 12, 23, 56, 86]
friends.extend(lucky_numbers)
friends.append("anuka")
friends.insert(3, "haliuka")
print(lucky_numbers)
print(friends)
print(friends.index("Jim"))
print(friends.count)
phrase = input("your favorite animal:")
print(len(phrase))
print(phrase[0:3])
print(phrase.index("a"))
print(phrase.islower())