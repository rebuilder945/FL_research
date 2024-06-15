dic={}
while True:
    a=input()
    if a=="ok":
        break
    else:
        a=a.split()
        dic[a[0]]=a[1]
lst1=list(dic.keys())
lst1.sort()
lst2=list(dic.values())
lst2.sort()
for i in range(len(lst2)):
    lst2[i]=int(lst2[i])
print(lst1)
print(lst2)
if 'India' in lst1:
    print('yes')
else:
    print('no')
print(sum(lst2))

