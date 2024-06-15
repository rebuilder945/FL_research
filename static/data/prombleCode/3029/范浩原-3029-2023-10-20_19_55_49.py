name=input().split(',')
score=eval(input())
bond=[]
for x in list(range(len(name))):
    a=[name[x],score[x]]
    bond.append(a)
print(bond)

