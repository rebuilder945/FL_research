names = input().split(",")
grades = eval(input())
bond = []
for x in list(range(len(names))):
    ls2 = [names[x],grades[x]]
    bond.append(ls2)
print(bond)

