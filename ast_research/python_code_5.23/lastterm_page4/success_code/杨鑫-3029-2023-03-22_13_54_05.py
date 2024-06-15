names = input().split(",")
grades = eval(input())
bond = []
for x in list(range(len(names))):
    m1=[names[x],grades[x]]
    bond.append(m1)
print(bond)
