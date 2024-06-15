lst=eval(input())
lst2=[]
for x in lst:
    if x==0:
        a=lst.pop(lst.index(x))
        lst2.append(a)
lst.extend(lst2)
print(lst)
