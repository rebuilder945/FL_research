#name=[input()]
#grade=input()
#answer=[name,grade]
#abc=[]
#for n in abc:
#   print(n)
#print(answer[n][n])
#
names=input().split(",")
grades=eval(input())
bond=[]
for x in list(range(len(names))):
    ml=[names[x],grades[x]]
    bond.append(ml)
print(bond)
