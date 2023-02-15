vokaler = "aeiouy"
print("f" in vokaler)
print("ai" in vokaler)
mening = input("skriv en mening på svenska:")
arabiska = ""
n = len(mening)
for i in range(n-2):
    if mening[i] in vokaler:
        if (not(mening[i+1] in vokaler) and not(mening[i+2])):
            
for letter in mening:
    if letter in mening:
        print(letter)