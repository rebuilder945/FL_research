lst=eval(input())
lst2=[]
for i in lst:
    x=lst.count(i)
    if x==1:
        lst2.append(i)
lst2.sort()
if lst2==[]:
    print(False)
else:
    print(','.join(str(m) for m in lst2))



