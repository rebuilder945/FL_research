dic={}
while True:
    item=input()
    if item=="ok":
        break
    else:
        coun,GDP=item.split()
        GDP=eval(GDP)
        dic[coun]=GDP
lst1=list(dic.keys())
lst2=list(dic.values())
lst1.sort()
lst2.sort()
print(lst1)
print(lst2)
if 'India' in lst1:
    print('yes')
else:
    print('no')
he=sum(lst2)
print(he)

