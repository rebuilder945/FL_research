lst=eval(input())
lst2=[]
for x in lst:
    if lst.count(x)==1:
        lst2.append(x)
    
lst2.sort()
if lst2:
    print(','.join(str(i) for i in lst2))
else:
    print('False')
