dict={}
while True:
    a=input().split()
    if a=="ok":
        break
    else:
        dict[a[0]]=a[1]
lst1=[]
lst2=[]
for i in dict:
    lst1.append(i)
for i in dict.values():
    lst2.append(i)
if "India" in dict:
    print("yes")
else:
    print("no")
print(sum[lst2])
