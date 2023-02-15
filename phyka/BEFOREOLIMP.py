deltagare = int(input("antal deltagare:"))
o = 0
fibb = 1
fibbforst = True
forfibb = 0 #hun
andrafibb = False
while deltagare > 0 :
    if fibbforst == True:
        fibb += forfibb
        fibbforst = False
        andrafibb = True
        deltagare = deltagare-fibb
    else:
        forfibb += fibb
        fibbforst = True
        andrafibb = False
        deltagare = deltagare - forfibb
    o += 1
print(o)