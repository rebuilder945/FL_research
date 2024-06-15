dic={}
while True:
    a=input().split()
    if a=="ok":
        break
    if len(a)==2:
        dic[a[0]]=a[1]
lst1=list(dic.keys())
lst2=list(dic.values())
print(lst1)
print(lst2)
print('India' in lst1)
print(sum(lst2)/len(lst2))

