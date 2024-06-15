lst=eval(input())
lst2=[]
for x in lst:
    if x==0:
        a=lst.pop(lst.index(x))
        lst2.append(a)
lst.extend(lst2)
if lst[0]==0:
    lst.remove(0)
    lst.extend([0])
print(lst)
