lst=eval(input())
lst2=[]
for i in lst:
    t=lst.count(i)
    if t==1:
        lst2.append(i)
    else:
        lst.remove(i)
print(lst2)
