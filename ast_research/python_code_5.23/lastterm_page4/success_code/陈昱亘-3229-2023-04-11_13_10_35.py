lst=eval(input())
lst2=[]
for i in lst:
    if lst.count(i)==1:
        lst2.append(i)
if lst2==[]:
    print('False')
else:
    lst2.sort()
    lst3=list(map(str,lst2))
    str=','.join(lst3)
    print(str)
