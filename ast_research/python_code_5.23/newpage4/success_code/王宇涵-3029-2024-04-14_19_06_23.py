names = input().split(",")
socres = eval(input())
bond = []
for x in list(range(len(names))):
    ml=[names[x],socres[x]]
    bond.append(ml)
print(bond)
