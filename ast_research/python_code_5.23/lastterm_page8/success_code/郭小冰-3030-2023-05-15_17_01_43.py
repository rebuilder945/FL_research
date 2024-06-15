names=input().split(",")
grades=eval(input())
bond=[]
for x in list(raange(len(names))):
    ml=[names[x],grades[x]]
    bond.append(ml)
print(bond)
