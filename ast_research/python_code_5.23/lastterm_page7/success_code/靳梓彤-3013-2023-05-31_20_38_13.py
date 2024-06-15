GDP={}
lst1=[]
lst2=[]
while True:
    ls=input()
    if ls=="ok":
        break
    else:
        ls=list(ls.split(" "))
        GDP[ls[0]]=ls[1]
for x,y in GDP.items():
    lst1.append(x)
    lst2.append(int(y))
lst2.sort()
lst1.sort()
summery=sum(lst2)
print(lst1)
print(lst2,)
if "India" in GDP:
    print("yes",)
else:
    print("no")
print(summery)
