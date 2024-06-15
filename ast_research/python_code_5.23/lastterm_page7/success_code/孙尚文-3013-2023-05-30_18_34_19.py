dic={}
key=[]
value=[]
while True:
    a=input().split()
    if a=="ok":
        break
    dic[a[0]]=a[1]
    key.append(a[0])
    value.append(a[1])
value.sort()
print(dic)
print(key)
print(value)
if "india" in dic:
    print("yes")
else:
    print("no")
a=0
for i in value:
    a+=int(i)
print(a)
