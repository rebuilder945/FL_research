dic={}
while True:
    a=input().split()
    if a=="ok":
        break
    dic[0]=dic[1]
lst1=list(dic.keys())
lst2=list(dic.values())
print(lst1)
print(lst2)
print('India' in lst1)
print(sum(lst2)/len(lst2))

