GDP={}
s=input()
lst=[]
lst2=[]
lst3=[]
lst4=[]
while s!="ok":
    lst=s.split()
    GDP[lst[0]]=eval(lst[1])
    s=input()
for x in GDP.keys():
    lst2.append(x)
lst2.sort()
print(lst2)
for y in GDP.values():
    lst3.append(y)
lst3.sort()
print(lst3)
for z in lst2:
    if z=="India":
        lst4.append(z)
if len(lst4)==0:
    print("no")
else:
    print("yes")
a=sum(lst3)
print(a)

    
