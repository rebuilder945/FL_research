names=input().split(",")
grades=eval(input())
bond=[]
for x in list(range(len(names))):
    n=[names[x],grades[x]]
    bond.append(n)
print(bond)
