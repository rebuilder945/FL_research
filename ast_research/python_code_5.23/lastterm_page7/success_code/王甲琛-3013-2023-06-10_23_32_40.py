dic={}
while True:
    a=input()
    if a=="ok":
        break
    else:
        a=a.split()
        dic[a[0]]=a[1]
lst1=list(dic.keys())
lst2=list(dic.values())
print(lst1)
print(lst2)
if 'India' in lst1:
    print('yes')
else:
    print('no')
for i in range(len(lst2)):
    lst2[i]=int(lst2[i])
print(sum(lst2))

