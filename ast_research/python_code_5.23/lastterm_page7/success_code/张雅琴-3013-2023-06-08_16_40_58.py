a=input() or "ok"
lst1=[]
lst2=[]
while a!='ok':
    b=a.split()
    lst1.append(b[0])
    lst2.append(int(b[1]))
    GDP={}
    GDP[b[0]]=b[1]
    a=input() or "ok"
lst1.sort()
lst2.sort()
print(lst1)
print(lst2)
if "India"not in lst1:
    print("no")
else:
    print("yes")
print(sum(lst2))

