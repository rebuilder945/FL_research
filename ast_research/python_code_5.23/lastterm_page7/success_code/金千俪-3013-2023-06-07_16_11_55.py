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
lst2=[]
for i in lst1:
    k=int(i)
    lst2.append(k)
print(lst2)
if "India" in GDP.keys():
    print("yes")
else:
    print("no")
print(sum(lst2))

