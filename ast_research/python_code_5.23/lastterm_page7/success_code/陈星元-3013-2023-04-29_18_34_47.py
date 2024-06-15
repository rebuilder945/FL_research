GDP={}
lst1=[]
lst2=[]
while True:
    tuple1=tuple(input().split())
    if tuple1[0]=="ok":
        break
    else:
        key,value=tuple1
        value=int(value)
        GDP["{}".format(key)]=value
for key,value in GDP.items():
    lst1.append(key)
    lst2.append(value)
print(lst1.sort(key=lambda x:x[0],reverse=True))
print(lst2.sort(reverse=True))
if "India" in GDP:
    print("yes")
else:
    print("no")
print(sum(lst2))

