GDP={}
a=input()
while a!="ok":
    a,b=map(str,input().split(" "))
    GDP[a]=int(b)
lst1=[]
lst2=[]
for i in GDP.keys():
    lst1.append(i)
for x in GDP.values():
    lst2.append(x)
lst1.sort()
lst2.sort()
print(lst1)
print(lst2)
if "India" in GDP:
    print("yes")
else:
    print("no")
print(sum(lst2))

