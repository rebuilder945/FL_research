a=input().split(" ")
GDP={}
while a[0]!="ok":
    GDP[a[0]]=int(a[1])
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
print(sum(lst1))
