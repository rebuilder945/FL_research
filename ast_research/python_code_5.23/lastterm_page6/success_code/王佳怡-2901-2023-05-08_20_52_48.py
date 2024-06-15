a=input()
l=[]
while a!="#":
    a=int(a)
    l.append(a)
    a=input()
print(len(l),end=" ")
print(sum(l))
