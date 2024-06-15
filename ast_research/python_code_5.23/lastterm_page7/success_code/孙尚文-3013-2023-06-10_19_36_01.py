dict={}
while True:
    a=input().split()
    b=a[0]
    if a==["ok"]:
        break
    else:
        c=a[1]
        dict[b]=c
lst1=[]
lst2=[]
for i in dict:
    lst1.append(i)
for i in dict.values():
    lst2.append(i)
lst1.sort()
lst2.sort()
print(lst1)

lst2=list(map(int,lst2))
print(lst2)
if "India" in dict:
    print("yes")
else:
    print("no")
print(sum(lst2))
