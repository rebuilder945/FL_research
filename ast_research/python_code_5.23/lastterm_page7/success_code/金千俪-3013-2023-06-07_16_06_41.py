a=input().split(" ")
GDP={}
while a[0]!="ok":
    GDP[a[0]]=a[1]
    a=input().split(" ")
lst=[x for x in GDP.keys()]
lst1=[i for i in GDP.values()]
lst.sort()
lst1.sort()
print(lst)
print(lst1)
for k in GDP.keys():
    if k=="India":
        print("yes")
    else:
        print("no")
        break
lst2=[]
for i in lst1:
    k=int(i)
    lst2.append(k)
print(sum(lst2))
