N = int(input("ange tavlans storlek:"))
table = []
for i in range(N):
    table.append(".")
print(table)
print()
for j in range(N):
    nyrad = []
    for i in range(N):
        nyrad.append(".")
    table[j] = nyrad
table[2][1] = "M"
table[0][4] = "skåne"
for row in table:
    print(row)
