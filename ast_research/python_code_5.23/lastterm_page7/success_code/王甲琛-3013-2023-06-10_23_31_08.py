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
print('India' in lst1)
for i in range(len(lst2)):
    lst2[i]=int(lst2)
print(sum(lst2)/len(lst2))

