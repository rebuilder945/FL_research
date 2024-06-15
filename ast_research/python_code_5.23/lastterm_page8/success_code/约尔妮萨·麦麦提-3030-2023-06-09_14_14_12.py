name=input().split(",")
grades=eval(input())
bond=[]
for x in list(range(len(name))):
    ml=[name[x],grades[x]]
    bond.append(ml)
print(bond)
